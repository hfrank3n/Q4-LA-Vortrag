from manim import *
from numpy import *


class ShearAnimationSlide(ThreeDScene):
    def construct(self):
        matrix = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]

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
        self.wait(2)
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=2)
        self.wait()
        self.begin_ambient_camera_rotation(rate=PI/8)
        self.play(vGroup.animate.apply_matrix(matrix), run_time=3)
        self.play(vGroup.animate.apply_matrix(linalg.inv(matrix)), run_time=3)
        self.play(vGroup.animate.apply_matrix(matrix), run_time=3)
        self.play(vGroup.animate.apply_matrix(linalg.inv(matrix)), run_time=3)
        self.wait(4)


class RotationAnimationSlide(ThreeDScene):
    def construct(self):
        deg = -45
        x_rotation = [
            [1, 0, 0],
            [0, cos(deg * DEGREES), -sin(deg * DEGREES)],
            [0, sin(deg * DEGREES), cos(deg * DEGREES)]
        ]
        y_rotation = [
            [cos(deg * DEGREES), 0, sin(deg * DEGREES)],
            [0, 1, 0],
            [-sin(deg * DEGREES), 0, cos(deg * DEGREES)]
        ]

        x_rotation_matrix_body = MobjectMatrix([
            [MathTex("1"), MathTex("0"), MathTex("0")],
            [MathTex("0"), MathTex("cos(", deg, ")"),
             MathTex("-sin(", deg, ")")],
            [MathTex("0"), MathTex("sin(", deg, ")"),
             MathTex("cos(", deg, ")")]
        ], h_buff=2.2)
        y_rotation_matrix_body = MobjectMatrix([
            [MathTex("cos(", deg, ")"), MathTex(
                "0"), MathTex("sin(", deg, ")")],
            [MathTex("0"), MathTex("1"), MathTex("0")],
            [MathTex("-sin(", deg, ")"), MathTex("0"),
             MathTex("cos(", deg, ")")]
        ], h_buff=1.8)
        z_rotation_matrix_body = MobjectMatrix([[MathTex("cos(", deg, ")"), MathTex("-sin(", deg, ")"), MathTex("0")], [
                                               MathTex("sin(", deg, ")"), MathTex("cos(", deg, ")"), MathTex("0")], [MathTex("0"), MathTex("0"), MathTex("1")]])

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

        matrix_text = MathTex("T=")
        matrix_text.next_to(y_rotation_matrix_body, LEFT)

        label = VGroup(y_rotation_matrix_body, matrix_text)
        label.add_background_rectangle(BLACK, 0.5)
        label.scale(0.8)
        self.add_fixed_in_frame_mobjects(label)
        label.to_corner(UR, buff=1)

        self.add(axes, vGroup)
        self.wait(2)
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=2)
        self.wait()
        self.begin_ambient_camera_rotation(rate=PI/8)
        self.play(vGroup.animate.apply_matrix(y_rotation), run_time=3)
        self.play(vGroup.animate.apply_matrix(y_rotation), run_time=3)
        self.play(vGroup.animate.apply_matrix(y_rotation), run_time=3)
        self.play(vGroup.animate.apply_matrix(y_rotation), run_time=3)
        self.wait()
