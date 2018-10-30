class Rectangle:
    def __init__(self,width=1,height=2):
        self.w=width
        self.h=height
    def getArea(self):
        return round(self.h*self.w,2)
    def getPerimeter(self):
        return 2*(self.h+self.w)
    def display(self):
        print("Width : ",self.w)
        print("Height : ",self.h)
        print("Area : ",self.getArea())
        print("Perimeter : ",self.getPerimeter())
    
r1=Rectangle(4,40)
r2=Rectangle(3.5,35.7)
r1.display()
r2.display()