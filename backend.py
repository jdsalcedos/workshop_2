"""
This is a set of classes to get an answer for the workshop
number I of Software Design course.

Author: Carlos Andres Sierra <cavirguezs@udistrital.edu.co>
"""


from typing import Any
from abc import ABC

class Engine:
    """This class represents the behaviour of a vehicle motor"""

    def __init__(
        self, engine_name: str, stability_engine: str, power_engine: int, weight: float, dimensions_engine: int, torque: float, maxSpeed: float
    ):
        self.__name = engine_name
        self.__stability = stability_engine
        self.__dimensions = dimensions_engine
        self.__power = power_engine
        self.__weight = weight
        self.__torque = torque
        self.__maxSpeed = maxSpeed
        

    def get_weight(self) -> int:
        """
        This method returns the weight of the engine.

        Returns:
        - int: weight of the engine
        """
        return self.__weight

    def __str__(self) -> str:
        return f"Stability: {self.__stability} Dimensions: {self.__dimensions} Power: {self.__power}\
                Weight: {self.__weight} Torque: {self.__torque} MaxSpeed: {self.__maxSpeed}"


class Car:  # pylint: disable=too-few-public-methods
    """This class is an abstraction of any car"""

    def __init__(self, engine: Engine, transmission: str, model: str, year_car: int, trade: str, combustible_type: str, chassis: str):
        self.__engine = engine
        self.__transmission = transmission
        self.__model = model
        self.__year = year_car
        self.__trade = trade
        self.__combustibleType = combustible_type
        self.__chassis = chassis

    def get_engine(self) -> Engine:
        """
        This method returns the engine of the vehicle.

        Returns:
        - Engine: engine of the vehicle
        """
        return self.__engine

    def get_year(self) -> int:
        """
        This method returns the year of the vehicle.

        Returns:
        - int: year of the vehicle
        """
        return self.__year

    

    def __str__(self):
        return f"Model: {self.__model}    Year: {self.__year}   Chassis: {self.__chassis}\
                Engine: {str(self.__engine)}    Transmission: {str(self.__transmission)}\
                Trade: {str(self.__trade)}  combustible Type:{str(self.__combustibleType)}"




class Truck:  # pylint: disable=too-few-public-methods
    """This class represents the behavior of a Truck vehicle"""
    def __init__(self, engine: Engine, model: str, year_truck: int, chassis: str):
        self.__engine = engine
        self.__model = model
        self.__year = year_truck
        self.__consumption = self.__calculate_gas_consumption()
        self.__chassis = chassis
    
    def get_engine(self) -> Engine:
        """
        This method returns the engine of the vehicle.

        Returns:
        - Engine: engine of the vehicle
        """
        return self.__engine
    
    def __calculate_gas_consumption(self) -> float:
        """
        This method calculates consumption based on engine
        values.

        Returns:
        - float: vehicle consumption
        """
        consumption = (
            (1.1 * self.__engine.get_potency())
            + (0.2 * self.__engine.weight)
            + (0.3 if self.__chassis == "A" else 0.5)
        )
        return consumption
    
    def __str__(self) -> str:
        return f"Model: {self.__model}    Year: {self.__year}    Consumption: {self.__consumption}\
                Chassis: {self.__chassis}    Engine: {str(self.__engine)}"
class Yatch:  # pylint: disable=too-few-public-methods
    """This class represents the behavior of a Yatch vehicle"""
    def __init__(self, length: float, weight: float, year_yatch: int, trade: str, model: str, engine: Engine):
        self.length = length
        self.weight = weight
        self.year = year_yatch
        self.trade = trade
        self.model = model
        self.engine = engine

class Motorcycle:  # pylint: disable=too-few-public-methods
    """This class represents the behavior of a Motorcycle vehicle"""
    def __init__(self, engine: Engine, model: str, year_motorcycle: int, chassis: str):
        self.__engine = engine
        self.__model = model
        self.__year = year_motorcycle
        self.__chassis = chassis

    def get_engine(self) -> Engine:
        """
        This method returns the engine of the motorcycle.
        """
        return self.__engine
    
    def __str__(self) -> str:
        return f"Model: {self.__model}    Year: {self.__year}    Chassis: {self.__chassis}\
                Engine: {str(self.__engine)}"
    

