define e = Character("Eileen")


label start:
    play music "sunflower-slow-drag.ogg"

    scene bg sac

    "I was at Brook Con, when someone came up to me..."

    show eileen happy
    with dissolve

    e "Hello there, I'm Eileen, and I've been with Ren'Py since the start."

menu:
    e "Would you like to learn how to make a Visual Novel?"
    "Yes!":
        jump attend_panel
    "I already did.":
        jump after_panel


label attend_panel:

    e "Great! I'll see you there!"

    return

label after_panel:

    show eileen vhappy
    with dissolve

    e "That's great! I hope you learned a lot."

    e "I'm looking forward to seeing what you create!"

    return
