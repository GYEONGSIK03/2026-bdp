
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
# 1. HDFS CSV 읽기
# =========================

df = spark.read \
    .option("header", "true") \
    .option("encoding", "cp949") \
    .csv("/user/maria_dev/BUS_STATION_BOARDING_MONTH/*.csv")

# =========================
# 2. 명지대 정류장 필터링
# =========================

target_stations = ["13195", "13196"]

filtered_df = df.filter(
    col("버스정류장ARS번호").isin(target_stations)
)

# =========================
# 3. 필요한 컬럼 선택
# =========================

selected_df = filtered_df.select(
    "사용일자",
    "노선번호",
    "노선명",
    "버스정류장ARS번호",
    "역명",
    "승차총승객수",
    "하차총승객수"
)

# =========================
# 4. 데이터 타입 변환
# =========================

processed_df = selected_df \
    .withColumn(
        "승차총승객수",
        col("승차총승객수").cast(IntegerType())
    ) \
    .withColumn(
        "하차총승객수",
        col("하차총승객수").cast(IntegerType())
    )

# =========================
# 5. 날짜 컬럼 생성
# =========================

processed_df = processed_df.withColumn(
    "date",
    to_date(col("사용일자"), "yyyyMMdd")
)

# =========================
# 6. 월 컬럼 추가
# =========================

processed_df = processed_df.withColumn(
    "month",
    month(col("date"))
)

# =========================
# 7. 요일 컬럼 추가
# =========================

processed_df = processed_df.withColumn(
    "day_of_week",
    dayofweek(col("date"))
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
    col("사용일자").alias("use_date"),
    col("노선번호").alias("route_id"),
    col("노선명").alias("route_name"),
    col("버스정류장ARS번호").alias("station_ars_id"),
    col("역명").alias("station_name"),
    col("승차총승객수").alias("ride_passenger"),
    col("하차총승객수").alias("alight_passenger"),
    col("date").cast("string").alias("ride_date"),
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
