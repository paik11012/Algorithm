class Point:
    
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    
    def __str__(self):
        print(f'Point: ({self.x},{self.y})')
        
p1 = Point(3, 5)


class Circle(Point):


    def __init__(center, r):
        self.center