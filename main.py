def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # # .
                        . . . . .
                        . . . . .
        """)
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # # # .
                        . . . . .
                        . . . . .
        """)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.clear_screen()
radio.on_received_number(on_received_number)

def on_logo_long_pressed():
    radio.send_number(1)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_logo_pressed():
    radio.send_number(0)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
