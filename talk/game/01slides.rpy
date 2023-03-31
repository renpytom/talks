default slide_kind = "slide"
default slide_lines = [ ]

python early:

    class SlideLine:
        def __init__(self, kind, text):
            self.kind = kind
            self.text = text


    def parse(l):
        rv = l.require(l.rest)

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
    stmt("oneline", title=True)
    stmt("notitle", title=True)
    stmt("line")
    stmt("smallline")
    stmt("subtitle")
    stmt("smallsubtitle")
    stmt("add")

    stmt("example")
    stmt("tinyexample")


screen slide():
    zorder 500

    fixed:

        at Transform(perspective=True)

        frame:
            if slide_kind == "slide":
                margin (20, 20)
                top_padding 40
                bottom_padding 40
                left_padding 40
                right_padding 80
            elif slide_kind == "oneline":
                margin (20, 20)
                padding (40, 40)
            elif slide_kind == "title":
                margin (20, 20)
                padding (60, 60)
                align (0.5, 0.33)
            if slide_kind == "notitle":
                background Null()
                margin (20, 20)

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

                elif l.kind == "notitle":

                    pass

                elif l.kind == "line" or l.kind == "oneline":

                    text "[l.text]":
                        line_spacing -15
                        size 70

                elif l.kind == "smallline":

                    text "[l.text]":
                        size 45

                elif l.kind == "subtitle":

                    text "[l.text]":
                        size 80
                        xalign 0.5
                        text_align 0.5

                elif l.kind == "smallsubtitle":

                    text "[l.text]":
                        size 50
                        xalign 0.5
                        text_align 0.5

                elif l.kind == "example":

                    frame:
                        top_margin 20
                        bottom_padding 30
                        left_padding 20
                        right_padding 20
                        text example_code(l.text):
                            size 50
                            color "#101010"

                elif l.kind == "tinyexample":

                    frame:
                        top_margin -20
                        bottom_padding 20
                        left_padding 20
                        right_padding 20
                        text example_code(l.text):
                            size 27
                            color "#101010"


                elif l.kind == "add":

                    add l.text xalign 0.5

                else:

                    text "Unknown kind: [l.kind]"
