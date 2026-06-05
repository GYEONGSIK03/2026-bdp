# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# -----------------------
# 1. 월별 승차 인원
# -----------------------

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
monthly_ride = [38367, 37218, 57428, 62086, 55115, 53087]

plt.figure(figsize=(8,5))
plt.bar(months, monthly_ride)
plt.title('Monthly Bus Ridership')
plt.xlabel('Month')
plt.ylabel('Passengers')
plt.tight_layout()
plt.savefig('monthly_analysis.png')
plt.close()

# -----------------------
# 2. 요일별 승차 인원
# -----------------------

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
daily_ride = [25859, 42513, 49082, 52519, 55330, 42493, 35505]

plt.figure(figsize=(8,5))
plt.bar(days, daily_ride)
plt.title('Ridership by Day of Week')
plt.xlabel('Day')
plt.ylabel('Passengers')
plt.tight_layout()
plt.savefig('dayofweek_analysis.png')
plt.close()

# -----------------------
# 3. 노선별 TOP 이용객
# -----------------------

routes = [
    '7612',
    '7734',
    '7021',
    '7611',
    '7019',
    '7713',
    '7017',
    'N75',
    '8773'
]

route_passengers = [
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

plt.figure(figsize=(10,6))
plt.barh(routes, route_passengers)
plt.title('Top Bus Routes')
plt.xlabel('Passengers')
plt.tight_layout()
plt.savefig('top_routes.png')
plt.close()

# -----------------------
# 4. 승차/하차 비교
# -----------------------

stations = [
    '13195\n(MJU)',
    '13196\n(MJU Intersection)'
]

ride = [246042, 57259]
alight = [60103, 100706]

x = range(len(stations))
width = 0.35

plt.figure(figsize=(8,5))
plt.bar(
    [i - width/2 for i in x],
    ride,
    width=width,
    label='Ride'
)

plt.bar(
    [i + width/2 for i in x],
    alight,
    width=width,
    label='Alight'
)

plt.xticks(x, stations)
plt.title('Boarding vs Alighting')
plt.ylabel('Passengers')
plt.legend()
plt.tight_layout()
plt.savefig('station_direction.png')
plt.close()

print("Visualization Complete")
