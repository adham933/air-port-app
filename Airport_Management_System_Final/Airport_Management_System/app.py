from flask import Flask, render_template, request, redirect
from collections import deque

app = Flask(__name__)

# ─────────────────────────────────────────────
#  Flight Class  (Q4 — OOP Design)
# ─────────────────────────────────────────────
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
        print(f"[{self.flight_id}] {self.destination} at {self.time} — {status}")


# ─────────────────────────────────────────────
#  Passenger Class  (Q5 — OOP Design)
# ─────────────────────────────────────────────
class Passenger:
    def __init__(self, name, passport_id, booked_flight):
        self.name          = name
        self.passport_id   = passport_id
        self.booked_flight = booked_flight

    def display(self):
        print(f"{self.name} (Passport: {self.passport_id}) → Flight {self.booked_flight}")


# ─────────────────────────────────────────────
#  Global Data Structures
# ─────────────────────────────────────────────
flights       = []        # list  — stores all Flight objects  (Q7)
passengers    = []        # list  — stores all Passenger objects
takeoff_queue = deque()   # deque — FIFO takeoff scheduling    (Q11)


# ─────────────────────────────────────────────
#  Routes
# ─────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("index.html", flights=flights)


# Q10 — Add flights
@app.route("/add", methods=["GET", "POST"])
def add_flight():
    if request.method == "POST":
        f = Flight(
            request.form["flight_id"],
            request.form["destination"],
            request.form["time"],
            request.form["capacity"]
        )
        flights.append(f)
        takeoff_queue.append(f.flight_id)
        return redirect("/")
    return render_template("add_flight.html")


# Q10 — Book passengers + check capacity
@app.route("/book/<flight_id>")
def book(flight_id):
    for f in flights:
        if f.flight_id == flight_id:
            if not f.is_full():
                f.booked += 1
            break
    return redirect("/")


# Q10 — Display flights
@app.route("/flights")
def show_flights():
    return render_template("flights.html", flights=flights)


# Q12 — Remove a cancelled flight from the list
@app.route("/cancel/<flight_id>")
def cancel(flight_id):
    global flights
    flights = [f for f in flights if f.flight_id != flight_id]
    if flight_id in takeoff_queue:
        takeoff_queue.remove(flight_id)
    return redirect("/flights")


# Q11 — Queue for takeoff scheduling
@app.route("/takeoff")
def takeoff():
    taken_off = []
    while takeoff_queue:
        taken_off.append(takeoff_queue.popleft())
    return render_template("flights.html", flights=flights, taken_off=taken_off)


if __name__ == "__main__":
    app.run(debug=True)
