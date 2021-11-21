class House:
    def __init__(self, address, x ,y,width,buildingcolor,roofcolor,chimney):
        self.address = address
        self.x = x
        self.y = y
        self.width = width
        self.buildingcolor = buildingcolor
        self.roofcolor = roofcolor
        self.chimney = chimney
    def draw(self,pen):
        self.drawbase(pen)



    def drawbase(self,pen):
        pen.up()
        pen.setpos(self.x- self.width/2, self.y - self.width/2)
        pen.down()
        pen.fillcolor(self.buildingcolor)
        pen.begin_fill()
        for i in range(4):
            pen.forward(self.width)
            pen.left(90)
        pen.end_fill()

        