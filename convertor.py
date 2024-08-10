#This program is about converting unit of 
# speed
# distance
# temperature

class convert: 
    def __init__(self,unit,choice):
        self.unit = unit
        self.choice = choice
    def conversion_velocity(self):
        if(self.choice == 1):
            new_speed = round(self.unit * (5/18),2)
            print(new_speed,"m/s")
        elif(self.choice == 2):
            new_speed = round(self.unit * (18/5),2)
            print(new_speed,"km/hr")
        else:
            print("Wrong Choice, try again")
            
    def conversion_distance(self):
        if(self.choice == 1):
            new_distance = self.unit * 1.609
            print(new_distance ,"km")
        elif(self.choice == 2):
            new_distance = self.unit / 1.609
            print(new_distance,"miles")
        else:
            print("Wrong Choice, try again")
            
    def conversion_temperature(self):
        if(self.choice == 1):
            new_temperature = (self.unit * 9 / 5) + 32
            print(new_temperature,"°F")
        elif(self.choice == 2):    
            new_temperature = self.unit + 273
            print(new_temperature,"K")
        elif(self.choice == 3):  
            new_temperature = (self.unit - 32) * 5 / 9
            print(new_temperature,"°C")
        elif(self.choice == 4):  
            new_temperature = (self.unit - 32) * 5 / 9 + 273
            print(new_temperature,"K")
        elif(self.choice == 5): 
            new_temperature = self.unit - 273
            print(new_temperature,"°C")
        elif(self.choice == 6):  
            new_temperature = (self.unit - 32) * 5 / 9 - 273
            print(new_temperature,"°F")
        else:
            print("wrong choice try again!")
repeat = 'y'
while repeat == 'y' or repeat == 'Y':
    try:
        choice = int(input("""Enter Choice :
1 : speed conversion
2 : Distance conversion
3 : Temperature conversion"""))

        if choice == 1:
            choice1 = int(input("""Enter Choice :
1 : Convert km/hr to m/s
2 : Convert m/s to km/hr 
"""))
            speed = float(input("Enter Speed : "))
            converting = convert(speed,choice1)
            converting.conversion_velocity()
        elif choice == 2:
            choice1 = int(input("""Enter Choice :
1 : Convert miles to km 
2 : Convert Km to miles
"""))
            distance = float(input("Enter distance : "))
            converting = convert(distance,choice1)
            converting.conversion_distance()
        elif choice == 3:
            choice1 = int(input("""Enter Choice :
1 : Convert °C to °F
2 : Convert °C to K
3 : Convert °F to °C
4 : Convert °F to k
5 : Convert K to °C
6 : Convert K to °F
"""))
            temperature = float(input("Enter Temperature : "))
            converting = convert(temperature,choice1)
            converting.conversion_temperature()
            
        else:
            print("Wrong Choice, try again")
        
        repeat = input("Enter 'y' to try again or enter any key to stop")
        
        if (repeat != 'y' or repeat != 'Y'):
            print("Thanks for using this program ☺")
    except ValueError:
        print("Wrong input, try again")