init python:
    import random
    thumbs = [ (i, random.random() * 3) for i in renpy.list_files() if i.startswith("thumbs/") and i.endswith(".png") ]
    random.shuffle(thumbs)

transform thumb_delay(param):
    zoom .5
    alpha 0.0
    pause param
    linear .5 alpha 1.0

transform slowgridmove:
    subpixel False
    xalign 0.5

    parallel:
        xpan 0.0
        linear 70 xpan 360.0
        repeat

    parallel:
        ypan 0.0
        linear 63 ypan 360.0
        repeat

screen thumbs():

    add "#000c"

    grid 12 11:

        at slowgridmove

        for i, delay in thumbs[:132]:
            add i  at thumb_delay(delay)
