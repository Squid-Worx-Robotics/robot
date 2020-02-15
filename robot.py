import magicbot
import wpilib
from components import DriveTrain

class MyRobot(magicbot.MagicRobot):

    drive_train: DriveTrain

    def createObjects(self):
        '''Create motors and stuff here'''
        self.drive_train.initRobot()
        pass

    def teleopInit(self):
        '''Called when teleop starts; optional'''
        self.controller = wpilib.XboxController(0)

    def teleopPeriodic(self):
        try:
            '''reads left hand stick value'''
            left_Y = self.controller.getY(0)
            right_Y = self.controller.getY(1)

            self.drive_train.drive(left_Y, right_Y)


        except:
            self.onException()


if __name__ == '__main__':
    wpilib.run(MyRobot)