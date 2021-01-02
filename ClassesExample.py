# Ejemplo de como definir clases

class Point:

    # constructor de clase
    def __init__(self,x1, x2, y1, y2):
        self.X1 = x1
        self.X2 = x2
        self.Y1 = y1
        self.Y2 = y2

    def move(self):
        print("move")

    def draw(self):
        print(f"X coordinates (x1:{self.X1},x2:{self.X2})")
        print(f"Y coordinates (y1:{self.Y1},y2:{self.Y2})")
        return self


square = Point(0, 10, 0 ,10)
# los atributos se pueden definir asignadolos automaticamente
square.X1 = 0
square.X2 = 10
square.Y1 = 0
square.Y2 = 10
square.draw()
