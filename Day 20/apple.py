from turtle import Turtle

class Apple(Turtle):
    def __init__(self,pos,*args, **kwargs):
        super(Apple,self).__init__(shape="circle",*args, **kwargs)
        # self.shape("classic")
        self.color("blue")
        self.setpos(pos)
