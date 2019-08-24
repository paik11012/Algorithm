# 파일명을 변경하지 마시오.
# 아래에 클래스 Point와 Circle을 선언하시오.

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point: ({self.x},{self.y})'


class Circle(Point):
    

    def __init__(self,center,r):
        self.center = center
        self.r = r
        self.x = center.x  # 이부분 중요함 받아와야 함
        self.y = center.y

    def get_area(self):
        area = self.r * self.r * 3.14
        return area

    def get_perimeter(self):
        peri = 2 * self.r * 3.14
        return peri

    def get_center(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        return f'Circle: ({self.x},{self.y},r:{self.r})'







# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    p1 = Point(0, 0)
    c1 = Circle(p1, 3)
    print(c1.get_area())
    print(c1.get_perimeter())
    print(c1.get_center())
    print(c1)
    p2 = Point(4, 5)
    c2 = Circle(p2, 1)
    print(c2.get_area())
    print(c2.get_perimeter())
    print(c2.get_center())
    print(c2)