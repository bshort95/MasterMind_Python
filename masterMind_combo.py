class Combo:
    def __init__(self,color1,color2,color3,color4):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4
        
    def display(self):
        print(self.color1 + " " + self.color2 + " " + self.color3 + " " + self.color4)
    
    def show_colors(self):
        color_list = [self.color1, self.color2, self.color3, self.color4]
        return color_list



