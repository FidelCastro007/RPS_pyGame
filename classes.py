#classes
#Parent class is blue print of all objects & child class

class Vehicle:
    def __init__(self, make, model): #self param assocites to class its object to access props # constructor in js this func be like //self be like tenables in js
        self.make = make
        self.model = model
    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        return(f"I'm a {self.make} {self.model}")

my_car = Vehicle('Tesla','Model Y')

my_car.moves()
print(my_car.make)
print(my_car.model)
my_car.get_make_model()

print('\n\n')

#Inheritance
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print("FLies along..") #overwrites the vechile moves()
    def get_make_model(self):
        basic_info = super().get_make_model()
        return f"{basic_info} FAA ID: {self.faa_id}."

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')

class GolfCart(Vehicle):
    pass # parent class props & props vals are directly passed into child class

my_airPlane = Airplane("Milan","model ZZ",'N-15741')
print(my_airPlane.get_make_model())
my_airPlane.moves()

my_Truck = Truck("Holla",'Mode; F')
my_Truck.get_make_model()
my_Truck.moves()

my_Golfcart = GolfCart('GGM',"Zen Model")
my_Golfcart.get_make_model()
my_Golfcart.moves()

print('\n\n')

# Polymorsphism
for v in (my_car,my_airPlane,my_Golfcart,my_Truck):
    print(v.get_make_model()) # single method is used but this method applies in different objects to get multiple vals is called polymorsphism
    v.moves()
    print('\n\n')

#try,catch & finally
x=2
try:
    print(x/0)
except NameError:
    print("NameError means something is probably undefined.")

except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:
    print(error)

else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error.")