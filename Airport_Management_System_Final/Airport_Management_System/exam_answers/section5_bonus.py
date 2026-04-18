"""
Section 5: Bonus (10 Marks)
Full system: Airport + Flight + Passenger classes
Bonus Question: Improve efficiency with advanced data structures
"""
from collections import deque
import heapq


# ──────────────────────────────────────────────
# Flight Class
# ──────────────────────────────────────────────
class Flight:
    def __init__(self, flight_id, destination, time, capacity):
        self.flight_id   = flight_id
        self.destination = destination
        self.time        = time
        self.capacity    = int(capacity)
        self.booked      = 0

    def is_full(self):
        return self.booked >= self.capacity

    def display(self):
        status = "FULL" if self.is_full() else f"{self.capacity - self.booked} seats left"
        print(f"    [{self.flight_id}] {self.destination} at {self.time} — {status}")


# ──────────────────────────────────────────────
# Passenger Class
# ──────────────────────────────────────────────
class Passenger:
    def __init__(self, name, passport_id, booked_flight):
        self.name          = name
        self.passport_id   = passport_id
        self.booked_flight = booked_flight

    def display(self):
        print(f"    🧍 {self.name} (Passport: {self.passport_id})"
              f" → Flight {self.booked_flight}")


# ──────────────────────────────────────────────
# Airport Class — full system
# ──────────────────────────────────────────────
class Airport:
    def __init__(self, name):
        self.name          = name
        self.flights       = []
        self.passengers    = []
        self.takeoff_queue = deque()

    def add_flight(self, flight_id, destination, time, capacity):
        f = Flight(flight_id, destination, time, capacity)
        self.flights.append(f)
        self.takeoff_queue.append(flight_id)
        print(f"  ✈️  Flight {flight_id} to {destination} added.")

    def book_passenger(self, name, passport_id, flight_id):
        for f in self.flights:
            if f.flight_id == flight_id:
                if not f.is_full():
                    f.booked += 1
                    p = Passenger(name, passport_id, flight_id)
                    self.passengers.append(p)
                    print(f"  ✅ {name} booked on flight {flight_id}.")
                else:
                    print(f"  ❌ Flight {flight_id} is FULL.")
                return
        print(f"  ⚠️  Flight {flight_id} not found.")

    def display_system(self):
        print(f"\n  🏢 Airport: {self.name}")
        print("  " + "─" * 40)
        print("  📋 Flights:")
        for f in self.flights:
            f.display()
        print("\n  👥 Passengers:")
        if self.passengers:
            for p in self.passengers:
                p.display()
        else:
            print("    No passengers booked yet.")
        print(f"\n  🕐 Takeoff Queue: {list(self.takeoff_queue)}")

    def process_takeoffs(self):
        print("\n  🛫 Processing Takeoff Queue:")
        while self.takeoff_queue:
            print(f"     ✈️  Flight {self.takeoff_queue.popleft()} has departed!")
        print("  ✅ All flights processed.")


# ── Demo ──
print("=" * 50)
print("BONUS — Full Airport System:")
airport = Airport("Cairo International Airport")

airport.add_flight("EG101", "Dubai",  "08:00", 2)
airport.add_flight("EG202", "London", "12:00", 3)

airport.book_passenger("Ahmed Ali",   "P001", "EG101")
airport.book_passenger("Sara Hassan", "P002", "EG101")
airport.book_passenger("Omar Khalid", "P003", "EG101")   # FULL

airport.display_system()
airport.process_takeoffs()


# ──────────────────────────────────────────────
# Bonus Question: Improve with advanced structures
# ──────────────────────────────────────────────
print("\n" + "=" * 50)
print("BONUS QUESTION — Priority Queue with heapq:")
print("(Emergency/VIP flights depart before regular ones)\n")

priority_queue = []
# (priority_level, flight_id)  — lower number = higher priority
heapq.heappush(priority_queue, (2, "EG202"))   # Normal
heapq.heappush(priority_queue, (1, "EG101"))   # Emergency
heapq.heappush(priority_queue, (3, "EG303"))   # Last

print("  Departure order (by priority):")
while priority_queue:
    priority, fid = heapq.heappop(priority_queue)
    label = "🚨 Emergency" if priority == 1 else "🔵 Normal"
    print(f"    [{priority}] {label} — Flight {fid} departs!")

print("\n  Other improvements:")
print("  • dict keyed by flight_id  → O(1) lookup instead of O(n) list scan")
print("  • dict keyed by passport   → O(1) passenger search")
print("  • Stack (list + pop)       → undo last cancellation")
