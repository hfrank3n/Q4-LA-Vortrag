from manim import *
from numpy import *


class Slide(Scene):
    def construct(self):
        title = Tex(r"Title", font_size=80)
        title.to_edge(UP)
        self.add(title)

        textGroup = VGroup(
            Tex("lorem ", "ipsum ", "dolor ", "sit ", "amet"),
            Tex("consetetur sadipscing elitr"),
            Tex("sed diam nonumy eirmod tempor"),
            Tex("ipsum ", "amet ", "amet ", "consetetur ", "sit")
        )

        textGroup.arrange(DOWN, buff=MED_SMALL_BUFF)
        for line in textGroup:
            line.set_color_by_tex_to_color_map({
                "lorem": BLUE,
                "ipsum": GREEN,
                "sit": TEAL
            })
            line.set_font_size(40)
        textGroup.to_edge(LEFT)
        self.add(textGroup)

        to_isolate = ["B", "C", "=", "(", ")"]
        mathGroup = VGroup(
            # isolate Tex string into multiple subjects (so they can be treated separately)
            MathTex("A^2", "+", "B^2", "=", "C^2"),
            MathTex("A^2 = (C + B)(C - B)",
                    substrings_to_isolate=["A^2", *to_isolate]),
            MathTex("A = \\sqrt{(C + B)(C - B)}", substrings_to_isolate=["A", *to_isolate]))
        mathGroup.arrange(DOWN, buff=MED_SMALL_BUFF)
        for line in mathGroup:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN
            })
        mathGroup.to_edge(RIGHT)
        self.add(mathGroup)


class LineareTransformationenSlide(Scene):
    def construct(self):
        text1 = Tex("Lineare ", font_size=50)
        text2 = Tex("Transformation", font_size=50)
        text = VGroup(text1, text2)
        text.arrange(RIGHT)
        text.to_corner(LEFT + UP, buff=1)

        brace = Brace(text2, sharpness=0.7)

        function_equation = MathTex(r"T(\vec{v_1})=\vec{v_2}")
        function_equation.next_to(brace, DOWN)

        matrix_equation = MathTex(r"T\cdot\vec{v_1}=\vec{v_2}")
        matrix_equation.next_to(function_equation, buff=4)
        matrix_equation.to_edge(RIGHT, buff=1.4)

        rotation_matrix_45deg = [
            [cos(radians(45)), -sin(radians(45))], [sin(radians(45)), cos(radians(45))]]
        left_grid = Axes(
            x_range=[-0.8, 2, 1],
            y_range=[-0.8, 2, 1],
            x_length=2.8,
            y_length=2.8,
            axis_config={
                "include_numbers": True,
                "font_size": 24,
                "tip_length": 0.2
            },
            tips=True,
        )

        v1 = Vector([1, 0], tip_length=0.25, color=GREEN)
        v2 = Vector([0, 1], tip_length=0.25, color=BLUE)
        vGroup = VGroup(v1, v2)
        left_grid.add(vGroup)

        transformation_arrow = MathTex(r"\longleftrightarrow", font_size=80)
        transformation_text = Tex("T")
        transformation_text.next_to(transformation_arrow, UP, buff=-0.06)
        transformation_label = VGroup(
            transformation_arrow, transformation_text)

        right_grid = left_grid.copy()
        right_grid[2].apply_matrix(rotation_matrix_45deg)

        left_grid[2].shift(left_grid.get_origin())
        right_grid[2].shift(right_grid.get_origin())

        left_grid.to_corner(LEFT+DOWN, buff=1)
        transformation_label.next_to(left_grid, buff=1, aligned_edge=RIGHT)
        right_grid.next_to(transformation_label, buff=1, aligned_edge=LEFT)

        matrix_body = Matrix([["i_1", "j_1"], ["i_2", "j_2"]], h_buff=1.0)
        matrix_body.set_column_colors(GREEN, BLUE)
        matrix_label = MathTex(r"T =")
        matrix_label.next_to(matrix_body, direction=LEFT)
        matrix = VGroup(matrix_body, matrix_label)
        matrix.next_to(matrix_equation, direction=DOWN, buff=2)
        matrix.to_edge(RIGHT, buff=1)

        self.add(text, brace, function_equation, matrix_equation)
        self.add(left_grid, right_grid, transformation_label, matrix)


