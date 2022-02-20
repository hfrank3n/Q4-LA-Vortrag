from manim import *
from numpy import *


class OrthogonalProjectionQuestion(Scene):
    def construct(self):
        matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.add(matrix)


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


class OrthogonalProjectionSummary(Scene):
    def construct(self):
        matrix_body = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        matrix_text = MathTex("T=")
        matrix_text.next_to(matrix_body, LEFT)
        matrix = VGroup(matrix_body, matrix_text)
        matrix.to_corner(UL, buff=1)

        dot = MathTex(r"\cdot")
        vector = MobjectMatrix(
            [MathTex("x_1"), MathTex("x_2"), MathTex("x_3")])
        dot.next_to(vector, LEFT)
        multiplication = VGroup(dot, vector)

        eq = MathTex("=")
        result_vector = MobjectMatrix([
            MathTex(r"1\cdot x_1 + 0\cdot x_2 + 0\cdot x_3"),
            MathTex(r"0\cdot x_1 + 1\cdot x_2 + 0\cdot x_3"),
            MathTex(r"0\cdot x_1 + 0\cdot x_2 + 0\cdot x_3",)
        ])
        eq.next_to(result_vector, LEFT)
        result = VGroup(eq, result_vector)
        result_vector_simplified = VGroup(eq.copy(), MobjectMatrix([
            MathTex("x_1"),
            MathTex("x_2"),
            MathTex("0")
        ]))

        self.add(matrix)

        self.wait()
        matrix.remove(matrix_text)
        self.play(matrix.animate.to_corner(UL, buff=1),
                  FadeOut(matrix_text))
        multiplication.next_to(matrix)
        self.play(FadeIn(multiplication))
        result.next_to(multiplication)
        self.play(FadeIn(result))

        result_vector_simplified[0].next_to(result_vector_simplified[1], LEFT)
        result_vector_simplified.next_to(result, DOWN, buff=1)
        result_vector_simplified.shift(2*LEFT)
        self.play(FadeIn(result_vector_simplified))
        self.wait()


class OrthogonalProjectionSlideFull1(ThreeDScene):
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

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.add_background_rectangle(BLACK, 0.5)
        label.scale(0.8)
        self.add_fixed_in_frame_mobjects(label)
        label.to_corner(UR, buff=1)

        house = Cube(side_length=1.5)
        house.shift([0.75, 0.75, 0])

        self.add(axes, house)
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=PI/8)
        # self.wait(5)
        # self.stop_ambient_camera_rotation()

        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=3)
        # self.move_camera(phi=0, theta=-90 * DEGREES, added_anims=[vGroup.animate.apply_matrix(matrix)], run_time=3)
        # self.wait(2)


class OrthogonalProjectionSlideFull2(ThreeDScene):
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

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.add_background_rectangle(BLACK, 0.5)
        label.scale(0.8)
        self.add_fixed_in_frame_mobjects(label)
        label.to_corner(UR, buff=1)

        house = Cube(side_length=1.5)
        house.shift([0.75, 0.75, 3])

        self.add(axes, house)
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        self.wait(2)

        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=3)

        self.begin_ambient_camera_rotation(rate=PI/8)
        self.wait()
        self.stop_ambient_camera_rotation()
