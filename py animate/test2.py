from manim import * 

config.background_color = DARK_GRAY

class PointMovingOnShapes(Scene):
    def construct(self):
        
        # Create a circle
        circle = Circle()
        circle.flip(RIGHT)
        circle.set_fill(PINK, opacity=0.5) # set the color and transparency

        # Create a square
        square = Square(color=BLUE)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 500)
      
        # Create animations
        self.play(GrowFromCenter(square))
        self.play(Transform(square, circle))  # turn the square into a circle
       
        self.wait() # wait for some seconds