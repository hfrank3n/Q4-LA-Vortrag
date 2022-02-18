from manim import *
from numpy import *


class Test(Scene):
    def construct(self):
        rotation_matrix_45deg = [
            [cos(radians(45)), -sin(radians(45))], [sin(radians(45)), cos(radians(45))]]

        function_equation = MathTex(r"T(\vec{v_1})=\vec{v_2}")
        function_equation.to_corner(LEFT+UP, buff=2)
        function_equation.shift(2*RIGHT)

        matrix_equation = MathTex(r"T\cdot\vec{v_1}=\vec{v_2}")
        matrix_equation.next_to(function_equation, buff=4)

        matrix = Matrix([["i_1", "j_1"], ["i_2", "j_2"]])
        matrix.next_to(matrix_equation, direction=DOWN, buff=2)

        matrix_label = MathTex(r"T =")
        matrix_label.next_to(matrix, direction=LEFT)

        i_label = MathTex(r"\hat{i}")
        i_label.next_to(matrix, direction=UP, buff=0.7)
        i_label.shift(LEFT)

        i_arrow = CurvedArrow(i_label.get_right()+0.2*DOWN,
                              matrix.get_columns()[0].get_top()+0.3*UP, angle=-PI/4, tip_length=0.2)

        j_label = MathTex(r"\hat{j}")
        j_label.next_to(matrix, direction=UP, buff=0.5)
        j_label.shift(RIGHT)

        j_arrow = CurvedArrow(j_label.get_left()+0.2*DOWN,
                              matrix.get_columns()[1].get_top()+0.3*UP, angle=PI/4, tip_length=0.2)

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

        v1 = Vector([1, 0], tip_length=0.25)
        v2 = Vector([0, 1], tip_length=0.25)
        vGroup = VGroup(v1, v2)
        left_grid.add(vGroup)
        left_grid[2].set_color(ORANGE)

        transformation_label = MathTex(
            r"\overset{T}{\longleftrightarrow}", font_size=100)

        right_grid = left_grid.copy()
        right_grid[2].set_color(BLUE)
        right_grid[2].apply_matrix(rotation_matrix_45deg)

        left_grid[2].shift(left_grid.get_origin())
        right_grid[2].shift(right_grid.get_origin())

        left_grid.to_corner(LEFT+DOWN, buff=1.3)
        transformation_label.next_to(left_grid, buff=0.5, aligned_edge=UP)
        right_grid.next_to(transformation_label, buff=0.5, aligned_edge=UP)

        self.add(function_equation, transformation_label, left_grid, right_grid, matrix_equation,
                 matrix, matrix_label, i_label, j_label, i_arrow, j_arrow)
