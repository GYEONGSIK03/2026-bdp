o "================================="
echo "MJU Bus Data Pipeline Start"
echo "================================="

echo ""
echo "[1/4] Collect API Data..."

python3.6 collect_data.py

if [ $? -ne 0 ]; then
    echo "API Collection Failed"
    exit 1
fi

echo ""
echo "[2/4] Spark Preprocessing..."

spark-submit preprocess.py

if [ $? -ne 0 ]; then
    echo "Spark Preprocessing Failed"
    exit 1
fi

echo ""
echo "[3/4] Hive Analysis..."

beeline \
-u "jdbc:hive2://sandbox-hdp.hortonworks.com:10000" \
-n hive \
-f hive_queries.sql

if [ $? -ne 0 ]; then
    echo "Hive Analysis Failed"
    exit 1
fi

echo ""
echo "[4/4] Visualization..."

python3.6 visualization.py

if [ $? -ne 0 ]; then
    echo "Visualization Failed"
    exit 1
fi

echo ""
echo "================================="
echo "Pipeline Finished"
echo "================================="