class MatrixMultiplication(Scene):
    def construct(self):

        general_equation = MathTex(r"T\cdot\vec{v_1}=\vec{v_2}")
        general_equation.to_corner(LEFT + UP, buff=1.0)

        matrix = Matrix([["i_1", "j_1"], ["i_2", "j_2"]])
        dot = MathTex(r"\cdot")
        vector = MobjectMatrix([MathTex("x_1"), MathTex("x_2")])
        eq = MathTex("=")

        i_vec = MobjectMatrix([MathTex("i_1"), MathTex("i_2")])
        j_vec = MobjectMatrix([MathTex("j_1"), MathTex("j_2")])
        i_vec.set_column_colors(GREEN)
        j_vec.set_column_colors(BLUE)
        tmp1 = MathTex(r"x_1")
        tmp2 = MathTex(r"+\,\, x_2")
        i_vec.next_to(tmp1)
        tmp2.next_to(i_vec)
        j_vec.next_to(tmp2)
        result_equation = VGroup(i_vec, tmp1, j_vec, tmp2)

        tmp3 = MathTex("=")
        result_vector = MobjectMatrix([
            MathTex(
                r"{{ i_1 }}\cdot {{x_1}}+{{j_1}}\cdot {{x_2}}"),
            MathTex(r"{{ i_2 }} \cdot {{x_1}} + {{ j_2 }}\cdot {{x_2}}"),
        ])
        for list in result_vector:
            for mobj in list.submobjects[0:-1]:
                print(mobj.get_tex_string())
                if (mobj.get_tex_string() == " i_1 " or mobj.get_tex_string() == " i_2 "):
                    mobj.set_color(GREEN)
                if (mobj.get_tex_string() == " j_1 " or mobj.get_tex_string() == " j_2 "):
                    mobj.set_color(BLUE)
                if mobj == "j_1":
                    mobj.set_color(BLUE)
        matrix.next_to(general_equation, DOWN, buff=1)
        dot.next_to(matrix)
        vector.next_to(dot)
        eq.next_to(vector)
        result_equation.next_to(eq)

        tmp3.next_to(eq, DOWN, buff=2)
        tmp3.to_edge(LEFT, buff=1)
        result_vector.next_to(tmp3)
        result = VGroup(tmp3, result_vector)

        equation = VGroup(matrix, dot, vector, eq, result_equation, result)

        self.add(general_equation, equation, result)

        # self.wait()
        # self.play(matrix.animate.to_corner(UL, buff=1), FadeOut(matrix_text))
        # multiplication.next_to(matrix)
        # self.play(FadeIn(multiplication))
        # result.next_to(multiplication)
        # self.play(FadeIn(result))

        # result_vector_simplified[0].next_to(result_vector_simplified[1], LEFT)
        # result_vector_simplified.next_to(result, DOWN, buff=1)
        # result_vector_simplified.shift(2*LEFT)
        # self.play(FadeIn(result_vector_simplified))
        # self.wait()


