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

        v1 = Vector([1, 0, 0], color=GREEN, tip_length=0.25)
        v2 = Vector([0, 1, 0], color=BLUE, tip_length=0.25)
        v3 = Vector([0, 0, 1], color=ORANGE, tip_length=0.25)

        vGroup = VGroup(v1, v2, v3)

        matrix_label = Matrix(matrix)
        matrix_label.set_column_colors(GREEN, BLUE, ORANGE)
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
        y_deg = -45
        z_deg = 45
        x_rotation = [
            [1, 0, 0],
            [0, cos(y_deg * DEGREES), -sin(y_deg * DEGREES)],
            [0, sin(y_deg * DEGREES), cos(y_deg * DEGREES)]
        ]
        y_rotation = [
            [cos(y_deg * DEGREES), 0, sin(y_deg * DEGREES)],
            [0, 1, 0],
            [-sin(y_deg * DEGREES), 0, cos(y_deg * DEGREES)]
        ]
        z_rotation = [
            [cos(z_deg * DEGREES), -sin(z_deg * DEGREES), 0],
            [sin(z_deg * DEGREES), cos(z_deg * DEGREES), 0],
            [0, 0, 1]
        ]

        x_rotation_matrix_body = MobjectMatrix([
            [MathTex("1"), MathTex("0"), MathTex("0")],
            [MathTex("0"), MathTex("cos(", y_deg, ")"),
             MathTex("-sin(", y_deg, ")")],
            [MathTex("0"), MathTex("sin(", y_deg, ")"),
             MathTex("cos(", y_deg, ")")]
        ], h_buff=2.5)

        y_rotation_matrix_body = MobjectMatrix([
            [MathTex("cos(", y_deg, ")"), MathTex(
                "0"), MathTex("sin(", y_deg, ")")],
            [MathTex(r"0"), MathTex("1"), MathTex("0")],
            [MathTex("-sin(", y_deg, ")"), MathTex("0"),
             MathTex("cos(", y_deg, ")")]
        ], h_buff=1.8)
        y_rotation_matrix_body.get_columns()[1].shift(LEFT)
        y_rotation_matrix_body.get_columns()[2].shift(0.6*LEFT)
        y_rotation_matrix_body.get_brackets()[1].shift(0.6*LEFT)

        z_rotation_matrix_body = MobjectMatrix([
            [MathTex("cos(", z_deg, ")"), MathTex(
                "-sin(", z_deg, ")"), MathTex("0")],
            [MathTex("sin(", z_deg, ")"), MathTex(
                "cos(", z_deg, ")"), MathTex("0")],
            [MathTex("0"), MathTex("0"), MathTex("1")]
        ], h_buff=2.2)
        z_rotation_matrix_body.get_columns()[2].shift(LEFT)
        z_rotation_matrix_body.get_brackets()[1].shift(LEFT)

        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-3, 3, 1],
            axis_config={
                "include_numbers": True
            }
        )

        v1 = Vector([1, 0, 0], color=GREEN, tip_length=0.25)
        v2 = Vector([0, 1, 0], color=BLUE, tip_length=0.25)
        v3 = Vector([0, 0, 1], color=ORANGE, tip_length=0.25)

        vGroup = VGroup(v1, v2, v3)

        y_matrix_text = MathTex("T=")
        y_matrix_text.next_to(y_rotation_matrix_body, LEFT)

        y_label = VGroup(y_rotation_matrix_body, y_matrix_text)
        y_label.add_background_rectangle(BLACK, 0.5)
        y_label.scale(0.8)

        z_matrix_text = MathTex("T=")
        z_matrix_text.next_to(z_rotation_matrix_body, LEFT)

        z_label = VGroup(z_rotation_matrix_body, z_matrix_text)
        z_label.add_background_rectangle(BLACK, 0.5)
        z_label.scale(0.8)

        self.add(axes, vGroup)
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        self.wait(2)

        self.add_fixed_in_frame_mobjects(y_label)
        y_label.to_corner(UR, buff=1)
        self.wait()

        self.begin_ambient_camera_rotation(rate=PI/8)

        self.play(vGroup.animate.apply_matrix(y_rotation), run_time=3)
        self.play(vGroup.animate.apply_matrix(y_rotation), run_time=3)

        self.remove(y_label)
        self.add_fixed_in_frame_mobjects(z_label)
        z_label.to_corner(UR, buff=1)
        self.wait()

        self.play(vGroup.animate.apply_matrix(z_rotation), run_time=3)
        self.play(vGroup.animate.apply_matrix(z_rotation), run_time=3)
        self.wait(3)
