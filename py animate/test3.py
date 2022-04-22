from turtle import circle
from manim import * 

class PointMovingOnShapes(Scene):
    def construct(self):
        square = Square(color=BLUE) # Create a square
        square.flip(RIGHT) # Flip the square to the right
        square.rotate(-3 * TAU / 8) # Rotate the square -3/8 * 2*PI 

        # circle = circle(color=PINK ) # Create a circle
        # circle.flip(RIGHT) # Flip the circle to the right
        # circle.rotate(-3 * TAU / 8) # Rotate the circle -3/8 * 2*PI 

         # Play the animation of a square growing from the center
        self.play(GrowFromCenter(square))