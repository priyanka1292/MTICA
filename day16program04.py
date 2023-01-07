class vector3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,ob):
        return vector3D(self.x+ob.x,self.y+ob.y,self.z+ob.z)
first=vector3D(11,22,33)
second=vector3D(1,2,3)
result=first+second
print(result.x,result.y,result.z)


