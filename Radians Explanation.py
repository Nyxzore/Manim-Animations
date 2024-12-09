from manim import *

class Radians(Scene):
    def construct(self):

        circle = Circle(radius=2, color=WHITE)
        diameter = Line(start=circle.get_edge_center(LEFT), end=circle.get_edge_center(RIGHT))

        self.play(Create(circle))
        self.play(Create(diameter))

        self.play(circle.animate.set_color(RED))

        #transforming the circumference into the letter c
        circum = MathTex(r"c", font_size = 60)

        circle_x = circle.get_center()[0] + circle.radius
        framewidth = config.frame_width/2
        mdpt = (circle_x + framewidth)/2
        y = circle.get_center()[1]
        circum.move_to([mdpt,y,0]).set_color(RED)

        dup_circle = circle.copy()
        self.play(Transform(dup_circle, circum))

        

        #transforming diam to d
        self.play(circle.animate.set_color(WHITE), diameter.animate.set_color(BLUE))
        diam = MathTex(r"\frac{}{d}", font_size = 60)
        diam.next_to(circum, DOWN).set_color(BLUE)
        dup_diam = diameter.copy() 
        self.play(Transform(dup_diam, diam))
        self.wait(1)

        fraction = VGroup(dup_circle, dup_diam)
        pi = MathTex(r"= \pi").next_to(fraction, RIGHT)
        self.play(Write(pi), diameter.animate.set_color(WHITE))

        #rearrangeing the equation
        equation = VGroup(fraction, pi)

        new_eq = MathTex(r"\frac{c}{2r} = \pi").move_to(equation)
        self.play(Transform(equation, new_eq))
        self.wait(2)

        new_eq = MathTex(r"c = 2 \pi r").move_to(equation)
        self.play(Transform(equation, new_eq))
        self.play(equation.animate.move_to(circle.get_edge_center(UP)).shift(UP))
        self.wait(1)

        #defining a radian
        radius = Line(start=circle.get_center(), end=circle.get_edge_center(RIGHT))
        raidus_label = MathTex(r"r").next_to(radius, DOWN)
        self.play(Transform(diameter, radius), Write(raidus_label))

        #move a copy of the radius onto the circumference
        self.play(radius.animate.set_color(BLUE))
        arc = Arc(angle=1, radius=2, color=BLUE)
        arcRadius = radius.copy()
        arc_label = MathTex(r"r").next_to(arc, RIGHT)
        
        self.play(Transform(arcRadius, arc), Write(arc_label))
        self.wait(2)

        other_radius = Line(start=circle.get_center(), end=arc.get_end()).set_color(BLUE)
        other_radius_label = arc_label = MathTex(r"r").next_to(other_radius, LEFT*0.05)
        self.play(Create(other_radius), Write(other_radius_label))

        #creating the angle
        angle = Arc(angle=1, radius=0.6)
        angle_label = MathTex(r"\theta").next_to(angle, RIGHT).shift(UP*0.2)
        self.play(Create(angle), Write(angle_label))

        #theta = 1 rad
        definition = MathTex(r"\theta=1^c = 1 \hspace{0.1cm} \text{rad}").align_on_border(DOWN)
        self.play(Write(definition))

        #1 revolution
        arrow = Arrow(start = equation[0][-1].get_center() + DOWN, end = equation[0][-1].get_center())
        self.play(Create(arrow))
        self.wait(2)
        self.play(arrow.animate.move_to(equation[0][0].get_center() + DOWN/2))
        
        new_arrow = Arrow(start=equation[0][-1].get_right(), end=equation[0][-1].get_right() + RIGHT)
        self.play(Transform(arrow, new_arrow))
        second_eq = MathTex(r"R = \frac{c}{r}").next_to(arrow, RIGHT).shift(RIGHT*0.2)
        self.play(Write(second_eq))
        self.play(second_eq[0][-1].animate.set_color(BLUE))
        self.play(second_eq[0][2].animate.set_color(RED))

        #visual
        radii = VGroup()
        for i in range(2,7):
            if i%2 == 0:
                color = RED
            else:
                color = BLUE

            next_radius = Arc(angle=1, radius=2, start_angle=i - 1).set_color(color)
            self.play(Create(next_radius))
            radii = VGroup(radii, next_radius)
        
        #approx
        approx = MathTex(r"\approx 6 = 6<R<7 = ", font_size = 35).next_to(circle, RIGHT)
        self.play(Write(approx))

        #rearrange equation
        self.play(FadeOut(radii))

        self.play(Transform(second_eq, MathTex(r"R = \frac{2\pi r}{r}").move_to(second_eq)))
        self.wait(1)
        self.play(Transform(second_eq , MathTex(r"R = 2 \pi").move_to(second_eq)))
        self.play(second_eq.copy()[0][3:].animate.next_to(approx[0][-1], RIGHT * 0.1))

class Perimeter(Scene):
    def construct(self):
        square = Square(side_length = 5)
        self.play(Create(square), run_time = 2)

        #side length
        side = Line(start=square.get_corner(DR), end=square.get_corner(UR)).set_color(RED)
        side_label = MathTex(r"s").next_to(side, RIGHT)
        self.play(Create(side), Write(side_label))

        top_Side = Line(start=square.get_corner(UR), end=square.get_corner(UL)).set_color(RED)
        left_Side = Line(start=square.get_corner(UL), end=square.get_corner(DL)).set_color(RED)
        bot_Side = Line(start=square.get_corner(DL), end=square.get_corner(DR)).set_color(RED)

        self.play(Create(top_Side, run_time = 1))
        self.play(Create(left_Side, run_time = 1))
        self.play(Create(bot_Side, run_time = 1))

        conclusion = MathTex(r"P = 4s").align_on_border(UP)
        self.play(Write(conclusion))
        self.wait(3)

class Review(Scene):
    def construct(self):
        Rev = Tex("Review")
        self.play(Write(Rev))
        self.play(FadeOut(Rev))

        #rad
        circle = Circle(radius=2, color=WHITE)
        self.play(Create(circle))

        radius = Line(start=circle.get_center(), end=circle.get_edge_center(RIGHT))
        raidus_label = MathTex(r"r").next_to(radius, DOWN)
        self.play(Create(radius), Write(raidus_label))

        #move a copy of the radius onto the circumference
        self.play(radius.animate.set_color(BLUE))
        arc = Arc(angle=1, radius=2, color=BLUE)
        arcRadius = radius.copy()
        arc_label = MathTex(r"r").next_to(arc, RIGHT)
        
        self.play(Transform(arcRadius, arc), Write(arc_label))
        self.wait(2)

        other_radius = Line(start=circle.get_center(), end=arc.get_end()).set_color(BLUE)
        other_radius_label = arc_label = MathTex(r"r").next_to(other_radius, LEFT*0.05)
        self.play(Create(other_radius), Write(other_radius_label))

        #creating the angle
        angle = Arc(angle=1, radius=0.6)
        angle_label = MathTex(r"\theta").next_to(angle, RIGHT).shift(UP*0.2)
        self.play(Create(angle), Write(angle_label))

        # 1 rad
        defintion = MathTex(r"\theta = 1^c = 1 \hspace{0.1cm} \text{rad}").next_to(circle,DOWN)
        self.play(Write(defintion))


        #circum
        circum = MathTex(r"c= 2\pi r \therefore R = 2\pi \hspace{0.1cm} \text{rad}").next_to(circle, UP)
        self.play(Write(circum))
        #revolution
