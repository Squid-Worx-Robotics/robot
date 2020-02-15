import wpilib
from wpilib import drive
class DriveTrain:

    def initRobot(self):
        self.frontLeft = wpilib.Spark(1)
        self.rearLeft = wpilib.Spark(2)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

        self.frontRight = wpilib.Spark(3)
        self.rearRight = wpilib.Spark(4)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

    def drive(self, left_speed, right_speed):
        self.drive.tankDrive(left_speed, right_speed, True)


