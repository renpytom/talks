# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

transform midright:
    align (0.75, 1.0)

init python:
    def big(d):
        return Fixed(
            Transform(d, fit="cover", xalign=0.5, yalign=0.5, blur=64),
            Transform(d, fit="contain", xalign=0.5, yalign=0.5),
        )

    def launch(project=None, talk=""):
        import sys,os,subprocess

        environ = os.environ.copy()
        environ["TALK"] = talk

        cmd = [ sys.executable, sys.argv[0] ]

        if project:
            cmd.append(project)

        subprocess.Popen(cmd, env=environ)

    def Launch(project=None, talk=""):
        return Function(launch, project=project, talk=talk)

screen launch():
    zorder 10


    textbutton "Launch":
        action Launch()
        align (1.0, 1.0)
        margin (20, 20)
        padding (20, 20)

image logo spin:
    "logo base"
    yrotate 0.0
    easein 2.5 yrotate 720.0


label main_menu:
    return

# The game starts here.

label start:

    $ quick_menu = False

    scene bg roof

    title "Making Visual Novels with Ren'Py"
    add "logo base"
    subtitle "Tom Rothamel"
    subtitle "Brook Con {color=#00000020}II{/color}"
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

        e "Visual Novels often have choices in them that affect the story. What do you think about that?"

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

    scene bg roof

    title "What is Ren'Py?"
    add "logo spin"
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
    smallline "our goal is to make it accessible to all creators"

    pause

    show screen thumbs
    title "Thousands of Games Have Been\nMade with Ren'Py"
    pause

    hide screen thumbs


label renpy:
    scene bg roof

    title "How do I make a Visual Novel with Ren'Py?"
    pause

    show screen launch

    slide "Download, Install, and run Ren'Py"
    line "www.renpy.org"

    smallline ""
    smallline "Windows: Unpack and run renpy.exe"
    smallline "Mac: Move entire sdk to Applications, run renpy.app"
    smallline "Linux: Unpack and run renpy.sh"
    pause


    hide screen launch

    slide "Our First Script"

    example """
define e = Character("Eileen")

label start:
    scene bg sac
    "I was at Brook Con, when someone came up to me..."
    show eileen happy
    e "Hello there, I'm Eileen, and I've been with Ren'Py since the start."
    """

    pause

    slide "Dialogue"

    example '''"I was at Brook Con, when someone came up to me..."'''
    smallline "Narration in quotes."

    example '''e "Hello there, I'm Eileen, and I've been with Ren'Py since the start."'''
    smallline "When a character speaks, their short name is written first."

    example '''define e = Character("Eileen")'''
    smallline "Here, we define a short name for Eileen."
    pause

    slide "Image Names"

    line "Put the image files in images directory"
    smallline "'BG SAC.jpg' becomes 'bg sac'."
    smallline "'eileen happy.png' becomes 'eileen happy'."
    line "The first part of an image is the tag"
    smallline "For 'eileen happy', the tag is 'eileen'."
    line "The rest of the image name are the attributes"
    smallline "For 'eileen happy', the one attribute is 'happy'."
    line "Names start with a letter, and contain letters, numbers, and underscores"

    pause


    slide "Scene, Show, and Hide"

    example '''scene bg sac'''
    smallline "The scene statement hides everything, then shows one image."

    example '''show eileen happy'''
    smallline "The show statement shows an image."
    smallline "Replaces anything with the same tag."

    example '''hide eileen'''
    smallline "The hide statement hides an image."
    pause

    slide "Label, Jump, and Return"

    example '''label start:'''
    smallline "The label statement defines a label."
    smallline "The start label is special, it's where the game starts."

    example '''jump elsewhere'''
    smallline "The jump statement jumps to a label."
    smallline "The label can be found in any .rpy file."

    example '''return'''
    smallline "The return ends the game."
    pause


    slide "Choice Menus"

    example '''\
menu:
    e "Would you like to learn how to make a Visual Novel?"
    "Yes!":
        jump attend_panel
    "I already did.":
        jump after_panel
'''

    smallline "Always indent with four spaces."

    pause


    slide "Music"

    line "Put the music in the audio directory."

    example '''play music "sunflower-slow-drag.ogg"'''
    smallline "The play music statement plays music, and replaces playing music."

    example '''stop music'''
    smallline "The stop music statement stops playing music."

    pause

    show eileen happy at right
    with None

    slide "Transforms"


    example '''show eileen happy at right'''
    smallline "Introduced by at. Predefined transforms are right, left, and center."

    pause

    show eileen happy at midright
    with None

    slide "Custom Transforms"

    example '''transform midright:
    align (0.75, 1.0)'''

    smallline "The transform statement defines a custom transform"
    smallline "X from 0.0 (left) to 1.0 (right)."
    smallline "Y from 0.0 (top) to 1.0 (bottom)."

    example '''show eileen happy at midright'''

    pause




    slide "Transitions"

    example """\
show eileen happy at right
with dissolve
"""

    smallline "Add 'with dissolve' to blend from old to new."

    example """\
hide eileen
with fade
"""

    smallline "Add 'with fade' to fade to black and back."

    pause

    show eileen happy at right
    with dissolve

    pause

    hide eileen
    with fade
    pause


    slide "Python"

    example '''default score = 0'''
    smallline "The default statement sets the default value of a variable."

    example '''python:
    score = score + 1'''
    smallline "The python statement runs Python. In this case, it adds one to a variable."

    example '''if score > 3:
    jump good_end
else:
    jump bad_end
'''
    smallline "The if statement makes decisions."
    pause


    notitle "A Simple Game"

    tinyexample '''label rightaway:
    show sylvie green smile
    s "Hi there! How was class?"
    m "Good..."
    "I can't bring myself to admit that it all went in one ear and out the other."
    m "Are you going home now? Wanna walk back with me?"
    s "Sure!"
    scene bg meadow
    with fade
    "After a short while, we reach the meadows just outside the neighborhood where we both live."
    "It's a scenic view I've grown used to. Autumn is especially beautiful here."
    "When we were children, we played in these meadows a lot, so they're full of memories."
    m "Hey... Umm..."
    show sylvie green smile
    with dissolve
    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."
    "I'll ask her...!"
    m "Ummm... Will you..."
    m "Will you be my artist for a visual novel?"
    show sylvie green surprised
    "Silence."
    "She looks so shocked that I begin to fear the worst. But then..."
    show sylvie green smile
    menu:
        s "Sure, but what's a \"visual novel?\""
        "It's a videogame.":
            jump game
        "It's an interactive book.":
            jump book'''
    pause


    slide "What We Didn't Cover"

    line "Movie Playback"
    line "Voice Acting"
    line "Translations"
    line "ATL: Animation and Transformation Language"
    line "GUI: Simple Customization of the UI"
    line "Screen Language: Advanced Customization of the UI"
    line "Python: Can extend and improve Ren'Py"
    pause


    title "For More Information"

    subtitle "www.renpy.org"
    subtitle "Ren'Py Discord"
    smallsubtitle ""
    subtitle "Game Development & Design Club"
    pause

    title "Thank You!"
    subtitle "www.renpy.org"
    smallsubtitle ""
    subtitle "Q&A"
    pause

label end:
    pause

    jump end
