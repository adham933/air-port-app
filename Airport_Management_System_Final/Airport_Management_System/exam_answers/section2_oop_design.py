"""
Section 2: OOP Design (20 Marks)
Q4, Q5, Q6
"""

# ──────────────────────────────────────────────
# Q4: Design a Flight class
# ──────────────────────────────────────────────
class Flight:
    def __init__(self, flight_id, destination, time, capacity):
        self.flight_id   = flight_id
        self.destination = destination
        self.time        = time
        self.capacity    = capacity
        self.booked      = 0          # starts with zero bookings

    def is_full(self):
        return self.booked >= self.capacity

    def display(self):
        status = "FULL" if self.is_full() else f"{self.capacity - self.booked} seats left"
        print(f"  Flight ID  : {self.flight_id}")
        print(f"  Destination: {self.destination}")
        print(f"  Time       : {self.time}")
        print(f"  Capacity   : {self.capacity}")
        print(f"  Booked     : {self.booked}  ({status})")


# ──────────────────────────────────────────────
# Q5: Design a Passenger class
# ──────────────────────────────────────────────
class Passenger:
    def __init__(self, name, passport_id, booked_flight):
        self.name          = name
        self.passport_id   = passport_id
        self.booked_flight = booked_flight    # Flight ID

    def display(self):
        print(f"  Name       : {self.name}")
        print(f"  Passport ID: {self.passport_id}")
        print(f"  Flight     : {self.booked_flight}")


# ──────────────────────────────────────────────
# Q6: Relationship between Flight and Passenger
# Association (has-a): A Passenger books a Flight
# One Flight can have many Passengers
# ──────────────────────────────────────────────
print("=" * 45)
print("Q4 — Flight object:")
f1 = Flight("EG101", "Cairo", "08:00", 150)
f1.booked = 50
f1.display()

print("\nQ5 — Passenger object:")
p1 = Passenger("Ahmed Ali", "P001", "EG101")
p1.display()

print("\nQ6 — Relationship:")
print("  Passenger ──books──▶ Flight  (Association / has-a)")
print("  A Passenger holds a reference to a Flight via booked_flight.")
print("  One Flight can serve MANY Passengers (one-to-many).")
print("  This is NOT inheritance — it is association.")
