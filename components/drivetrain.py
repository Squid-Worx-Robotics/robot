import wpilib
from wpilib import drive

class DriveTrain:


    def on_enable(self):
        """Called when the robot enters teleop or autonomous mode"""
        self.logger.info(
            "Robot is enabled: I have SOME_CONSTANT=%s", 5
        )
        self.left_speed = 0
        self.right_speed = 0

        self.frontLeft = wpilib.Spark(1)
        self.rearLeft = wpilib.Spark(2)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

        self.frontRight = wpilib.Spark(3)
        self.rearRight = wpilib.Spark(4)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

    def set_left(self, left):
        self.left_speed = left

    def set_right(self, right):
        self.right_speed = right

    def execute(self):
        self.drive.tankDrive(self.left_speed, self.right_speed, True)


