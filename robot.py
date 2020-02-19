#!/usr/bin/env python3

import wpilib
from magicbot import MagicRobot

from components.component1 import Component1
from components.component2 import Component2
from components.drivetrain import DriveTrain


class MyRobot(MagicRobot):

    #
    # Define components here
    #

    component1: Component1
    component2: Component2
    drivetrain: DriveTrain

    # You can even pass constants to components
    SOME_CONSTANT = 1

    def createObjects(self):
        """Initialize all wpilib motors & sensors"""

        # TODO: create button example here

        self.component1_motor = wpilib.Talon(1)
        self.some_motor = wpilib.Talon(2)

        # self.joystick = wpilib.Joystick(0)
        self.controller = wpilib.XboxController(0)

    #
    # No autonomous routine boilerplate required here, anything in the
    # autonomous folder will automatically get added to a list
    #

    def teleopPeriodic(self):
        """Place code here that does things as a result of operator
           actions"""

        try:
            # if self.joystick.getTrigger():
            #     self.component2.do_something()

            '''reads left hand stick value'''
            left_Y = self.controller.getY(0)
            right_Y = self.controller.getY(1)

            self.drive_train.set_left(left_Y)
            self.drive_train.set_right(right_Y)
        except:
            self.onException()


if __name__ == "__main__":
    wpilib.run(MyRobot)
