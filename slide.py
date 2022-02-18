from lib2to3.pgen2.token import RIGHTSHIFT
from manim import *


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
