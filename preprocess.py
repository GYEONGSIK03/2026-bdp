# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, month, dayofweek
from pyspark.sql.types import IntegerType

# =========================
# Spark Session 생성
# =========================

spark = SparkSession.builder \
    .appName("MJU_Bus_Preprocessing") \
    .getOrCreate()

# =========================
# 1. API 데이터 읽기
# =========================

df = spark.read \
    .option("header", "true") \
    .csv(
        "/user/maria_dev/api_data/BUS_STATION_BOARDING_2025_1H.csv"
    )

# =========================
# 2. 명지대 정류장 필터링
# =========================

target_stations = ["13195", "13194"]

filtered_df = df.filter(
    col("STOPS_ARS_NO").isin(target_stations)
)

# =========================
# 3. 필요한 컬럼 선택
# =========================

selected_df = filtered_df.select(
    "USE_YMD",
    "RTE_NO",
    "RTE_NM",
    "STOPS_ARS_NO",
    "SBWY_STNS_NM",
    "GTON_TNOPE",
    "GTOFF_TNOPE"
)

# =========================
# 4. 데이터 타입 변환
# =========================

processed_df = selected_df \
    .withColumn(
        "GTON_TNOPE",
        col("GTON_TNOPE").cast(IntegerType())
    ) \
    .withColumn(
        "GTOFF_TNOPE",
        col("GTOFF_TNOPE").cast(IntegerType())
    )

# =========================
# 5. 날짜 컬럼 생성
# =========================

processed_df = processed_df.withColumn(
    "ride_date",
    to_date(col("USE_YMD"), "yyyyMMdd")
)

# =========================
# 6. 월 컬럼 추가
# =========================

processed_df = processed_df.withColumn(
    "month",
    month(col("ride_date"))
)

# =========================
# 7. 요일 컬럼 추가
# =========================

processed_df = processed_df.withColumn(
    "day_of_week",
    dayofweek(col("ride_date"))
)

# =========================
# 8. 결측치 제거
# =========================

processed_df = processed_df.dropna()

# =========================
# 9. 중복 제거
# =========================

processed_df = processed_df.dropDuplicates()

# =========================
# 10. Hive 스키마 맞춤
# =========================

processed_df = processed_df.select(
    col("USE_YMD").alias("use_date"),
    col("RTE_NO").alias("route_id"),
    col("RTE_NM").alias("route_name"),
    col("STOPS_ARS_NO").alias("station_ars_id"),
    col("SBWY_STNS_NM").alias("station_name"),
    col("GTON_TNOPE").alias("ride_passenger"),
    col("GTOFF_TNOPE").alias("alight_passenger"),
    col("ride_date").cast("string"),
    col("month"),
    col("day_of_week")
)

# =========================
# 11. 결과 확인
# =========================

print("전처리 후 데이터 개수:")
print(processed_df.count())

# =========================
# 12. HDFS 저장
# =========================

processed_df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("/user/maria_dev/processed/mju_bus")

# =========================
# 13. Spark 종료
# =========================

spark.stop()
