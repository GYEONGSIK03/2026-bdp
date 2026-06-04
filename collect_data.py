# -*- coding: utf-8 -*-

import requests
import pandas as pd
import os

API_KEY = "7a6f454f7a72756433306d4b55414e"

os.makedirs("data", exist_ok=True)

all_rows = []

# =========================
# 2025년 1~6월
# 매월 1~15일 수집
# =========================

for month in range(1, 7):

    for day in range(1, 16):

        use_dt = f"2025{month:02d}{day:02d}"

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

                r = requests.get(
                    url,
                    timeout=30
                )

                data = r.json()

            except Exception as e:

                print(
                    "Error:",
                    use_dt,
                    e
                )

                break

            service = data.get(
                "CardBusStatisticsServiceNew"
            )

            if not service:
                break

            rows = service.get(
                "row",
                []
            )

            if len(rows) == 0:
                break

            # 원본 데이터 전체 저장
            all_rows.extend(rows)

            if len(rows) < 1000:
                break

            start += 1000
            end += 1000

# =========================
# CSV 저장
# =========================

df = pd.DataFrame(all_rows)

output_file = (
    "data/BUS_STATION_BOARDING_2025_1H.csv"
)

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print(
    "Saved:",
    len(df)
)

# =========================
# HDFS 업로드
# =========================

os.system(
    "hdfs dfs -mkdir -p "
    "/user/maria_dev/api_data"
)

os.system(
    "hdfs dfs -put -f "
    + output_file +
    " /user/maria_dev/api_data/"
)

print(
    "Uploaded to HDFS: "
    "/user/maria_dev/api_data"
)
