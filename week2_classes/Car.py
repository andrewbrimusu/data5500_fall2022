class Car:
    def __init__(self, make, model, year, price):
        print("I'm in the parent class")
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        
    def calc_value(self, current_year):
        return self.price * 0.9 ** (current_year - self.year)
        
        
class AntiqueCar(Car):
    def calc_value(self, current_year):
        return self.price * 1.04 ** (current_year - self.year)
    

andy_car = Car("toyota", "sequoia", 2001, 40000)
print(andy_car.calc_value(2022))

gavin_car = Car("toyota", "corolla", 2022, 40000)
print(gavin_car.calc_value(2022))

kauri_car = Car("infiniti", "g35x", 2007, 35000)
print(kauri_car.calc_value(2022))
    
print("gavin's antique car")
gavin_antique = AntiqueCar("mercury", "grand marquiex", 1989, 20000)
print(gavin_antique.calc_value(2022))

andys_dream_car = AntiqueCar("cadillac", "deville", 1978, 15000)
jenss_car = Car("vw", "jettas", 2020, 30000)

lot_cars = [andy_car, gavin_car, kauri_car, gavin_antique, andys_dream_car, jenss_car]


total_value = sum([car.calc_value(2022) for car in lot_cars])

print("total_value: ", total_value)


