from manim import *
from numpy import *


class OrthogonalProjectionSlide(ThreeDScene):
    def construct(self):
        matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]

        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-3, 3, 1],
            axis_config={
                "include_numbers": True
            }
        )

        v1 = Vector([1, 0, 0], color=ORANGE, tip_length=0.25)
        v2 = Vector([0, 1, 0], color=ORANGE, tip_length=0.25)
        v3 = Vector([0, 0, 1], color=ORANGE, tip_length=0.25)

        vGroup = VGroup(v1, v2, v3)

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.add_background_rectangle(BLACK, 0.5)
        label.scale(0.8)
        self.add_fixed_in_frame_mobjects(label)
        label.to_corner(UR, buff=1)

        self.add(axes, vGroup)
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=PI/8)
        self.wait(5)
        # self.stop_ambient_camera_rotation()

        self.play(vGroup.animate.apply_matrix(matrix), run_time=3)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=3)
        # self.move_camera(phi=0, theta=-90 * DEGREES, added_anims=[vGroup.animate.apply_matrix(matrix)], run_time=3)
        self.wait(2)
