import math
class GeogeometricObject:
    def __init__(self,c,f):
        self.color=c
        self.filled=f
    def getArea(self):
        pass
    def getPerimeter(self):
        pass

class Triangle(GeogeometricObject):
    def __init__(self,c,f,s1=1,s2=1,s3=1):
        GeogeometricObject.__init__(self, c, f)
        self.side1=s1
        self.side2=s2
        self.side3=s3
    def getPerimeter(self):
        return self.side1+self.side2+self.side3
    def getArea(self):
        s=self.getPerimeter()/2
        a=math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
        return a
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def __str__(self):
        t="Side 1 : "+str(self.side1)+"\n"+"Side 2 : "+str(self.side2)+"\n"+"Side 3 : "+str(self.side3)+"\n"+"Area : "+str(self.getArea())+"\nPerimeter : "+str(self.getPerimeter())+"\nColor : "+self.color+"\nFilled : "+self.filled
        return t

s1,s2,s3=input("Enter 3 sides").split()
c=input("Enter color")
f=input("Enter filled")
t1=Triangle(c,f,int(s1),int(s2),int(s3))
print(t1)

        