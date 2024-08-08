class Rectangle:
    def __init__(self,width,height):
        self.classname='Rectangle'
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return (self.width**2+self.height**2)**.5
    def get_picture(self):
        pic=''
        if self.width >50 or self.height>50:
            return 'Too big for picture.'
        for i in range(self.height):
            pic+='*'*self.width+'\n'
            
        
        return pic
    def get_amount_inside(self,other):
        num_height=self.height//other.height
        num_width=self.width//other.width
        return num_height*num_width
    def __str__(self):
        string=''
        string+=self.classname
        string+=f'(width={self.width}, height={self.height})'
        return string


        
    

class Square(Rectangle):
    def __init__(self,side):
        self.width=side
        self.height=side
    def set_width(self,width):
        self.height=self.width=width
    def set_height(self,height):
        self.height=self.width=height
    def set_side(self,side):
        self.height=self.width=side
    def __str__(self):
        return f'Square(side={self.height})'
rect=Rectangle(10,5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
sq=Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))