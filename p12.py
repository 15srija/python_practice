import math
height=int(input("Enter the height of the wall:"))
width=int(input("Enter the width of the wall:"))
coverage=7
def paint_calculation(h,w,cover):
    area=h*w
    no_of_cans=math.ceil(area/cover)
    print(f"You will need {no_of_cans} of cans to paint the wall")
paint_calculation(h=height,w=width,cover=coverage)