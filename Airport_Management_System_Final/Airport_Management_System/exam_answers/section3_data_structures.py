"""
Section 3: Data Structures (20 Marks)
Q7, Q8, Q9
"""
from collections import deque


class Flight:
    def __init__(self, flight_id, destination, time, capacity):
        self.flight_id   = flight_id
        self.destination = destination
        self.time        = time
        self.capacity    = capacity


# ──────────────────────────────────────────────
# Q7: List — store 5 flights, add a new flight
# ──────────────────────────────────────────────
flights = [
    Flight("EG101", "Cairo",    "08:00", 150),
    Flight("EG202", "Dubai",    "10:30", 200),
    Flight("EG303", "London",   "13:00", 180),
    Flight("EG404", "Paris",    "15:45", 160),
    Flight("EG505", "New York", "20:00", 220),
]

# Add a new flight
new_flight = Flight("EG606", "Istanbul", "22:00", 170)
flights.append(new_flight)

print("Q7 — Flights List:")
for f in flights:
    print(f"  [{f.flight_id}] {f.destination} at {f.time}")
print(f"  Total: {len(flights)} flights\n")


# ──────────────────────────────────────────────
# Q8: Dictionary — {flight_id: passengers_count}
# ──────────────────────────────────────────────
flight_passengers = {
    "EG101": 0,
    "EG202": 0,
    "EG303": 0,
}

def book_seat(flight_id):
    if flight_id in flight_passengers:
        flight_passengers[flight_id] += 1
        print(f"  ✅ Seat booked on flight {flight_id}.")
    else:
        print(f"  ❌ Flight {flight_id} not found.")

def display_passengers():
    print("  --- Passenger Count per Flight ---")
    for fid, count in flight_passengers.items():
        print(f"  Flight {fid}: {count} passenger(s)")

print("Q8 — Dictionary booking:")
book_seat("EG101")
book_seat("EG101")
book_seat("EG202")
display_passengers()


# ──────────────────────────────────────────────
# Q9: Queue — airport flight scheduling
# ──────────────────────────────────────────────
print("\nQ9 — Queue (FIFO) for takeoff scheduling:")
print("  Reason: Flights are processed in the order they arrive.")
print("  The first flight scheduled is the first to take off.")
print("  This ensures fairness and organized management.\n")

takeoff_queue = deque()
takeoff_queue.append("EG101")
takeoff_queue.append("EG202")
takeoff_queue.append("EG303")

print("  Queue:", list(takeoff_queue))
first = takeoff_queue.popleft()
print(f"  First to take off: {first}")
print("  Remaining queue:", list(takeoff_queue))
