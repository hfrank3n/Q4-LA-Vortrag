from manim import *
from numpy import *


class OrthogonalProjectionQuestion(Scene):
    def construct(self):
        matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        colors = [
            ["#77b05d", "#55c1a7"], ["#55c1a7", "#29abca"], ["#29ABCA", "#49A88F"],
            ["#A6CF8C", "#FFEA94"], ["#F9B775", "#B189C6"], ["#1C758A", "#94424F"],
            ["#F4D345", "#FFF1B6"], ["#e1a158", "#FF8080"], ["#A24D61", "#CF5044"]
        ]
        for k in range(len(colors)):
            matrix.get_entries()[k].set_color(colors[k])
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

        v1 = Vector([1, 0, 0], color=GREEN, tip_length=0.25)
        v2 = Vector([0, 1, 0], color=BLUE, tip_length=0.25)
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
        # self.move_camera(phi=0, theta=-90 * DEGREES, run_time=3)
        self.play(house.animate.apply_matrix(matrix), run_time=3)
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=3)
        self.wait(2)


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
        self.camera.set_focal_distance(40)

        matrix_label = Matrix(matrix)
        matrix_label_T = MathTex("T=")
        matrix_label_T.next_to(matrix_label, LEFT)

        label = VGroup(matrix_label, matrix_label_T)
        label.add_background_rectangle(BLACK, 0.5)
        label.scale(0.8)
        self.add_fixed_in_frame_mobjects(label)
        label.to_corner(UR, buff=1)

        house = Cube(side_length=1.5)
        house.shift([0.75, 0.75, 2])

        self.add(axes, house)
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        self.wait(2)

        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=3)

        self.begin_ambient_camera_rotation(rate=PI/8)
        self.wait(16)
        self.stop_ambient_camera_rotation()


class WeakPerspectiveProjection(ThreeDScene):
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

        house = Cube(side_length=1.5)
        house.shift([0.75, 0.75, 2])

        self.add(axes, house)
        self.set_camera_orientation(
            phi=60 * DEGREES, theta=30 * DEGREES, run_time=3)

        points = [[0, 0, 1.5], [1.5, 0, 1.5], [1.5, 1.5, 1.5], [
            0, 1.5, 1.5], [0, 0, 3], [1.5, 0, 3], [1.5, 1.5, 3], [0, 1.5, 3]]
        new_points = []
        for point in points:
            new_point = np.array(point) * (1/point[2])
            new_points.append(new_point)
        print(new_points)
        square1 = Square().set_points_as_corners(new_points[:5])
        square1.add_background_rectangle(BLUE, opacity=0.5)

        line = Line(start=new_points[2], end=new_points[6])

        square2 = Square().set_points_as_corners(new_points[5:])
        square2.add_background_rectangle(DARK_BLUE, opacity=0.8)
        squares = VGroup(square1, square2)

        self.move_camera(phi=0, theta=-90 * DEGREES,
                         added_anims=[ReplacementTransform(house, squares), GrowFromEdge(line, DL)], run_time=3)

        self.wait(2)


class PerspectiveProjection(ThreeDScene):
    foo = Vector()

    def construct(self):
        matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
        # cam_deg = DecimalNumber()
        # cam_deg.add_updater(self.updateNumber)
        # self.add(cam_deg)

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

        cam_deg = self.camera.get_theta()

        x_rotation = [
            [1, 0, 0],
            [0, cos(cam_deg), sin(cam_deg)],
            [0, -sin(cam_deg), cos(cam_deg)]
        ]
        y_rotation = [
            [cos(cam_deg), 0, -sin(cam_deg)],
            [0, 1, 0],
            [sin(cam_deg), 0, cos(cam_deg)]
        ]
        z_rotation = [
            [cos(cam_deg), sin(cam_deg), 0],
            [-sin(cam_deg), cos(cam_deg), 0],
            [0, 0, 1]
        ]

        rotation_complete = matmul(x_rotation, matmul(y_rotation, z_rotation))
        x = 2.5 * np.sin(self.camera.get_phi()) * \
            np.cos(self.camera.get_theta())
        y = 2.5 * np.sin(self.camera.get_phi()) * \
            np.sin(self.camera.get_theta())
        z = 2.5 * np.cos(self.camera.get_phi())
        c = [x, y, z]
        # print(d)
        e = [3, 3, 3.5]
        new_points = []

        self.add(axes, house)
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        self.wait(2)

        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=3)

        points = [[0, 0, 1.5], [1.5, 0, 1.5], [1.5, 1.5, 1.5], [
            0, 1.5, 1.5], [0, 0, 3], [1.5, 0, 3], [1.5, 1.5, 3], [0, 1.5, 3]]
        for a in points:
            d = matmul(self.camera.get_rotation_matrix(),
                       np.array(a)-np.array(c))
            vf = matmul(
                np.array([[1, 0, e[0]/e[2]], [0, 1, e[1]/e[2]], [0, 0, 1/e[2]]]), d)
            b = [vf[0]/vf[2], vf[1]/vf[2], 0]
            new_points.append(b)
            print(b)

        square1 = Square().set_points_as_corners(new_points[:5])
        square1.add_background_rectangle(BLUE, opacity=0.5)

        # line = Line(start=new_points[2], end=new_points[6])

        square2 = Square().set_points_as_corners(new_points[5:])
        square2.add_background_rectangle(DARK_BLUE, opacity=0.8)
        squares = VGroup(square1, square2)

        self.add(squares)

        # self.set_camera_orientation(phi=0, theta=-90, zoom=1)
        # self.wait(4)

        self.begin_ambient_camera_rotation(rate=PI/8)
        self.wait()
        self.stop_ambient_camera_rotation()
        self.wait(2)

    # def updateNumber(self, obj):
    #     obj.set_value(self.camera.get_theta() / DEGREES)
    #     x_rotation = [
    #         [1, 0, 0],
    #         [0, cos(obj.get_value() * DEGREES), -
    #          sin(obj.get_value() * DEGREES)],
    #         [0, sin(obj.get_value() * DEGREES),
    #          cos(obj.get_value() * DEGREES)]
    #     ]
    #     y_rotation = [
    #         [cos(obj.get_value() * DEGREES), 0,
    #          sin(obj.get_value() * DEGREES)],
    #         [0, 1, 0],
    #         [-sin(obj.get_value() * DEGREES), 0,
    #          cos(obj.get_value() * DEGREES)]
    #     ]
    #     z_rotation = [
    #         [cos(obj.get_value() * DEGREES), -
    #          sin(obj.get_value() * DEGREES), 0],
    #         [sin(obj.get_value() * DEGREES),
    #          cos(obj.get_value() * DEGREES), 0],
    #         [0, 0, 1]
    #     ]

    #     rotation_complete = matmul(x_rotation, matmul(y_rotation, z_rotation))
    #     a = [1, 2, 1]
    #     x = self.camera.get_focal_distance() * np.sin(self.camera.get_phi()) * \
    #         np.cos(self.camera.get_theta())
    #     y = self.camera.get_focal_distance() * np.sin(self.camera.get_phi()) * \
    #         np.sin(self.camera.get_theta())
    #     z = self.camera.get_focal_distance() * np.cos(self.camera.get_phi())
    #     c = [x, y, z]
    #     d = matmul(rotation_complete, np.array(a)-np.array(c))
    #     # print(d)
    #     vf = matmul(np.array([[1, 0, 1], [0, 1, 1], [0, 0, 1]]), d)
    #     b = [vf[0]/vf[2], vf[1]/vf[2], 0]
    #     self.remove(self.foo)
    #     self.foo = Vector(b)
    #     self.add(self.foo)
