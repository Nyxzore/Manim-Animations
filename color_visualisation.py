from manim import *

class Colors(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        Axes = ThreeDAxes(
            x_range=[0,255,50],
            y_range=[0,255,50],
            z_range=[0,255,50],
            )
        labels = Axes.get_axis_labels(
            MathTex("x"), MathTex("y"), MathTex("z")
            )
        self.add(Axes, labels)

        vec = Vector((50,65,34))
        self.add(vec)

        self.begin_ambient_camera_rotation(rate=0.5, about="theta")
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
