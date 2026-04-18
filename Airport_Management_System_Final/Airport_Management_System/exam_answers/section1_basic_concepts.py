"""
Section 1: Basic Concepts (10 Marks)
Q1, Q2, Q3
"""


print("Q1 Answer: (b) Organizing code into objects")
print("OOP groups related data and behavior into objects,")
print("making code modular, reusable, and easy to maintain.\n")



class Car:          
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

my_car = Car("Toyota", "Red")  

print("Q2: Class vs Object")
print(f"  Class  → Car  (blueprint: defines brand, color)")
print(f"  Object → my_car = Car('Toyota', 'Red')  (real instance)")
print(f"  my_car.brand = {my_car.brand}, my_car.color = {my_car.color}\n")


# ──────────────────────────────────────────────
# Q3: 3 examples of classes in an airport system
# ──────────────────────────────────────────────
class Flight:
    """Stores flight ID, destination, time, and capacity."""
    def __init__(self, flight_id, destination):
        self.flight_id   = flight_id
        self.destination = destination

class Passenger:
    """Holds passenger name and passport ID."""
    def __init__(self, name, passport_id):
        self.name        = name
        self.passport_id = passport_id

class Ticket:
    """Represents booking details linking a passenger to a flight."""
    def __init__(self, ticket_id, passenger, flight):
        self.ticket_id = ticket_id
        self.passenger = passenger
        self.flight    = flight

print("Q3: 3 Classes in an Airport System")
print("  1. Flight    — stores flight number, destination, time, capacity")
print("  2. Passenger — holds passenger name and passport ID")
print("  3. Ticket    — represents booking details (passenger + flight)")
