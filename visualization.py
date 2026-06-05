# -*- coding: utf-8 -*-

import os
import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

os.makedirs("result_images", exist_ok=True)

# =========================
# Monthly Analysis
# =========================

monthly = pd.read_csv(
    "analysis_result/monthly.csv"
)

plt.figure(figsize=(8, 5))

plt.plot(
    monthly.iloc[:, 0],
    monthly.iloc[:, 1],
    marker="o"
)

plt.title("Monthly Ridership")
plt.xlabel("Month")
plt.ylabel("Passengers")
plt.grid(True)

plt.savefig(
    "result_images/monthly_analysis.png"
)

plt.close()

# =========================
# Day Of Week Analysis
# =========================

day = pd.read_csv(
    "analysis_result/dayofweek.csv"
)

plt.figure(figsize=(8, 5))

plt.bar(
    day.iloc[:, 0].astype(str),
    day.iloc[:, 1]
)

plt.title("Day Of Week Ridership")
plt.xlabel("Day")
plt.ylabel("Passengers")

plt.savefig(
    "result_images/dayofweek_analysis.png"
)

plt.close()

# =========================
# Route Analysis
# =========================

routes = pd.read_csv(
    "analysis_result/routes.csv"
)

plt.figure(figsize=(10, 6))

plt.barh(
    routes.iloc[:, 0].astype(str),
    routes.iloc[:, 1]
)

plt.title("Top Bus Routes")
plt.xlabel("Passengers")

plt.savefig(
    "result_images/top_routes.png"
)

plt.close()

# =========================
# Station Analysis
# =========================

station = pd.read_csv(
    "analysis_result/station.csv"
)

x = range(len(station))
width = 0.35

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width/2 for i in x],
    station.iloc[:, 1],
    width=width,
    label="Ride"
)

plt.bar(
    [i + width/2 for i in x],
    station.iloc[:, 2],
    width=width,
    label="Alight"
)

plt.xticks(
    list(x),
    station.iloc[:, 0].astype(str)
)

plt.title("Boarding vs Alighting")
plt.ylabel("Passengers")
plt.legend()

plt.savefig(
    "result_images/station_direction.png"
)

plt.close()

print("=================================")
print("Visualization Complete")
print("Saved to result_images/")
print("=================================")