class ShearSummarySlide(Scene):
    def construct(self):
        grid1 = Axes(
            x_range=[-0.8, 2.5, 1],
            y_range=[-0.8, 2.5, 1],
            x_length=3.3,
            y_length=3.3,
            axis_config={
                "include_numbers": True,
                "font_size": 24,
                "tip_length": 0.2
            },
            tips=True,
        )

        v1 = Vector([1, 0], tip_length=0.25, color=ORANGE)
        v1_label = v1.coordinate_label()
        v1_label.scale(0.5)
        v1_label.next_to(v1.get_end(), UP + RIGHT)

        v2 = Vector([0, 1], tip_length=0.25, color=ORANGE)
        v2_label = v2.coordinate_label()
        v2_label.scale(0.5)
        v2_label.next_to(v2.get_end(), RIGHT, buff=MED_SMALL_BUFF)

        v3 = Vector([1, -1], tip_length=0.25, color=BLUE)
        v3_label = v3.coordinate_label(color=BLUE)
        v3_label.scale(0.5)
        v3_label.next_to(v3.get_end(), RIGHT)

        vGroup = VGroup(v1, v2, v3, v1_label, v2_label, v3_label)
        grid1.add(vGroup)

        grid1[2].shift(grid1.get_origin())

        grid2 = Axes(
            x_range=[-0.8, 2.5, 1],
            y_range=[-0.8, 2.5, 1],
            x_length=3.3,
            y_length=3.3,
            axis_config={
                "include_numbers": True,
                "font_size": 24,
                "tip_length": 0.2
            },
            tips=True,
        )

        v4 = Vector([2, 0], tip_length=0.25, color=ORANGE)
        v4_label = v4.coordinate_label()
        v4_label.scale(0.5)
        v4_label.next_to(v4.get_end(), UP)

        v5 = Vector([0, 2], tip_length=0.25, color=ORANGE)
        v5_label = v5.coordinate_label()
        v5_label.scale(0.5)
        v5_label.next_to(v5.get_end(), RIGHT)

        v6 = Vector([2, -2], tip_length=0.25, color=BLUE)
        v6_label = v6.coordinate_label(color=BLUE)
        v6_label.scale(0.5)
        v6_label.next_to(v6.get_end(), UP + RIGHT)

        vGroup2 = VGroup(v5, v4, v6, v4_label, v5_label, v6_label)
        grid2.add(vGroup2)

        grid2[2].shift(grid2.get_origin())

        grid1.to_corner(UL, buff=1)
        grid2.next_to(grid1, RIGHT)
        grid2.to_edge(UP, buff=1)

        equation_matrix_mul = MathTex(
            r"T = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} = 2 \cdot \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}", font_size=40)

        equation_matrix_mul.to_corner(UR, buff=1)

        other_equation = MathTex(
            r"""\vec{v'} &= T \cdot \vec{v} \\ %
				&= \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ -1 \end{bmatrix} \\ %
				&= \begin{bmatrix} 1 \cdot 2 - 1 \cdot 0 \\ 1 \cdot 0 - 2 \end{bmatrix} = \begin{bmatrix} 2 \\ -2 \end{bmatrix}""",
            color=BLUE, font_size=40)

        other_equation.next_to(equation_matrix_mul, DOWN)

        label_grid1 = grid1.get_axis_labels(
            Tex("x").scale(0.7), Tex("y").scale(0.7))
        label_grid2 = grid2.get_axis_labels(
            Tex("x").scale(0.7), Tex("y").scale(0.7))

        self.add(grid1, grid2, equation_matrix_mul,
                 other_equation, label_grid1, label_grid2)


class ScaleAnimationSlide(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            include_foreground_plane=False
        )

    def construct(self):
        matrix = [[2, 0], [0, 2]]

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.to_corner(UR, buff=1)
        label.add_background_rectangle(BLACK, 0.5)
        self.add(label)

        self.apply_matrix(matrix)
        self.wait()


class ScaleFullAnimationSlide(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[2, 0], [0, 2]]

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.to_corner(UR, buff=1)
        label.add_background_rectangle(BLACK, 0.5)
        self.add(label)

        self.apply_matrix(matrix, run_time=5)
        self.wait()


