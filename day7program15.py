Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict1={"Sedan":1500, "SUV":2000, "Pickup":2500, "Minivan":1600, "Van":2400,
       "Semi":13600, "Bicycle":7, "Motorcycle":110}
dict1.keys()
dict_keys(['Sedan', 'SUV', 'Pickup', 'Minivan', 'Van', 'Semi', 'Bicycle', 'Motorcycle'])
dict1.values()
dict_values([1500, 2000, 2500, 1600, 2400, 13600, 7, 110])
dict1.items()
dict_items([('Sedan', 1500), ('SUV', 2000), ('Pickup', 2500), ('Minivan', 1600), ('Van', 2400), ('Semi', 13600), ('Bicycle', 7), ('Motorcycle', 110)])
for i in dict1:
    print(i)

    
Sedan
SUV
Pickup
Minivan
Van
Semi
Bicycle
Motorcycle
for i in dict1:
    print(i,dict1[i])

    
Sedan 1500
SUV 2000
Pickup 2500
Minivan 1600
Van 2400
Semi 13600
Bicycle 7
Motorcycle 110
for i in dict1:
    if (dict1[i]>5000)
    
SyntaxError: expected ':'
for i in dict1:
    if (dict1[i]>5000):
        print(i)

        
Semi
for i in dict1:
    if (dict1[i]<5000):
        print(i)

        
Sedan
SUV
Pickup
Minivan
Van
Bicycle
Motorcycle
for i in dict1:
    if dict1[i]<5000:
        print(i)

        
Sedan
SUV
Pickup
Minivan
Van
Bicycle
Motorcycle
for i in dict1:
    if dict1[i]<5000:
        print(i.upper())

        
SEDAN
SUV
PICKUP
MINIVAN
VAN
BICYCLE
MOTORCYCLE
