import math

class Point:
    x,y=0,0
    def __init__(self,a,b):
        self.x= a
        self.y= b
    def Opposite(self):
        temp= 
        self.x= -self.x
        self.y= -self.y
    def Add(self,P):
        nx= self.x+ P.x
        mx= self.y+ P.y
        return Point(mx,nx)
    def Distance(self,P):
        return math.sqrt((self.x - P.x)**2 + (self.y - P.y)**2)
    def Rotate(self,P,angle):
        angle = angle *math.pi /180
        nx= (self.x - P.x)* math.cos(angle)- (self.y - P.y)* math.sin(angle)
        mx= (self.x - P.x)* math.sin(angle)+ (self.y - P.y)* math.cos(angle)
        mx+= P.x
        nx+= P.y
        return Point(mx,nx)
    def Alligned(self,P,Q):
        a=(self.x - P.x) % (self.x - Q.x) and (self.x - P.x) %(self.x - Q.x)
        return bool(a) 

class Rectangle:
    t= Point(0,0)
    b=Point(0,0)
    def __init__(self,a,c):
        self.t.x= a.x
        self.t.y= a.y
        self.b.x= c.x
        self.b.y= c.y
    def center(self):
        C = self.t.add(self.b)
        return Point(C.x/2,C.y/2)
    
    def opposite(self):
        self.t.opposite()
        self.b.opposite()
    def distance(self,R):
        C = self.t.add(self.b)
        C.x/=2
        C.y/=2
        D = R.t.add(R.b)
        D.x/=2
        D.y/=2
        return C.Distance(D)

    def zoom(self,scale):
        C = self.t.add(self.b)
        C.x/=2
        C.y/=2
        
    
    def rotation(self, p, angle):
        i= Rotate(self.t,P,angle)
        j= Rotate(self.b,P,angle)
        return Rectange(i,j)

    def aligned(self,P,Q):
        A = center(self)
        B = center(P)
        C = center(Q)
        return A.alligned(B,C)

