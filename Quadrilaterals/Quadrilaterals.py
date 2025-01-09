from manim import *

class Quadrilaterals(Scene):
    def construct(self):
        #intro
        sqaure = Square()
        IntroText = Tex("What is a quadrilateral?", font_size = 60)
        IntroText.align_on_border(UP)
        self.play(Write(IntroText), Create(sqaure))
        self.wait(2)

        #quad has 4 sides/edges and 4 vertices/corners
        property1 = Tex("- 4 sides(edges)", font_size = 40)
        property2 = Tex("- 4 vertices(corners)", font_size = 40)
        property3 = Tex("- Sum of interior angles = 360 \\degrees", font_size = 40)

        property1.next_to(IntroText, DOWN)
        property2.next_to(property1, DOWN)
        property2.next_to(property2, DOWN)

        self.play(Write(property1))
        self.play(sqaure.animate.set_color("RED"))

        self.play(Write(property2))
        vertices = sqaure.get_vertices() # retrives positions of vertices

        corners = VGroup()
        for vertex in vertices:
            corner = Dot(point=vertex, color=BLUE)
            corners = VGroup(corners, corner)

        self.play(Create(corners))

        #property 3
        #draw right angles, sum them 
        self.wait(1)
        #defining various quads
        self.play(FadeOut(sqaure), FadeOut(property1), FadeOut(property2), FadeOut(IntroText), FadeOut(corners))
        Section2 = Tex("Defining quadrilaterals", font_size = 60)
        content = Tex("We will be defining the: \\\\ Rectangle \\\\ Sqaure \\\\ Parallelogram \\\\ Rhombus \\\\ Kite", font_size=40)

        Section2.align_on_border(UP)
        content.next_to(Section2, DOWN)
        self.play(Write(Section2))
        self.wait(1)
        self.play(Write(content))

        #the rectangle
        self.play(FadeOut(content), FadeOut(Section2))
        TheRectangle = Tex("The Rectangle").align_on_border(UP)
        rectangle = Rectangle()

        self.play(Write(TheRectangle), Create(rectangle))

        #property 1 opp sides 
        property1 = Tex("2 pairs of opposite side are = (equal)")
        property2 = Tex("2 pairs of opposite side are // (parrelel)")  
        property3 = Tex("Diagonals bisect eachother") 
        property4 = MathTex(r"every angle = 90 \\degrees") 

        