class ShearAnimationSlide1(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            include_foreground_plane=False
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.to_corner(UR, buff=1)
        label.add_background_rectangle(BLACK, 0.5)
        self.add(label)


class ShearAnimationSlide2(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.to_corner(UR, buff=1)
        label.add_background_rectangle(BLACK, 0.5)
        self.add(label)

        self.apply_matrix(matrix)
        self.wait()


class ShearAnimationSlide3(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            include_foreground_plane=False
        )

    def construct(self):
        matrix = [[1, 0], [1, 1]]

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.to_corner(UR, buff=1)
        label.add_background_rectangle(BLACK, 0.5)
        self.add(label)
        self.apply_matrix(matrix)
        self.wait()


class ShearAnimationSlide4(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[2, 1], [1, 2]]

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.to_corner(UR, buff=1)
        label.add_background_rectangle(BLACK, 0.5)
        self.add(label)
        self.apply_matrix(matrix)
        self.wait()


class RotationSummarySlide(Scene):
    def construct(self):
        grid1 = Axes(
            x_range=[-0.8, 2.5, 1],
            y_range=[-0.8, 2.5, 1],
            x_length=3.3,
            y_length=3.3,
            axis_config={
                "include_numbers": True,
                "font_size": 24,
                "tip_length": 0.2
            },
            tips=True,
        )

        v1 = Vector([1, 0], tip_length=0.25, color=ORANGE)
        v1_label = v1.coordinate_label()
        v1_label.scale(0.5)
        v1_label.next_to(v1.get_end(), UP + RIGHT)

        v2 = Vector([0, 1], tip_length=0.25, color=ORANGE)
        v2_label = v2.coordinate_label()
        v2_label.scale(0.5)
        v2_label.next_to(v2.get_end(), RIGHT, buff=MED_SMALL_BUFF)

        vGroup = VGroup(v1, v2, v1_label, v2_label)
        grid1.add(vGroup)

        grid1[2].shift(grid1.get_origin())

        grid2 = Axes(
            x_range=[-0.8, 2.5, 1],
            y_range=[-0.8, 2.5, 1],
            x_length=3.3,
            y_length=3.3,
            axis_config={
                "include_numbers": True,
                "font_size": 24,
                "tip_length": 0.2
            },
            tips=True,
        )

        v4 = Vector([0, -1], tip_length=0.25, color=ORANGE)
        v4_label = v4.coordinate_label()
        v4_label.scale(0.5)
        v4_label.next_to(v4.get_end(), RIGHT)

        v5 = Vector([1, 0], tip_length=0.25, color=ORANGE)
        v5_label = v5.coordinate_label()
        v5_label.scale(0.5)
        v5_label.next_to(v5.get_end(), UP)

        vGroup2 = VGroup(v5, v4, v4_label, v5_label)
        grid2.add(vGroup2)

        grid2[2].shift(grid2.get_origin())

        grid1.to_corner(UL, buff=1)
        grid2.next_to(grid1, RIGHT, buff=1)
        grid2.to_edge(UP, buff=1)

        matrix_body = Matrix([[0, 1], [-1, 0]])
        matrix_label = MathTex("T=")
        matrix_label.next_to(matrix_body, LEFT)
        matrix = VGroup(matrix_body, matrix_label)
        matrix.to_corner(UR, buff=1)

        label_grid1 = grid1.get_axis_labels(
            Tex("x").scale(0.7), Tex("y").scale(0.7))
        label_grid2 = grid2.get_axis_labels(
            Tex("x").scale(0.7), Tex("y").scale(0.7))

        self.add(grid1, grid2, matrix,
                 label_grid1, label_grid2)


class RotationAnimationSlide(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            include_foreground_plane=False
        )

    def construct(self):
        matrix = [[0, 1], [-1, 0]]

        matrix_body = Matrix(matrix)
        matrix_text = MathTex("T=")
        matrix_text.next_to(matrix_body, LEFT)
        matrix_label = VGroup(matrix_body, matrix_text)
        matrix_label.to_corner(UR, buff=1)
        matrix_label.add_background_rectangle(BLACK, 0.5)

        self.add(matrix_label)
        self.apply_matrix(matrix)
        self.wait()


class RotationFullAnimationSlide(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[0, 1], [-1, 0]]

        matrix_body = Matrix(matrix)
        matrix_text = MathTex("T=")
        matrix_text.next_to(matrix_body, LEFT)
        matrix_label = VGroup(matrix_body, matrix_text)
        matrix_label.to_corner(UR, buff=1)
        matrix_label.add_background_rectangle(BLACK, 0.5)

        self.add(matrix_label)
        self.apply_matrix(matrix)
        self.wait()


class RotationUnitCircleSlide(LinearTransformationScene):
    deg = 45
    last_deg = 0
    cos

    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False
        )

    def construct(self):
        matrix_label = MathTex(
            r"T=\begin{bmatrix} cos(\alpha) & -sin(\alpha) \\ sin(\alpha) & cos(\alpha) \end{bmatrix}")
        matrix_label.to_corner(UR, buff=1)
        matrix_label.add_background_rectangle(BLACK, 0.5)
        alpha = MathTex(r"\alpha=")
        number = DecimalNumber()
        alpha.next_to(number, LEFT)
        label = VGroup(alpha, number)
        label.next_to(matrix_label, DOWN)
        label.add_background_rectangle(BLACK, 0.5)
        number.add_updater(self.update_label)
        self.add(alpha, label, matrix_label)

        circle = self.get_circle()
        self.add(circle)

        i_hat = Arrow(start=circle.get_center(),
                      end=circle.point_at_angle(0), color=GREEN)
        i_hat.add_updater(self.update_i_hat)

        self.cos = Line(start=circle.get_center(),
                        end=circle.point_at_angle(0))
        self.cos.add_updater(self.update_cos)

        sin = Line(start=circle.get_center(),
                   end=circle.point_at_angle(radians(90)))
        sin.add_updater(self.update_sin)

        self.add(self.cos)
        self.add(sin)
        self.add(i_hat)

        for _ in range(8):
            self.rotation(radians(self.deg))

    def rotation(self, rad):
        # rad = deg*(pi/180)
        matrix = [[cos(rad), -sin(rad)], [sin(rad), cos(rad)]]
        self.apply_matrix(matrix)
        self.wait(duration=0.1)

    def get_curr_deg(self):
        i_hat = self.i_hat.get_end()[:2]
        x_axis = [1, 0]

        curr_deg = degrees(arccos(array(i_hat)@x_axis) /
                           (linalg.norm(i_hat)*linalg.norm(x_axis)))

        if (round(self.last_deg) >= 180) and not (round(self.last_deg) == 360):
            curr_deg = 360 - curr_deg

        self.last_deg = curr_deg
        return curr_deg

    def update_label(self, obj):
        obj.set_value(self.get_curr_deg())

    def update_i_hat(self, obj):
        circle = self.get_circle()
        obj.put_start_and_end_on(
            circle.get_center(), circle.point_at_angle(radians(self.get_curr_deg())))

    def update_cos(self, obj):
        circle = self.get_circle()

        start = circle.get_center()

        deg = self.get_curr_deg()

        angle = cos(radians(deg))
        end = array(
            [circle.get_x() + angle, circle.get_y(), 0])

        if linalg.norm(start - end) == 0:
            pass
        else:
            obj.put_start_and_end_on(start, end)

    def update_sin(self, obj):
        circle = self.get_circle()

        start = self.cos.get_end()
        end = array([self.cos.get_end()[0], circle.get_y() +
                    sin(radians(self.get_curr_deg())), 0])

        if linalg.norm(start - end) == 0:
            pass
        else:
            obj.put_start_and_end_on(start, end)

    def get_circle(self):
        circle = Circle(radius=1)
        circle.set_color(GRAY)
        circle.set_fill(GRAY, 0.5)
        circle.to_corner(RIGHT+DOWN)
        return circle


class UnitCircleSlide(Scene):
    def construct(self):
        circle = Circle(radius=2)
        circle.set_color(GRAY)
        circle.set_fill(GRAY, 0.5)
        self.add(circle)

        cos = Line(start=circle.get_center(), end=array([1.4, 0, 0]))
        sin = Line(start=cos.get_end(), end=array([cos.get_end()[0], 1.4, 0]))

        foo = Line(circle.get_center(), circle.point_at_angle(45 * DEGREES))

        self.add(cos, sin, foo)
