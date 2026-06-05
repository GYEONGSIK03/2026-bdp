#!/bin/bash

cd ~/2026-bdp

echo "================================="
echo "MJU Bus Data Pipeline Start"
echo "================================="

echo ""
echo "[1/5] Collect API Data..."

python3.6 collect_data.py

if [ $? -ne 0 ]; then
    echo "API Collection Failed"
    exit 1
fi

echo ""
echo "[2/5] Spark Preprocessing..."

spark-submit preprocess.py

if [ $? -ne 0 ]; then
    echo "Spark Preprocessing Failed"
    exit 1
fi

echo ""
echo "[3/5] Hive Analysis..."

beeline \
-u "jdbc:hive2://sandbox-hdp.hortonworks.com:10000" \
-n hive \
-f hive_queries.sql

if [ $? -ne 0 ]; then
    echo "Hive Analysis Failed"
    exit 1
fi

echo ""
echo "[4/5] Export Analysis Result..."

mkdir -p analysis_result

beeline \
-u "jdbc:hive2://sandbox-hdp.hortonworks.com:10000" \
-n hive \
--outputformat=csv2 \
-e "
SELECT month,
SUM(ride_passenger) AS total_ride
FROM mju_bus
GROUP BY month
ORDER BY month;
" > analysis_result/monthly.csv

beeline \
-u "jdbc:hive2://sandbox-hdp.hortonworks.com:10000" \
-n hive \
--outputformat=csv2 \
-e "
SELECT day_of_week,
SUM(ride_passenger) AS total_ride
FROM mju_bus
GROUP BY day_of_week
ORDER BY day_of_week;
" > analysis_result/dayofweek.csv

beeline \
-u "jdbc:hive2://sandbox-hdp.hortonworks.com:10000" \
-n hive \
--outputformat=csv2 \
-e "
SELECT route_id,
SUM(ride_passenger) AS total_ride
FROM mju_bus
GROUP BY route_id
ORDER BY total_ride DESC
LIMIT 10;
" > analysis_result/routes.csv

beeline \
-u "jdbc:hive2://sandbox-hdp.hortonworks.com:10000" \
-n hive \
--outputformat=csv2 \
-e "
SELECT station_ars_id,
SUM(ride_passenger) AS ride,
SUM(alight_passenger) AS alight
FROM mju_bus
GROUP BY station_ars_id;
" > analysis_result/station.csv

echo ""
echo "[5/5] Visualization..."

python3.6 visualization.py

if [ $? -ne 0 ]; then
    echo "Visualization Failed"
    exit 1
fi

echo ""
echo "================================="
echo "Pipeline Finished"
echo "================================="
