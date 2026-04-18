<div align="center">

<!-- BANNER -->
<img src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1200&q=80" alt="Airport Banner" width="100%" style="border-radius:12px;" />

<br/><br/>

# ✈️ Airport Management System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Templates-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styled-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Based-27AE60?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

**A Flask-based Airport Flight Management Web Application**
*Built with OOP principles, Data Structures (Queue & List), and Jinja2 templating*

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Installation & Setup](#-installation--setup)
- [Routes Overview](#-routes-overview)
- [Data Structures Used](#-data-structures-used)
- [Exam Q&A — All Sections](#-exam-qa--all-sections)
  - [Section 1: Basic Concepts](#section-1-basic-concepts-10-marks)
  - [Section 2: OOP Design](#section-2-oop-design-20-marks)
  - [Section 3: Data Structures](#section-3-data-structures-20-marks)
  - [Section 4: Problem Solving](#section-4-problem-solving-30-marks)
  - [Section 5: Bonus](#section-5-bonus-10-marks)

---

## 🛫 About the Project

The **Airport Management System** is a lightweight web application built with **Python Flask** that simulates core airport operations. It demonstrates the real-world application of **Object-Oriented Programming (OOP)** and **Data Structures** (lists, dictionaries, and queues) in a working web system.

<div align="center">
<img src="https://images.unsplash.com/photo-1542296332-2e4473faf563?w=900&q=80" alt="Flights Board" width="80%" style="border-radius:10px; margin:16px 0;"/>
<br/><em>Manage flights the smart way — structured, efficient, and organized.</em>
</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ **Add Flights** | Create flights with ID, destination, time & capacity |
| 📋 **View Flights** | Browse all flights and their live booking status |
| 🎟️ **Book a Seat** | Increment booked count while respecting capacity |
| ❌ **Cancel Flight** | Remove a flight from the system and the takeoff queue |
| 🛫 **Takeoff Queue** | Process all queued flights in FIFO order |

---

## 📁 Project Structure

```
air_port app/
│
├── app.py                    # Main Flask app — routes + Flight class logic
│
├── static/
│   └── style.css             # Custom CSS (blue theme, card layout)
│
└── templates/
    ├── index.html            # Home — lists all flights with Book/Cancel
    ├── add_flight.html       # Form to add a new flight
    ├── flights.html          # Full flights list + takeoff results
    └── book.html             # Booking confirmation template
```

---

## 📸 Screenshots

> Add your own screenshots by running the app and saving images to a `/screenshots` folder in your repo, then reference them below.

| Page | Preview |
|---|---|
| 🏠 Home Page | `screenshots/home.png` |
| ➕ Add Flight | `screenshots/add_flight.png` |
| 📋 Flights List | `screenshots/flights.png` |
| 🛫 Takeoff Queue | `screenshots/takeoff.png` |

<div align="center">
<img src="https://images.unsplash.com/photo-1556388158-158ea5ccacbd?w=900&q=80" alt="Coding on laptop" width="80%" style="border-radius:10px; margin:16px 0;"/>
<br/><em>Built with Python & Flask — clean code, clean design.</em>
</div>

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.x
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/airport-management-system.git
cd airport-management-system

# 2. Install Flask
pip install flask

# 3. Run the app
python app.py
```

Open your browser at:
```
http://127.0.0.1:5000/
```

---

## 🛣️ Routes Overview

| Route | Method | Description |
|---|---|---|
| `/` | GET | Home — show all flights |
| `/add` | GET, POST | Add a new flight |
| `/book/<flight_id>` | GET | Book a seat on a flight |
| `/flights` | GET | View all flights |
| `/cancel/<flight_id>` | GET | Cancel & remove a flight |
| `/takeoff` | GET | Process the full takeoff queue |

---

## 🗂️ Data Structures Used

| Structure | Where Used | Why |
|---|---|---|
| `list` | `flights = []` | Store all Flight objects; easy to iterate, append, and filter |
| `deque` (Queue) | `takeoff_queue = deque()` | FIFO ordering — first scheduled flight departs first |
| `dict` | Q8 example | Map flight IDs to passenger counts for fast lookup |

---

## 📚 Exam Q&A — All Sections

> ✅ = Answered &nbsp;|&nbsp; Full answers with code for every question below.

---

### Section 1: Basic Concepts *(10 Marks)*

---

#### ✅ Q1: What is the main goal of OOP?

- a) Writing code faster
- **b) Organizing code into objects ✅**
- c) Deleting data
- d) Running programs only

> **Answer: (b)** — OOP groups related data and behaviors into **objects**, making code modular, reusable, and easier to maintain.

---

#### ✅ Q2: Explain the difference between Class and Object

| Term | Definition | Airport Example |
|---|---|---|
| **Class** | A blueprint/template that defines attributes and methods | `class Flight:` |
| **Object** | A real instance created from the class | `f = Flight("EG101", "Cairo", "08:00", 150)` |

- A **Class** is the *idea* of a flight.
- An **Object** is a *specific, actual* flight with real data.

---

#### ✅ Q3: Give 3 examples of classes in an airport system

| Class | Purpose |
|---|---|
| `Flight` | Stores flight ID, destination, time, and capacity |
| `Passenger` | Holds passenger name, passport ID, and booked flight |
| `Ticket` | Represents booking details linking a passenger to a flight |

---

### Section 2: OOP Design *(20 Marks)*

---

#### ✅ Q4: Design a `Flight` class

```python
class Flight:
    def __init__(self, flight_id, destination, time, capacity):
        self.flight_id   = flight_id
        self.destination = destination
        self.time        = time
        self.capacity    = capacity
        self.booked      = 0       # starts with zero bookings

    def display(self):
        print(f"Flight ID  : {self.flight_id}")
        print(f"Destination: {self.destination}")
        print(f"Time       : {self.time}")
        print(f"Capacity   : {self.capacity}")
        print(f"Booked     : {self.booked}")
```

---

#### ✅ Q5: Design a `Passenger` class

```python
class Passenger:
    def __init__(self, name, passport_id, booked_flight):
        self.name          = name
        self.passport_id   = passport_id
        self.booked_flight = booked_flight   # Flight ID

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Passport ID: {self.passport_id}")
        print(f"Flight     : {self.booked_flight}")
```

---

#### ✅ Q6: Explain the relationship between `Flight` and `Passenger`

The relationship is an **Association** (has-a relationship):

```
 Passenger ──────books──────▶ Flight
  (many)                       (one)
```

- A `Passenger` **books** a `Flight` via `booked_flight`
- A `Flight` **can serve many** Passengers (one-to-many)
- Neither class **inherits** from the other — a Passenger *has a reference to* a Flight

---

### Section 3: Data Structures *(20 Marks)*

---

#### ✅ Q7: Use a list to store 5 flights and add a new flight

```python
class Flight:
    def __init__(self, flight_id, destination, time, capacity):
        self.flight_id   = flight_id
        self.destination = destination
        self.time        = time
        self.capacity    = capacity

# Store 5 flights
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

print(f"Total flights: {len(flights)}")   # Output: Total flights: 6
```

---

#### ✅ Q8: Dictionary `{flight_id: number_of_passengers}` — book & display

```python
# Initialize dictionary
flight_passengers = {
    "EG101": 0,
    "EG202": 0,
    "EG303": 0,
}

# Book a passenger on a flight
def book_seat(flight_id):
    if flight_id in flight_passengers:
        flight_passengers[flight_id] += 1
        print(f"✅ Seat booked on flight {flight_id}.")
    else:
        print(f"❌ Flight {flight_id} not found.")

# Display all passenger counts
def display_passengers():
    print("\n--- Passenger Count per Flight ---")
    for flight_id, count in flight_passengers.items():
        print(f"  Flight {flight_id}: {count} passenger(s)")

# Example
book_seat("EG101")
book_seat("EG101")
book_seat("EG202")
display_passengers()
```

**Output:**
```
✅ Seat booked on flight EG101.
✅ Seat booked on flight EG101.
✅ Seat booked on flight EG202.

--- Passenger Count per Flight ---
  Flight EG101: 2 passenger(s)
  Flight EG202: 1 passenger(s)
  Flight EG303: 0 passenger(s)
```

---

#### ✅ Q9: Why do we use Queue in airport flight scheduling?

1. **Order of arrival** — Flights are processed in the exact order they were scheduled (FIFO).
2. **Fairness** — No flight skips the line; every flight waits its proper turn.
3. **Organized management** — Applies to takeoffs, landings, and boarding — all sequential, conflict-free operations.

```python
from collections import deque

takeoff_queue = deque()
takeoff_queue.append("EG101")   # First scheduled
takeoff_queue.append("EG202")
takeoff_queue.append("EG303")

first_to_depart = takeoff_queue.popleft()  # → "EG101" (first in, first out)
```

> 🔑 A **stack** (LIFO) would give the *last* flight priority — unfair and unsafe. A **queue** guarantees first-scheduled = first to depart.

---

### Section 4: Problem Solving *(30 Marks)*

---

#### ✅ Q10: Full program — Add flights, Display, Book passengers, Check capacity

```python
from collections import deque

class Flight:
    def __init__(self, flight_id, destination, time, capacity):
        self.flight_id   = flight_id
        self.destination = destination
        self.time        = time
        self.capacity    = capacity
        self.booked      = 0

    def display(self):
        status = "FULL" if self.booked >= self.capacity else "Available"
        print(f"  [{self.flight_id}] {self.destination} at {self.time} "
              f"— Seats: {self.booked}/{self.capacity} ({status})")


flights = []
takeoff_queue = deque()


def add_flight(flight_id, destination, time, capacity):
    f = Flight(flight_id, destination, time, capacity)
    flights.append(f)
    takeoff_queue.append(flight_id)
    print(f"✈️  Flight {flight_id} to {destination} added.")


def display_flights():
    print("\n📋 All Flights:")
    if not flights:
        print("  No flights available.")
    for f in flights:
        f.display()


def book_passenger(flight_id):
    for f in flights:
        if f.flight_id == flight_id:
            if f.booked < f.capacity:
                f.booked += 1
                print(f"✅ Seat booked on {flight_id}. "
                      f"({f.booked}/{f.capacity} seats taken)")
            else:
                print(f"❌ Flight {flight_id} is FULL.")
            return
    print(f"⚠️  Flight {flight_id} not found.")


# --- Demo ---
add_flight("EG101", "Cairo",  "08:00", 2)
add_flight("EG202", "Dubai",  "10:30", 3)

display_flights()

book_passenger("EG101")
book_passenger("EG101")
book_passenger("EG101")   # Should say FULL

display_flights()
```

**Output:**
```
✈️  Flight EG101 to Cairo added.
✈️  Flight EG202 to Dubai added.

📋 All Flights:
  [EG101] Cairo at 08:00 — Seats: 0/2 (Available)
  [EG202] Dubai at 10:30 — Seats: 0/3 (Available)

✅ Seat booked on EG101. (1/2 seats taken)
✅ Seat booked on EG101. (2/2 seats taken)
❌ Flight EG101 is FULL.

📋 All Flights:
  [EG101] Cairo at 08:00 — Seats: 2/2 (FULL)
  [EG202] Dubai at 10:30 — Seats: 0/3 (Available)
```

---

#### ✅ Q11: Use Queue for flight takeoff scheduling

```python
from collections import deque

takeoff_queue = deque()

# Schedule flights for takeoff
def schedule_takeoff(flight_id):
    takeoff_queue.append(flight_id)
    print(f"🕐 Flight {flight_id} added to takeoff queue.")

# Process takeoffs one by one
def process_takeoff():
    if takeoff_queue:
        flight_id = takeoff_queue.popleft()
        print(f"🛫 Flight {flight_id} is taking off! "
              f"Remaining in queue: {len(takeoff_queue)}")
    else:
        print("✅ No flights left in queue.")

# Process all at once
def process_all_takeoffs():
    print("\n🛫 Processing all takeoffs:")
    while takeoff_queue:
        print(f"   ✈️  Flight {takeoff_queue.popleft()} has taken off.")
    print("✅ All flights have departed.")


# --- Demo ---
schedule_takeoff("EG101")
schedule_takeoff("EG202")
schedule_takeoff("EG303")

process_all_takeoffs()
```

**Output:**
```
🕐 Flight EG101 added to takeoff queue.
🕐 Flight EG202 added to takeoff queue.
🕐 Flight EG303 added to takeoff queue.

🛫 Processing all takeoffs:
   ✈️  Flight EG101 has taken off.
   ✈️  Flight EG202 has taken off.
   ✈️  Flight EG303 has taken off.
✅ All flights have departed.
```

> The queue ensures **EG101** departs before **EG202**, and **EG202** before **EG303** — exactly the order they were scheduled.

---

#### ✅ Q12: Remove a cancelled flight from a list and display updated list

```python
class Flight:
    def __init__(self, flight_id, destination):
        self.flight_id   = flight_id
        self.destination = destination

    def display(self):
        print(f"  ✈️  [{self.flight_id}] → {self.destination}")


flights = [
    Flight("EG101", "Cairo"),
    Flight("EG202", "Dubai"),
    Flight("EG303", "London"),
    Flight("EG404", "Paris"),
]


def cancel_flight(flight_id):
    global flights
    before = len(flights)
    flights = [f for f in flights if f.flight_id != flight_id]
    after = len(flights)

    if before != after:
        print(f"❌ Flight {flight_id} has been cancelled and removed.")
    else:
        print(f"⚠️  Flight {flight_id} not found.")


def display_all():
    print("\n📋 Current Flights:")
    for f in flights:
        f.display()


# --- Demo ---
display_all()
cancel_flight("EG202")
display_all()
```

**Output:**
```
📋 Current Flights:
  ✈️  [EG101] → Cairo
  ✈️  [EG202] → Dubai
  ✈️  [EG303] → London
  ✈️  [EG404] → Paris

❌ Flight EG202 has been cancelled and removed.

📋 Current Flights:
  ✈️  [EG101] → Cairo
  ✈️  [EG303] → London
  ✈️  [EG404] → Paris
```

---

### Section 5: Bonus *(10 Marks)*

---

#### ✅ Bonus Design: Full system with `Airport`, `Flight`, and `Passenger` classes

```python
from collections import deque


class Flight:
    def __init__(self, flight_id, destination, time, capacity):
        self.flight_id   = flight_id
        self.destination = destination
        self.time        = time
        self.capacity    = capacity
        self.booked      = 0

    def is_full(self):
        return self.booked >= self.capacity

    def display(self):
        status = "FULL" if self.is_full() else f"{self.capacity - self.booked} seats left"
        print(f"  [{self.flight_id}] {self.destination} at {self.time} — {status}")


class Passenger:
    def __init__(self, name, passport_id, booked_flight):
        self.name          = name
        self.passport_id   = passport_id
        self.booked_flight = booked_flight

    def display(self):
        print(f"  🧍 {self.name} (Passport: {self.passport_id}) → Flight {self.booked_flight}")


class Airport:
    def __init__(self, name):
        self.name         = name
        self.flights      = []
        self.passengers   = []
        self.takeoff_queue = deque()

    def add_flight(self, flight_id, destination, time, capacity):
        f = Flight(flight_id, destination, time, capacity)
        self.flights.append(f)
        self.takeoff_queue.append(flight_id)
        print(f"✈️  Flight {flight_id} to {destination} added.")

    def book_passenger(self, name, passport_id, flight_id):
        for f in self.flights:
            if f.flight_id == flight_id:
                if not f.is_full():
                    f.booked += 1
                    p = Passenger(name, passport_id, flight_id)
                    self.passengers.append(p)
                    print(f"✅ {name} booked on flight {flight_id}.")
                else:
                    print(f"❌ Flight {flight_id} is FULL.")
                return
        print(f"⚠️  Flight {flight_id} not found.")

    def display_system(self):
        print(f"\n🏢 Airport: {self.name}")
        print("─" * 40)
        print("📋 Flights:")
        for f in self.flights:
            f.display()
        print("\n👥 Passengers:")
        if self.passengers:
            for p in self.passengers:
                p.display()
        else:
            print("  No passengers booked yet.")
        print(f"\n🕐 Takeoff Queue: {list(self.takeoff_queue)}")

    def process_takeoffs(self):
        print("\n🛫 Processing Takeoff Queue:")
        while self.takeoff_queue:
            print(f"   ✈️  Flight {self.takeoff_queue.popleft()} has departed!")
        print("✅ All flights processed.")


# --- Demo ---
airport = Airport("Cairo International Airport")

airport.add_flight("EG101", "Dubai",  "08:00", 2)
airport.add_flight("EG202", "London", "12:00", 3)

airport.book_passenger("Ahmed Ali",   "P001", "EG101")
airport.book_passenger("Sara Hassan", "P002", "EG101")
airport.book_passenger("Omar Khalid", "P003", "EG101")   # FULL

airport.display_system()
airport.process_takeoffs()
```

**Output:**
```
✈️  Flight EG101 to Dubai added.
✈️  Flight EG202 to London added.
✅ Ahmed Ali booked on flight EG101.
✅ Sara Hassan booked on flight EG101.
❌ Flight EG101 is FULL.

🏢 Airport: Cairo International Airport
────────────────────────────────────────
📋 Flights:
  [EG101] Dubai at 08:00 — FULL
  [EG202] London at 12:00 — 3 seats left

👥 Passengers:
  🧍 Ahmed Ali (Passport: P001) → Flight EG101
  🧍 Sara Hassan (Passport: P002) → Flight EG101

🕐 Takeoff Queue: ['EG101', 'EG202']

🛫 Processing Takeoff Queue:
   ✈️  Flight EG101 has departed!
   ✈️  Flight EG202 has departed!
✅ All flights processed.
```

---

#### ✅ Bonus Question: How can you improve system efficiency using advanced data structures?

| Improvement | Current | Better Structure | Benefit |
|---|---|---|---|
| **Finding a flight by ID** | Loop through `list` — O(n) | `dict` keyed by `flight_id` | O(1) instant lookup |
| **Priority takeoffs** | Basic FIFO `deque` | `heapq` (Priority Queue) | Emergency/VIP flights depart first |
| **Passenger search** | Loop through `list` | `dict` keyed by `passport_id` | Instant passenger lookup |
| **Undo cancellations** | Not supported | `Stack` (list with append/pop) | Restore last cancelled flight |

**Example — Priority Queue for takeoffs:**

```python
import heapq

# (priority, flight_id)  — lower number = higher priority
priority_queue = []
heapq.heappush(priority_queue, (2, "EG202"))   # Normal flight
heapq.heappush(priority_queue, (1, "EG101"))   # Emergency — priority 1
heapq.heappush(priority_queue, (3, "EG303"))   # Last in queue

while priority_queue:
    priority, flight_id = heapq.heappop(priority_queue)
    print(f"🛫 Departing: {flight_id} (Priority {priority})")
```

**Output:**
```
🛫 Departing: EG101 (Priority 1)   ← Emergency goes first!
🛫 Departing: EG202 (Priority 2)
🛫 Departing: EG303 (Priority 3)
```

---

<div align="center">

<img src="https://images.unsplash.com/photo-1464037866556-6812c9d1c72e?w=900&q=80" alt="Airplane in sky" width="80%" style="border-radius:10px; margin:16px 0;" />

---

**✅ All 12 Questions + Bonus Fully Answered**

Made with ❤️ using Python & Flask

</div>
