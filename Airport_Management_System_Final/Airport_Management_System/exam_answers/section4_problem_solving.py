"""
Section 4: Problem Solving (30 Marks)
Q10, Q11, Q12
"""
from collections import deque


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
        print(f"  [{self.flight_id}] {self.destination} at {self.time} "
              f"— Seats: {self.booked}/{self.capacity} ({status})")


flights       = []
takeoff_queue = deque()


# ──────────────────────────────────────────────
# Q10: Full program — add, display, book, capacity
# ──────────────────────────────────────────────
def add_flight(flight_id, destination, time, capacity):
    f = Flight(flight_id, destination, time, capacity)
    flights.append(f)
    takeoff_queue.append(flight_id)
    print(f"  ✈️  Flight {flight_id} to {destination} added.")

def display_flights():
    print("\n  📋 All Flights:")
    if not flights:
        print("  No flights available.")
        return
    for f in flights:
        f.display()

def book_passenger(flight_id):
    for f in flights:
        if f.flight_id == flight_id:
            if not f.is_full():
                f.booked += 1
                print(f"  ✅ Seat booked on {flight_id}. ({f.booked}/{f.capacity})")
            else:
                print(f"  ❌ Flight {flight_id} is FULL — cannot book.")
            return
    print(f"  ⚠️  Flight {flight_id} not found.")


print("=" * 50)
print("Q10 — Add, Display, Book, Check Capacity:")
add_flight("EG101", "Cairo",  "08:00", 2)
add_flight("EG202", "Dubai",  "10:30", 3)
display_flights()
book_passenger("EG101")
book_passenger("EG101")
book_passenger("EG101")   # Should be FULL
display_flights()


# ──────────────────────────────────────────────
# Q11: Queue for flight takeoff scheduling
# ──────────────────────────────────────────────
def process_all_takeoffs():
    print("\n  🛫 Processing Takeoff Queue (FIFO):")
    if not takeoff_queue:
        print("  Queue is empty.")
        return
    while takeoff_queue:
        fid = takeoff_queue.popleft()
        print(f"     ✈️  Flight {fid} has taken off!")
    print("  ✅ All flights processed.")

print("\n" + "=" * 50)
print("Q11 — Takeoff Queue:")
print("  Current queue:", list(takeoff_queue))
process_all_takeoffs()


# ──────────────────────────────────────────────
# Q12: Remove cancelled flight from list
# ──────────────────────────────────────────────
def cancel_flight(flight_id):
    global flights
    before = len(flights)
    flights = [f for f in flights if f.flight_id != flight_id]
    if len(flights) < before:
        print(f"  ❌ Flight {flight_id} cancelled and removed.")
    else:
        print(f"  ⚠️  Flight {flight_id} not found.")

print("\n" + "=" * 50)
print("Q12 — Cancel & Remove a Flight:")

# Reset for demo
flights = []
add_flight("EG101", "Cairo",  "08:00", 150)
add_flight("EG202", "Dubai",  "10:30", 200)
add_flight("EG303", "London", "13:00", 180)

display_flights()
cancel_flight("EG202")
display_flights()
