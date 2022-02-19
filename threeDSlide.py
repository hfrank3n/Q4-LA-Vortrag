from manim import *
from numpy import *


class RotationAnimationSlide(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-3, 3, 1]
        )

        v1 = Vector([1, 0, 0], color=ORANGE)
        v2 = Vector([0, 1, 0], color=ORANGE)
        v3 = Vector([0, 0, 1], color=ORANGE)

        self.add(axes, v1, v2, v3)
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=2)
        self.wait()
        self.move_camera(theta=-45 * DEGREES, run_time=2)
        self.wait()
        self.begin_ambient_camera_rotation(rate=PI/4)
        self.wait(5)
