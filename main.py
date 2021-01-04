def on_received_number(receivedNumber):
    if liv > 0:
        if receivedNumber == 0:
            robobit.rotatems(RBRobotDirection.LEFT, 60, 400)
            robobit.set_pixel_color(0, 0x0000FF)
            robobit.set_pixel_color(1, 0x0000FF)
            robobit.go(RBDirection.FORWARD, 50)
        elif receivedNumber == 1:
            robobit.rotatems(RBRobotDirection.RIGHT, 60, 400)
            robobit.go(RBDirection.FORWARD, 50)
        elif receivedNumber == 2:
            robobit.go(RBDirection.REVERSE, 50)
        elif receivedNumber == 3:
            robobit.go(RBDirection.FORWARD, 50)
        elif receivedNumber == 4:
            robobit.stop(RBStopMode.COAST)
        else:
            pass
radio.on_received_number(on_received_number)

liv = 0
radio.set_group(3)
liv = 5
basic.show_number(5)
robobit.set_led_color(0x659900)
while liv < 0:
    if robobit.sonar(RBPingUnit.CENTIMETERS) <= 1:
        liv += -1
        if liv == 4:
            basic.show_leds("""
                . # . # .
                . # . # .
                . # # # #
                . . . # .
                . . . # .
                """)
            robobit.set_led_color(0x80FF80)
        elif liv == 3:
            basic.show_leds("""
                . # # # .
                . # . # .
                . . # # #
                . . . . #
                . # # # #
                """)
            robobit.set_led_color(0xFFFF00)
        elif liv == 2:
            basic.show_leds("""
                . # # . .
                # . . # .
                # . # . .
                . . # . .
                . # # # #
                """)
            robobit.set_led_color(0xFFC000)
        elif liv == 0:
            basic.show_leds("""
                . . . # .
                . . # . .
                . . . . .
                . . # . .
                . . # . .
                """)
            robobit.set_led_color(0xFF8000)
        elif liv == 0:
            robobit.stop(RBStopMode.COAST)
            basic.show_icon(IconNames.NO)
            robobit.set_led_color(0xFF0000)
        else:
            pass

def on_forever():
    pass
basic.forever(on_forever)