class Helicopter:

    def __init__(self, engine: Engine, capacity: int, helicopter_type: str):
        self.__engine = engine
        self.__capacity = capacity
        self.__type = helicopter_type

    def get_engine(self):
        """
        This method returns the engine of the helicopter.
        """
        return self.__engine
    def __str__(self) -> str:
        return f"Capacity: {self.__capacity}    Type: {self.__type}    engine: {str(self.__engine)}"

class Scooter:

    def __init__(self, engine: Engine, capacityWeight: float):
        self.__engine = engine
        self.__capacityWeight = capacityWeight
    
    def get_engine(self):
        """
        This method returns the engine of the scooter.
        """
        return self.__engine
    
    def __str__(self) -> str:
        return f"Capacity: {self.__capacityWeight}    engine: {str(self.__engine)}"



# ==================================== MENU
MESSAGE = """
Option 1. Create engine
Option 2. Create car
Option 3. Create truck
Option 4. Create yatch
Option 5. Crear motorcyle
Option 6. Show engines
Option 7. Show vehicles
Option 8. Search by year
Option 9. Search by potency
Opcion 10. Exit
"""

# save data related to engines and vehicles in memory, sort of a database
engines = {}
vehicles = []


def create_engine():
    """This method lets add a new engine to list"""
    
    new_obj_engine = Engine("Engine 1", "good", 300, 450.5 ,600, 480.6, 186.9)
    engines["Engine 1"] = new_obj_engine

def create_vehicle(type_vehicle: str):
    """
    This method lets create a new vehicle and add it to the
    catalog.

    Parameters:
    - type_vehicle (str): The type of the vehicle
    """
    chassis = input("Write the chassis of the vehicle (A or B):")
    if chassis not in ["A", "B"]:
        raise ValueError("Error: Chassis wrote is wrong. Must be A or B.")
    model = input("Write the model of the vehicle: ")
    year_ = int(
        input("Write the year of the vehicle (should be greater or equal than 2000): ")
    )
    if year_ < 2000:
        raise ValueError("Error. Year is not in a valid range.")
    engine_name = input("Write the name of the motor for the vehicle: ")

    transmission = input("Write the transmission of the car")

    try:
        engine = engines[engine_name]
        if type_vehicle == "car":
            vehicle_obj_new = Car(engine, chassis, model, year_)
        elif type_vehicle == "truck":
            vehicle_obj_new = Truck(engine, chassis, model, year_)
        elif type_vehicle == "yatch":
            vehicle_obj_new = Yatch(engine, chassis, model, year_)
        elif type_vehicle == "motorcycle":
            vehicle_obj_new = Motorcycle(engine, chassis, model, year_)
        vehicles.append(vehicle_obj_new)
    except Exception as e:
        print(f"Error: {e}.")


def search_by_year(year_: int) -> list:
    """
    This method makes a search of all vehicles of a specific
    year.

    Parameters:
    - year (int): Year to filter
    """
    return [vehicle for vehicle in vehicles if vehicle.get_year() == year_]


def search_by_potency(potency_: float) -> list:
    """
    This method makaes a search of vehicles based on the potency
    of the engine of the vehicle.

    Parameters:
    - potency_ (float): Potency to filter
    """
    return [
        vehicle
        for vehicle in vehicles
        if vehicle.get_engine().get_potency() == potency_
    ]


print(MESSAGE)
option = int(input("Please, choise an option: "))
while option != 10:
    if option == 1:
        create_engine()
    elif option == 2:
        create_vehicle("car")
    elif option == 3:
        create_vehicle("truck")
    elif option == 4:
        create_vehicle("yatch")
    elif option == 5:
        create_vehicle("motorcycle")
    elif option == 6:
        for name, values in engines.items():
            print(f"{name} = {str(values)}")
    elif option == 7:
        for vehicle in vehicles:
            print(vehicle)
    elif option == 8:
        year = int(input("Please, write the year: "))
        search_by_year(year)
    elif option == 9:
        potency = float(input("Please, write the potency:"))
        search_by_potency(potency)
    else:
        print("Invalid option.")
    print("\n\n" + MESSAGE)
    option = int(input("Please, choise an option: "))
