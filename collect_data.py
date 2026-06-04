# -*- coding: utf-8 -*-

import requests
import pandas as pd
import os

API_KEY = "7a6f454f7a72756433306d4b55414e"



os.makedirs("data", exist_ok=True)

all_rows = []

for month in range(1, 13):

    use_dt = f"2025{month:02d}01"

    url = (
        f"http://openapi.seoul.go.kr:8088/"
        f"{API_KEY}/json/CardBusStatisticsServiceNew/"
        f"1/1000/{use_dt}"
    )

    print("Downloading:", use_dt)

    r = requests.get(url)
    data = r.json()

    service = data.get("CardBusStatisticsServiceNew")

    if not service:
        print("No data:", use_dt)
        continue

    rows = service.get("row", [])
    all_rows.extend(rows)

df = pd.DataFrame(all_rows)

df.to_csv(
    "data/BUS_STATION_BOARDING_MONTH_2025.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Saved:", len(df))
