pi=3.14159
radius=int(input())
height=int(input())
base_area=pi*radius**2
volume=round(base_area*height,4)
surface_area=round(2*base_area+2*pi*radius*height,4)
print("volume is",volume,"surface area is",surface_area)
print(volume)
print(surface_area)

