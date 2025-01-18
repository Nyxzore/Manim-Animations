from manim import *

class Example(Scene):
    def construct(self):
        self.example_one()
        self.wait(2)
        self.clear_screen()  # Clear the screen before starting the next example
        self.example_two()
        self.wait(2)
        self.clear_screen()
        self.summary()
        self.wait(2)
        self.clear_screen()
    
    def example_one(self):
        title = Tex("Sigma Notation")
        series = MathTex("1+2+3+4+5+6+7+8+9")
        sigma = MathTex("\\Sigma", font_size = 100).align_on_border(DOWN).shift(UP)

        self.play(Write(title), run_time = 1.5)
        self.play(FadeOut(title))

        self.play(Write(series), run_time = 3)
        self.play(Write(sigma))

        #number of terms
        highlight_term = SurroundingRectangle(series[0][0])
        self.play(Create(highlight_term))
        index = MathTex("n=1").next_to(series, UP)
        self.play(Write(index))
        self.wait(1)
        lower_index = index.copy()
        self.play(lower_index.animate.move_to(sigma).shift(DOWN*0.6))

        self.play(highlight_term.animate.move_to(series[0][-1]), ReplacementTransform(index[0][-1], MathTex("9").move_to(index[0][-1])))

        upper_index = index.copy()
        self.play(upper_index.animate.move_to(sigma).shift(UP*0.6))
        self.play(Transform(upper_index, MathTex("9").move_to(sigma).shift(UP*0.6)))
        self.wait(2)

        #representing the formula
        self.play(FadeOut(highlight_term))
        tn = MathTex("T_n").next_to(sigma, RIGHT)
        self.play(Write(tn), FadeOut(index))
        
        formula = MathTex("T_n = a + (n-1)(d)").next_to(series, UP)
        self.play(Write(formula))
        self.play(Indicate(formula[0][-2]) ,Transform(formula[0][-2], MathTex(1).move_to(formula[0][-2])))
        self.play(Indicate(formula[0][3]), Indicate(series[0][0]))
        self.play(Transform(formula[0][3], MathTex(1).move_to(formula[0][3])))

        self.play(Transform(formula, MathTex("T_n = n").next_to(series, UP)))
        self.play(Transform(tn, MathTex("n").next_to(sigma, RIGHT)))

        self.wait(2)


        equals = MathTex("=").next_to(series, RIGHT)
        sigma = VGroup(sigma, upper_index, lower_index, tn)
        self.play(FadeOut(formula))
        self.play(Write(equals), sigma.animate.next_to(equals, RIGHT)) 
    def example_two(self):
        title = Tex("Example 2")
        series = MathTex("5+7+9+11+13+15+17")
        sigma = MathTex("\\Sigma", font_size = 100).align_on_border(DOWN).shift(UP)

        self.play(Write(title), run_time = 1.5)
        self.play(FadeOut(title))

        self.play(Write(series), run_time = 3)
        self.play(Write(sigma))

        #number of terms
        highlight_first = SurroundingRectangle(series[0][0])
        self.play(Create(highlight_first))
        index = MathTex("n=1").next_to(series, UP)
        self.play(Write(index))
        self.wait(1)
        lower_index = index.copy()
        self.play(lower_index.animate.move_to(sigma).shift(DOWN*0.6))

        highlight_last = SurroundingRectangle(VGroup(series[0][-1], series[0][-2]))
        self.play(Transform(highlight_first, highlight_last), Transform(index[0][-1], MathTex("7").move_to(index[0][-1])))

        upper_index = index.copy()
        self.play(upper_index.animate.move_to(sigma).shift(UP*0.6))
        self.play(Transform(upper_index, MathTex("7").move_to(sigma).shift(UP*0.6)))
        self.wait(2)

        #representing the formula
        self.play(FadeOut(highlight_first))
        tn = MathTex("T_n").next_to(sigma, RIGHT)
        self.play(Write(tn), FadeOut(index))
        
        formula = MathTex("T_n = a + (n-1)(d)").next_to(series, UP)
        self.play(Write(formula))
        self.play(Indicate(formula[0][-2]) ,Transform(formula[0][-2], MathTex("2").move_to(formula[0][-2])))
        self.play(Indicate(formula[0][3]), Indicate(series[0][0]))
        self.play(Transform(formula[0][3], MathTex("5").move_to(formula[0][3])))
        self.play(Transform(formula, MathTex("T_n = 2n+3").next_to(series, UP)))
        self.play(Transform(tn, MathTex("2n+3").next_to(sigma, RIGHT)))

        self.wait(2)


        equals = MathTex("=").next_to(series, RIGHT)
        sigma = VGroup(sigma, upper_index, lower_index, tn)
        self.play(FadeOut(formula))
        self.play(Write(equals), sigma.animate.next_to(equals, RIGHT)) 

        self.wait(3)
    def summary(self):
        title = Tex("Summary")
        self.play(Write(title))
        self.play(FadeOut(title))

        # Create the sigma expression
        sigma = MathTex("\\sum_{n=1}^{7}{T_n}", font_size=100)
        self.play(Write(sigma))

        # Positions for arrows
        start_pos = sigma.get_corner(DOWN + LEFT)  # Bottom-left corner
        end_pos = sigma.get_corner(UP + LEFT)     # Top-left corner
        tn_pos = sigma.get_corner(RIGHT)          # Middle-right corner

        # Arrows and text
        start_arrow = Arrow(start=start_pos + LEFT, end=start_pos, color=BLUE)
        start_tex = Tex("Starting index of n").next_to(start_arrow, LEFT)

        end_arrow = Arrow(start=end_pos + LEFT, end=end_pos, color=GREEN)
        end_tex = Tex("Final index of n").next_to(end_arrow, LEFT)

        tn_arrow = Arrow(start=tn_pos + RIGHT, end=tn_pos, color=RED)
        tn_tex = Tex("General formula").next_to(tn_arrow, RIGHT)

        # Groups for better alignment
        start = VGroup(start_arrow, start_tex)
        end = VGroup(end_arrow, end_tex)
        tn = VGroup(tn_arrow, tn_tex)

        # Animate arrows and text
        self.play(Create(start), Create(end), Create(tn))
        self.wait()

    def clear_screen(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])