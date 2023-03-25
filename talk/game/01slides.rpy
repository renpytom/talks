default slide_kind = "slide"
default slide_lines = [ ]

python early:

    class SlideLine:
        def __init__(self, kind, text):
            self.kind = kind
            self.text = text


    def parse(l):
        rv = l.require(l.simple_expression)
        l.expect_noblock("statement")
        l.expect_eol()

        return rv

    def execute(kind, p, title=False):
        global slide_kind
        global slide_lines

        if title:

            slide_kind = kind
            slide_lines = [ ]
            renpy.transition(Dissolve(.2))
            renpy.show_screen("slide")

        s = eval(p)

        slide_lines.append(SlideLine(kind, s))

    def stmt(name, **kwargs):
        renpy.register_statement(name, parse=parse, execute=renpy.partial(execute, name, **kwargs))

    stmt("slide", title=True)
    stmt("title", title=True)
    stmt("l")
    stmt("st")


screen slide():

    frame:
        if slide_kind == "slide":
            margin (20, 20)
            padding (40, 40)
        elif slide_kind == "title":
            margin (20, 20)
            padding (60, 60)
            align (0.5, 0.33)

        has vbox

        for l in slide_lines:

            if l.kind == "slide":

                text "[l.text]":
                    font "fonts/medium.ttf"
                    size 100

                null height 40

            elif l.kind == "title":

                text "[l.text]":
                    font "fonts/medium.ttf"
                    size 100
                    xalign 0.5
                    text_align 0.5

                null height 40

            elif l.kind == "l":

                    text "[l.text]":
                        size 80

            elif l.kind == "st":

                    text "[l.text]":
                        size 80
                        xalign 0.5
                        text_align 0.5

            else:

                text "Unknown kind: [l.kind]"
