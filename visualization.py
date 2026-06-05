import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

# -------------------------
# Monthly Analysis
# -------------------------

months = [1, 2, 3, 4, 5, 6]
rides = [38367, 37218, 57428, 62086, 55115, 53087]

plt.figure(figsize=(8, 5))
plt.plot(months, rides, marker="o")
plt.title("Monthly Ridership")
plt.xlabel("Month")
plt.ylabel("Passengers")
plt.grid(True)

plt.savefig("monthly_analysis.png")
plt.close()

# -------------------------
# Day Of Week Analysis
# -------------------------

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

day_rides = [
    25859,
    42513,
    49082,
    52519,
    55330,
    42493,
    35505
]

plt.figure(figsize=(8, 5))
plt.bar(days, day_rides)

plt.title("Day Of Week Ridership")
plt.xlabel("Day")
plt.ylabel("Passengers")

plt.savefig("dayofweek_analysis.png")
plt.close()

# -------------------------
# Top Routes
# -------------------------

routes = [
    "7612",
    "7734",
    "7021",
    "7611",
    "7019",
    "7713",
    "7017",
    "N75",
    "8773"
]

route_rides = [
    81111,
    61488,
    40578,
    39739,
    32755,
    26318,
    16964,
    2282,
    2066
]

plt.figure(figsize=(10, 6))

plt.barh(routes, route_rides)

plt.title("Top Bus Routes")
plt.xlabel("Passengers")

plt.savefig("top_routes.png")
plt.close()

# -------------------------
# Station Comparison
# -------------------------

stations = [
    "MJU",
    "MJU Intersection"
]

ride = [
    246042,
    57259
]

alight = [
    60103,
    100706
]

x = range(len(stations))
width = 0.35

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width/2 for i in x],
    ride,
    width=width,
    label="Ride"
)

plt.bar(
    [i + width/2 for i in x],
    alight,
    width=width,
    label="Alight"
)

plt.xticks(x, stations)

plt.title("Boarding vs Alighting")
plt.ylabel("Passengers")
plt.legend()

plt.savefig("station_direction.png")
plt.close()

print("Visualization Complete")
