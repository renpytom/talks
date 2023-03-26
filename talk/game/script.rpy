# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init python:
    def big(d):
        return Fixed(
            Transform(d, fit="cover", xalign=0.5, yalign=0.5, blur=64),
            Transform(d, fit="contain", xalign=0.5, yalign=0.5),
        )

image logo spin:
    "logo base"
    yrotate 1


label main_menu:
    return

# The game starts here.

label start:

    camera:
        perspective True

    jump renpy

    scene bg roof

    title "Making Visual Novels with Ren'Py"
    subtitle "Tom Rothamel"
    subtitle "Brook Con II"
    subtitle "March 26, 2023"

    pause

    slide "Agenda"

    line "What are Visual Novels?"
    line "What is Ren'Py?"
    line "How do I make a Visual Novel with Ren'Py?"
    line "Q & A"

    pause


    title "What are Visual Novels?"
    pause

    hide screen slide

    "I think visual novels are a type of digital storytelling that uses text, images, sound, and more."

    show eileen vhappy at center
    with dissolve

    e "These elements can be combined to create different experiences."

    show eileen happy at right
    with ease

    menu:

        e "Visual Novels often have choices in them that affect the story."

        "That sounds cool!":
            pass

        "I don't like choices.":
            pass

    hide eileen

    scene bg advent

    slide "History of Visual Novels"
    pause

    scene bg portopia box

    oneline "The Portopia Serial Murder Case"
    pause

    show portopia:
        align (1.0, 1.0)
        offset (-20, -20)

    with dissolve

    pause

    # 1997
    scene bg toheart at big
    oneline "To Heart"
    pause

    # 1998
    scene bg kanon at big
    oneline "Kanon"
    pause

    # Ever17 2002/2005
    scene bg ever17 at big
    oneline "Ever 17 - Out of Infinity"
    pause

    # TOL1 # 2003
    scene bg tol1 at big
    oneline "Tales of Lemma 1"
    pause

    # Katawa Shoujo
    scene bg katawa at big
    oneline "Katawa Shoujo"
    pause

    # DDLC
    scene bg ddlc at big
    oneline "Doki Doki Literature Club"
    pause

    scene bg roof
    slide "Why Visual Novels?"
    pause

label renpy:

    slide "Test"
    pause

    scene bg roof

    title "What is Ren'Py?"
    add "logo base"
    subtitle "Free and Open Source Visual Novel Engine"
    smallsubtitle "for Windows, Mac, Linux, Android, iOS, Chromebook, Web"
    pause

    scene bg wolfhall at big

    slide "Ren'Py is meant for:"
    line "Visual Novels"
    line "Life Simulation Games"
    line "Choice Based RPGs"
    smallline ""
    smallline "but not all games."
    pause

    scene bg roof

    slide "Ren'Py is meant for:"
    line "Experienced Programmers"
    line "Intermediate Programmers"
    line "Non-Programmmers"
    smallline ""
    smallline "Our goal is to make it accessible to all creators."

    pause


label end:
    pause

    jump end
















    return
