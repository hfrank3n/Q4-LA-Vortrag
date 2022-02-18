from manim import *
from numpy import *


class Test(Scene):
    def construct(self):
        rotation_matrix_45deg = [
            [cos(radians(45)), -sin(radians(45))], [sin(radians(45)), cos(radians(45))]]

        text1 = MathTex(r"T(\vec{v_1})=\vec{v_2}")
        text1.to_corner(LEFT+UP, buff=2)
        text1.shift(2*RIGHT)

        text2 = MathTex(r"T\cdot\vec{v_1}=\vec{v_2}")
        text2.next_to(text1, buff=4)

        m1 = Matrix([["i_1", "j_1"], ["i_2", "j_2"]])
        m1.next_to(text2, direction=DOWN, buff=2)

        text3 = MathTex(r"T =")
        text3.next_to(m1, direction=LEFT)

        text4 = MathTex(r"\hat{i}")
        text4.next_to(m1, direction=UP, buff=0.7)
        text4.shift(LEFT)

        arrow1 = CurvedArrow(text4.get_right()+0.2*DOWN,
                             m1.get_columns()[0].get_top()+0.3*UP, angle=-PI/4, tip_length=0.2)

        text5 = MathTex(r"\hat{j}")
        text5.next_to(m1, direction=UP, buff=0.5)
        text5.shift(RIGHT)

        arrow2 = CurvedArrow(text5.get_left()+0.2*DOWN,
                             m1.get_columns()[1].get_top()+0.3*UP, angle=PI/4, tip_length=0.2)

        grid1 = Axes(
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
        grid1.to_corner(LEFT+DOWN, buff=1.3)
        v1 = Vector([1, 0], color=ORANGE, tip_length=0.25)
        v2 = Vector([0, 1], color=ORANGE, tip_length=0.25)
        v3 = v1.copy()
        v4 = v2.copy()
        v1.shift(grid1.get_origin())
        v2.shift(grid1.get_origin())

        arrow_text = MathTex(
            r"\overset{T}{\longleftrightarrow}", font_size=100)
        arrow_text.next_to(grid1, buff=0.5, aligned_edge=UP)

        grid2 = grid1.copy()
        grid2.next_to(arrow_text, buff=0.5, aligned_edge=UP)
        v3 = v3.apply_matrix(rotation_matrix_45deg)
        v4 = v4.apply_matrix(rotation_matrix_45deg)
        v3.set_color(BLUE)
        v3.set_tip_length(0.25)
        v4.set_color(BLUE)
        v4.set_tip_length(0.25)
        v3.shift(grid2.get_origin())
        v4.shift(grid2.get_origin())

        self.add(text1, grid1, arrow_text, v1, v2, grid2,
                 v3, v4, text2, m1, text3, text4, text5, arrow1, arrow2)

        # circle = Circle()
        # circle.set_fill(PINK, opacity=0.5)
        # square = Square()
        # self.play(Create(circle))
        # self.play(Transform(circle, square))
        # self.play(Rotate(square, angle=PI), run_time=2)
        # self.play(FadeOut(square))
