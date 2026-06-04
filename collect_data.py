# -*- coding: utf-8 -*-

import requests
import pandas as pd
import os

from datetime import datetime, timedelta

API_KEY = "7a6f454f7a72756433306d4b55414e"

os.makedirs("data", exist_ok=True)

all_rows = []

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

current_date = start_date

while current_date <= end_date:

    use_dt = current_date.strftime("%Y%m%d")

    start = 1
    end = 1000

    while True:

        url = (
            f"http://openapi.seoul.go.kr:8088/"
            f"{API_KEY}/json/CardBusStatisticsServiceNew/"
            f"{start}/{end}/{use_dt}"
        )

        print(
            f"Downloading {use_dt} "
            f"({start}~{end})"
        )

        try:
            r = requests.get(url, timeout=30)
            data = r.json()
        except:
            break

        service = data.get(
            "CardBusStatisticsServiceNew"
        )

        if not service:
            break

        rows = service.get("row", [])

        if len(rows) == 0:
            break

        # 명지대 정류장만 저장
        for row in rows:

            ars = str(
                row.get("STOPS_ARS_NO", "")
            )

            if ars in ["13195", "13196"]:
                all_rows.append(row)

        if len(rows) < 1000:
            break

        start += 1000
        end += 1000

    current_date += timedelta(days=1)

df = pd.DataFrame(all_rows)

output_file = (
    "data/BUS_STATION_BOARDING_MONTH_2025.csv"
)

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("Saved:", len(df))

os.system(
    "hdfs dfs -mkdir -p "
    "/user/maria_dev/api_data"
)

os.system(
    "hdfs dfs -put -f "
    + output_file +
    " /user/maria_dev/api_data/"
)

print("Uploaded to HDFS: /user/maria_dev/api_data")

print("Uploaded to HDFS")
