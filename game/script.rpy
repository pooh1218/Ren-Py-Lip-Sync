define akuto = Character("akuto", color="#f99c30")
define michael = Character("michael", color="#00ff00")

layeredimage akuto:
    zoom 3.0
    group mouth:
        attribute mouth_A:
            "Papi_p1_flirt1.png"
        attribute mouth_B:
            "Papi_p1_flirt2.png"
        attribute mouth_C:
            "Papi_p1_happy1.png"
        attribute mouth_D:
            "Papi_p1_happy2.png"
        attribute mouth_E:
            "Papi_p2_normal1.png"
        attribute mouth_F:
            "Papi_p2_normal2.png"
        attribute mouth_X default:
            "Papi_p1_default.png"

layeredimage michael:
    zoom 3.0
    group mouth:
        attribute mouth_a:
            "Michael_embarassed1.png"
        attribute mouth_b:
            "Michael_embarassed2.png"
        attribute mouth_c:
            "Michael_normal1.png"
        attribute mouth_d:
            "Michael_normal2.png"
        attribute mouth_e:
            "Michael_sad1.png"
        attribute mouth_f:
            "Michael_sad2.png"
        attribute mouth_X default:
            "Michael_default.png"
        
# Note: Lip-sync requires audio files in .wav format.
# Note: Prepare lip-sync data using generate_lipsync_data.py.

label start:
    # show akuto at left
    show akuto at left
    show michael at right


    akuto "Hello, I'm akuto."
    akuto "Watch me lip-sync."

    michael "Hi, I'm a new character."
    michael "I can lip-sync too."
    # Play the lip-sync animation for the given audio file.
    # parameters are : character, audio file, text to display
    $ lipsync(akuto, "Akuto_Are you comfortable.ogg", "Are you comfortable?")
    $ lipsync(michael, "Chris_W5_ICanHelp.ogg", "I can help.")
    $ lipsync(akuto, "Akuto_I'm just babysitting you.ogg", \
        "I'm just babysitting you.")
    $ lipsync(michael, "Chris_W5_YeahYouStillHaveMuch.ogg", "Yeah, you still have Much.")
    $ lipsync(akuto, "Akuto_Maybe they did.ogg", "Maybe they did.")
    $ lipsync(michael, "Chris_W6_It'sTime.ogg", "It's Time.")
    "Thank you for watching!"