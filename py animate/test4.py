from manim import * 

class PointMovingOnShapes(Scene):
    def construct(self):
        square = Square(color=BLUE) # Cоздаем квадрат заданного цвета
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8) # Поворачиваем квадрат на -3/8 * 2*PI 

        # Проигрываем анимацию
        self.play(GrowFromCenter(square))