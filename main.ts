radio.onReceivedNumber(function (receivedNumber) {
    if (liv > 0) {
        if (receivedNumber == 0) {
            robobit.rotatems(RBRobotDirection.Left, 60, 400)
            robobit.go(RBDirection.Forward, 50)
        } else if (receivedNumber == 1) {
            robobit.rotatems(RBRobotDirection.Right, 60, 400)
            robobit.go(RBDirection.Forward, 50)
        } else if (receivedNumber == 2) {
            robobit.go(RBDirection.Reverse, 50)
        } else if (receivedNumber == 3) {
            robobit.go(RBDirection.Forward, 50)
        } else if (receivedNumber == 4) {
            robobit.stop(RBStopMode.Coast)
        } else {
        	
        }
    }
})
let liv = 0
radio.setGroup(3)
liv = 5
basic.showNumber(5)
robobit.setLedColor(0x659900)
while (liv > 0) {
    if (robobit.sonar(RBPingUnit.Centimeters) <= 5) {
        liv += -1
        if (liv == 4) {
            basic.showLeds(`
                . # . # .
                . # . # .
                . # # # #
                . . . # .
                . . . # .
                `)
            robobit.setLedColor(0x80FF80)
        } else if (liv == 3) {
            basic.showLeds(`
                . # # # .
                . # . # .
                . . # # #
                . . . . #
                . # # # #
                `)
            robobit.setLedColor(0xFFFF00)
        } else if (liv == 2) {
            basic.showLeds(`
                . # # . .
                # . . # .
                # . # . .
                . . # . .
                . # # # #
                `)
            robobit.setLedColor(0xFFC000)
        } else if (liv == 0) {
            basic.showLeds(`
                . . . # .
                . . # . .
                . . . . .
                . . # . .
                . . # . .
                `)
            robobit.setLedColor(0xFF8000)
        } else if (liv == 0) {
            robobit.stop(RBStopMode.Coast)
            basic.showIcon(IconNames.No)
            robobit.setLedColor(0xFF0000)
        } else {
        	
        }
    }
}
basic.forever(function () {
	
})
