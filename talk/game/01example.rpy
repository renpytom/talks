python early:

    # This maps from example name to the text of a fragment.
    examples = { }

    # The size of the example - large or small.
    example_size = "small"

    # The location of the example - top or bottom.
    example_location = "top"

    # The screen in the last example.
    example_screen = None

    # A transition used with examples
    example_transition = None

    def reset_example():
        """
        Called to reset the example code to the defaults.
        """

        global example_size
        global example_location
        global example_screen

        example_size = "small"
        example_location = "top"
        example_screen = None

    def show_example_screen(name):
        global example_screen
        example_screen = name
        renpy.show_screen(name)

    def hide_example_screen():
        global example_screen

        if example_screen is not None:
            renpy.hide_screen(example_screen)

        example_screen = None


    # Keywords that, at the start of an example block, cause it to be
    # outdented
    OUTDENT_KEYWORDS = { "define", "default", "image", "screen", "init", "transform", "label", "style" }


    # This defines the example statement.
    #
    # The example statement takes:
    # * An optional name for the example.
    # * An optional hide flag.
    # * Optional size flags, large or small.
    # * Optional position flags, top or bottom.
    #
    # The statement defines an example with the name, or an anyonymous name if no
    # name is given. When run, the example is displayed if the hide flag is not
    # given.


    def read_example(name, fn, line, outdent):
        """
        This reads an example from an example statement, and places it into
        the examples dictionary.
        """

        fn = fn.replace("game/", "")

        with renpy.notl_file(fn) as f:
            data = f.read()

        rawlines = [ i.rstrip() for i in data.split("\n") ]

        lines = [ ]

        base_indent = 0

        while True:

            if line >= len(rawlines):
                raise Exception("Example open at end of {}.".format(fn))

            l = rawlines[line]
            line += 1

            if not l:
                lines.append(l)
                continue

            indent = len(l) - len(l.lstrip())

            if base_indent == 0:
                base_indent = indent
                lines.append(l[4:])
            elif indent >= base_indent:
                lines.append(l[4:])
            else:
                break

        # Determine if the line should be indented.
        if outdent == "auto":

            for i in lines:
                l = i.strip().split()
                if not l:
                    continue

                if l[0] in OUTDENT_KEYWORDS:
                    outdent = True
                else:
                    outdent = False

                break

        # Strip indentation.
        if outdent:
            lines = [ i[base_indent - 4:] for i in lines ]

        if name in examples:
            examples[name].append('')
            examples[name].extend(lines)
        else:
            examples[name] = lines

    def parse_example(l):
        """
        This parses the example statement.
        """

        name = l.require(l.name)
        l.require(':')
        l.expect_eol()

        if name is None:
            name = "example_{}_{}".format(l.filename, l.number)

        ll = l.subblock_lexer()
        ll.advance()

        if ll.keyword('screen'):
            screen_name = ll.name()
        else:
            screen_name = None

        return {
            "name" : name,
            "filename" : l.filename,
            "number" : l.number,
            }

    def next_example(data, first):
        return first

    def execute_example(data):
        # This doesn't need to do anything.
        return

    def execute_init_example(data):
        read_example(data["name"], data["filename"], data["number"], "auto")

    renpy.register_statement("example", parse=parse_example, execute=execute_example, execute_init=execute_init_example, next=next_example, block="script")



init python:

    import re
    import keywords

    KEYWORDS = set(keywords.keywords)
    PROPERTIES = set(keywords.properties)

    regex = r"(?P<word>\b(\$|[_a-zA-Z0-9]+)\b)" + \
        r"|(?P<string>\"([^\"]|\\.)*(?<!\\)\")" + \
        r"|(?P<comment>#.*)"

    regex = re.compile(regex)

    def quote(s):
        s = s.replace("{", "{{")
        s = s.replace("[", "[[")

        return s

    def colorize(m):
        if m.group("string"):
            return "{color=#060}" + m.group(0) + "{/color}"

        word = m.group("word")
        if word:
            if word in KEYWORDS:
                return "{color=#840}" + m.group(0) + "{/color}"
            elif word in PROPERTIES:
                return "{color=#048}" + m.group(0) + "{/color}"
            else:
                return m.group(0)

        if m.group("comment"):
            return "{color=#600}" + m.group(0) + "{/color}"

        return m.group(0)

    def example_code(text):

        last_blank = False

        lines = [ ]

        for i in text.split("\n"):

            if not i and last_blank:
                continue

            last_blank = not i

            i = re.sub(r'(label \w+)__\w+', r'\1', i)

            if True:
                i = re.sub(r'__?\((".*?")\)', r'\1', i)
                i = re.sub(r"__?\(('.*?')\)", r'\1', i)
                i = i.replace("!t]", "]")

            i = quote(i)
            i = regex.sub(colorize, i)

            lines.append(i)

        while not lines[-1]:
            lines.pop()

        while lines and not lines[0]:
            lines.pop(0)

        # Join them into a single string.
        return "\n".join(lines)
