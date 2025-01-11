from manim import *
class Quadrilaterals(Scene):
    def construct(self):
        #intro

        title_font_size = 50
        body_font_size = 40
        sqaure = Square().shift(DOWN)
        IntroText = Tex("What is a quadrilateral?", font_size = title_font_size)
        IntroText.align_on_border(UP)
        self.play(Write(IntroText), Create(sqaure))
        self.wait(2)

        #quad has 4 sides/edges and 4 vertices/corners
        property1 = Tex("- 4 sides(edges)", font_size = body_font_size)
        property2 = Tex("- 4 vertices(corners)", font_size = body_font_size)
        property3 = Tex("- Sum of interior angles = 360 degrees", font_size = body_font_size)

        property1.next_to(IntroText, DOWN)
        property2.next_to(property1, DOWN)
        property3.next_to(property2, DOWN)

        self.play(Write(property1))
        self.play(sqaure.animate.set_color("GREEN"))

        self.play(Write(property2))
        vertices = sqaure.get_vertices() # retrives positions of vertices

        corners = VGroup()
        for vertex in vertices:
            corner = Dot(point=vertex, color=BLUE)
            corners.add(corner)

        self.play(Create(corners))
        #property 3
        self.play(Write(property3))
        #draw right angles, sum them 
        right_angles = VGroup()
        for i, vertex in enumerate(vertices):
            edge1 = Line(vertex, vertices[i-1])
            edge2 = Line(vertex, vertices[(i+1) % 4])

            right_angle = RightAngle(edge1, edge2, color=BLUE)
            right_angles.add(right_angle)

        self.play(Create(right_angles))
        self.wait(1)
        #defining various quads
        self.play(FadeOut(sqaure), FadeOut(property1), FadeOut(property2), FadeOut(property3), FadeOut(IntroText), FadeOut(corners), FadeOut(right_angles))
        Section2 = Tex("Defining quadrilaterals", font_size = title_font_size)
        content = Tex("We will be defining the: \\\\ Rectangle \\\\ Sqaure \\\\ Parallelogram \\\\ Rhombus \\\\ Kite", font_size=40)

        Section2.align_on_border(UP)
        content.next_to(Section2, DOWN)
        self.play(Write(Section2))
        self.wait(1)
        self.play(Write(content), run_time = 5)

        #the rectangle
        self.play(FadeOut(content), FadeOut(Section2))
        TheRectangle = Tex("The Rectangle", font_size = title_font_size).align_on_border(UP)
        rectangle = Rectangle().shift(DOWN)

        self.play(Write(TheRectangle), Create(rectangle))

        #properteis of rectangle
        property1 = Tex("-2 pairs of opposite side are = (equal)", font_size = body_font_size).next_to(TheRectangle, DOWN)
        property2 = Tex("-2 pairs of opposite side are // (parrelel)", font_size = body_font_size).next_to(property1, DOWN)  
        property3 = Tex("-Every angle = 90 degrees", font_size = body_font_size).next_to(property2, DOWN)
        #property4 = Tex("-Diagonals bisect eachother", font_size = body_font_size).next_to(property3, DOWN) 

        self.play(Write(property1)) 
        left_edge = Line(rectangle.get_corner(UL), rectangle.get_corner(DL), color=BLUE)
        right_edge = Line(rectangle.get_corner(UR), rectangle.get_corner(DR), color=BLUE)
        one_tick_equal_left = Line(left_edge.get_center() - 0.1*LEFT, left_edge.get_center() - 0.1*RIGHT)
        one_tick_equal_right = Line(right_edge.get_center() - 0.1*LEFT, right_edge.get_center() - 0.1*RIGHT)

        bot_edge = Line(rectangle.get_corner(UL), rectangle.get_corner(UR), color=GREEN)
        top_edge = Line(rectangle.get_corner(DL), rectangle.get_corner(DR), color=GREEN)
        one_tick_equal_top = Line(top_edge.get_center() - 0.1*DOWN, top_edge.get_center() - 0.1*UP)
        one_tick_equal_bot = Line(bot_edge.get_center() - 0.1*DOWN, bot_edge.get_center() - 0.1*UP)
        two_tick_top = VGroup(one_tick_equal_top, one_tick_equal_top.copy().shift(LEFT*0.1))
        two_tick_bot = VGroup(one_tick_equal_bot, one_tick_equal_bot.copy().shift(LEFT*0.1))

        self.play(Create(left_edge), Create(right_edge))
        self.play(Create(one_tick_equal_left), Create(one_tick_equal_right))
        self.wait(0.5)
        self.play(FadeOut(left_edge, right_edge))
        self.play(Create(bot_edge), Create(top_edge))
        self.play(Create(two_tick_top), Create(two_tick_bot))
        self.wait(0.5)
        self.play(FadeOut(top_edge, bot_edge))
      
        self.play(Write(property2))
        left_parralel = MathTex(">", font_size = 30).rotate(PI/2).move_to(left_edge.get_center() + DOWN*0.2)
        right_parralel = MathTex(">", font_size = 30).rotate(PI/2).move_to(right_edge.get_center() + DOWN*0.2)
        self.play(Create(left_edge), Create(right_edge))
        self.play(Create(left_parralel), Create(right_parralel))
        self.wait(0.5)
        self.play(FadeOut(left_edge), FadeOut(right_edge))

        top_parralel = MathTex(">>", font_size = 30).move_to(top_edge.get_center() + LEFT*0.5)
        bot_parralel = MathTex(">>", font_size = 30).move_to(bot_edge.get_center() + LEFT*0.5)
        self.play(Create(top_edge), Create(bot_edge))
        self.play(Create(top_parralel), Create(bot_parralel))
        self.wait(0.5)
        self.play(FadeOut(top_edge), FadeOut(bot_edge))

        self.play(Write(property3))
        vertices = rectangle.get_vertices()
        right_angles = VGroup()
        for i, vertex in enumerate(vertices):
            edge1 = Line(vertex, vertices[i-1])
            edge2 = Line(vertex, vertices[(i+1) % 4])

            right_angle = RightAngle(edge1, edge2, color=GREEN)
            right_angles.add(right_angle)
        self.play(Create(right_angles))
        self.wait(2)
        #-------------------------------------------------------------------------
        #THE SQAURE
        self.play(FadeOut(rectangle), FadeOut(right_angles), FadeOut(two_tick_bot), FadeOut(two_tick_top),
                  FadeOut(one_tick_equal_left), FadeOut(one_tick_equal_right), FadeOut(bot_parralel), FadeOut(top_parralel),
                  FadeOut(left_parralel), FadeOut(right_parralel), FadeOut(TheRectangle),
                  FadeOut(property1, property2, property3))
        TheSqaure = Tex("The Sqaure", font_size = title_font_size).align_on_border(UP)
        sqaure = Square().shift(DOWN)

        self.play(Write(TheSqaure), Create(sqaure))

        #properteis of rectangle
        property1 = Tex("-all 4 sides are = (equal)", font_size = body_font_size).next_to(TheRectangle, DOWN)
        property2 = Tex("-2 pairs of opposite side are // (parrelel)", font_size = body_font_size).next_to(property1, DOWN)  
        property3 = Tex("-Every angle = 90 degrees", font_size = body_font_size).next_to(property2, DOWN)
        #property4 = Tex("-Diagonals bisect eachother", font_size = body_font_size).next_to(property3, DOWN) 

        self.play(Write(property1)) 
        left_edge = Line(sqaure.get_corner(UL), sqaure.get_corner(DL), color=GREEN)
        right_edge = Line(sqaure.get_corner(UR), sqaure.get_corner(DR), color=GREEN)
        one_tick_equal_left = Line(left_edge.get_center() - 0.1*LEFT, left_edge.get_center() - 0.1*RIGHT)
        one_tick_equal_right = Line(right_edge.get_center() - 0.1*LEFT, right_edge.get_center() - 0.1*RIGHT)

        bot_edge = Line(sqaure.get_corner(UL), sqaure.get_corner(UR), color=GREEN)
        top_edge = Line(sqaure.get_corner(DL), sqaure.get_corner(DR), color=GREEN)
        one_tick_equal_top = Line(top_edge.get_center() - 0.1*DOWN, top_edge.get_center() - 0.1*UP)
        one_tick_equal_bot = Line(bot_edge.get_center() - 0.1*DOWN, bot_edge.get_center() - 0.1*UP)

        self.play(Create(left_edge), Create(right_edge), Create(top_edge), Create(bot_edge))
        self.play(Create(one_tick_equal_left), Create(one_tick_equal_right), Create(one_tick_equal_top), Create(one_tick_equal_bot))
        self.wait(1)
        self.play(FadeOut(top_edge, bot_edge, left_edge, right_edge))
      
        self.play(Write(property2))
        left_parralel = MathTex(">", font_size = 30).rotate(PI/2).move_to(left_edge.get_center() + DOWN*0.2)
        right_parralel = MathTex(">", font_size = 30).rotate(PI/2).move_to(right_edge.get_center() + DOWN*0.2)
        self.play(Create(left_edge), Create(right_edge))
        self.play(Create(right_parralel), Create(left_parralel))
        self.wait(0.5)
        self.play(FadeOut(left_edge), FadeOut(right_edge))

        top_parralel = MathTex(">>", font_size = 30).move_to(top_edge.get_center() + LEFT*0.5)
        bot_parralel = MathTex(">>", font_size = 30).move_to(bot_edge.get_center() + LEFT*0.5)
        self.play(Create(top_edge) ,Create(bot_edge))
        self.play(Create(top_parralel), Create(bot_parralel))
        self.wait(0.5)
        self.play(FadeOut(top_edge), FadeOut(bot_edge))

        self.play(Write(property3))
        vertices = sqaure.get_vertices()
        right_angles = VGroup()
        for i, vertex in enumerate(vertices):
            edge1 = Line(vertex, vertices[i-1])
            edge2 = Line(vertex, vertices[(i+1) % 4])

            right_angle = RightAngle(edge1, edge2, color=GREEN)
            right_angles.add(right_angle)
        self.play(Create(right_angles))

        self.wait(2)

        #-------------------------------------------------------------------------
        #THE Parrelagram
        self.play(FadeOut(sqaure), FadeOut(right_angles), FadeOut(one_tick_equal_top), FadeOut(one_tick_equal_bot),
                  FadeOut(one_tick_equal_left), FadeOut(one_tick_equal_right), FadeOut(bot_parralel), FadeOut(top_parralel),
                  FadeOut(left_parralel), FadeOut(right_parralel), FadeOut(TheSqaure),
                  FadeOut(property1, property2, property3))
        TheParallelogram = Tex("The Parallelogram", font_size = title_font_size).align_on_border(UP)
        points = [
            LEFT*2 + DOWN,  # Point A (bottom left)
            RIGHT + DOWN,  # Point B (bottom right)
            RIGHT*2 + UP,  # Point C (top right)
            LEFT + UP  # Point D (top left)
        ]
        parallelogram = Polygon(*points, color=WHITE).shift(DOWN)

        self.play(Write(TheParallelogram), Create(parallelogram))

        #properteis of rectangle
        property1 = Tex("-2 pairs of opposite side are = (equal)", font_size = body_font_size).next_to(TheRectangle, DOWN)
        property2 = Tex("-2 pairs of opposite side are // (parrelel)", font_size = body_font_size).next_to(property1, DOWN)  
        property3 = Tex("-2 pairs of opposite angles are = (equal)", font_size = body_font_size).next_to(property2, DOWN)

        left_edge = Line(points[0], points[3], color=GREEN).shift(DOWN)
        right_edge = Line(points[1], points[2], color=GREEN).shift(DOWN)
        bot_edge = Line(points[0], points[1], color=BLUE).shift(DOWN)
        top_edge = Line(points[2], points[3], color=BLUE).shift(DOWN)

        self.play(Write(property1)) 
        one_tick_equal_left = Line(left_edge.get_center() - 0.1*LEFT, left_edge.get_center() - 0.1*RIGHT)
        one_tick_equal_right = Line(right_edge.get_center() - 0.1*LEFT, right_edge.get_center() - 0.1*RIGHT)

        one_tick_equal_top = Line(top_edge.get_center() - 0.1*DOWN, top_edge.get_center() - 0.1*UP)
        one_tick_equal_bot = Line(bot_edge.get_center() - 0.1*DOWN, bot_edge.get_center() - 0.1*UP)
        two_tick_top = VGroup(one_tick_equal_top, one_tick_equal_top.copy().shift(LEFT*0.1))
        two_tick_bot = VGroup(one_tick_equal_bot, one_tick_equal_bot.copy().shift(LEFT*0.1))

        self.play(Create(left_edge), Create(right_edge))
        self.play(Create(one_tick_equal_left), Create(one_tick_equal_right))
        self.wait(0.5)
        self.play(FadeOut(left_edge, right_edge))
        self.play(Create(bot_edge), Create(top_edge))
        self.play(Create(two_tick_top), Create(two_tick_bot))
        self.wait(0.5)
        self.play(FadeOut(top_edge, bot_edge))
      
        self.play(Write(property2))
        left_parralel = MathTex(">", font_size = 30).rotate(PI/2).move_to(left_edge.get_center() + DOWN*0.2)
        right_parralel = MathTex(">", font_size = 30).rotate(PI/2).move_to(right_edge.get_center() + DOWN*0.2)
        self.play(Create(left_edge), Create(right_edge))
        self.play(Create(right_parralel), Create(left_parralel))
        self.wait(0.5)
        self.play(FadeOut(left_edge), FadeOut(right_edge))

        top_parralel = MathTex(">>", font_size = 30).move_to(top_edge.get_center() + LEFT*0.5)
        bot_parralel = MathTex(">>", font_size = 30).move_to(bot_edge.get_center() + LEFT*0.5)
        self.play(Create(top_edge) ,Create(bot_edge))
        self.play(Create(top_parralel), Create(bot_parralel))
        self.wait(0.5)
        self.play(FadeOut(top_edge), FadeOut(bot_edge))

        self.play(Write(property3))
        #opp angles = 
        ul_angle = Angle(top_edge, left_edge, radius=0.5)
        dr_angle = Angle(bot_edge, right_edge, radius=0.5)

        ur_angle = Angle(top_edge, right_edge, radius=0.5)
        dl_angle = Angle(bot_edge, left_edge, radius=0.5)

        ur_angle = VGroup(ur_angle, ur_angle.copy().shift(LEFT*0.05))
        dl_angle = VGroup(dl_angle, dl_angle.copy().shift(RIGHT*0.05))

        self.play(Create(ul_angle), Create(dr_angle))
        self.play(Create(ur_angle), Create(dl_angle))
        self.wait(2)