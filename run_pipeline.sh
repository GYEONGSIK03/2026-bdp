#!/bin/bash

cd ~/2026-bdp

echo "================================="
echo "MJU Bus Data Pipeline Start"
echo "================================="

echo ""
echo "[1/3] Data Collection..."

python3.6 collect_data.py

echo ""
echo "[2/3] Spark Preprocessing..."

spark-submit preprocess.py

echo ""
echo "[3/3] Hive Analysis..."

beeline -u "jdbc:hive2://sandbox-hdp.hortonworks.com:10000" \
-n hive \
-f hive_queries.sql

echo ""
echo "================================="
echo "Pipeline Finished"
echo "================================="
