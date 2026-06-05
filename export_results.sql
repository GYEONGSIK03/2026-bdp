INSERT OVERWRITE LOCAL DIRECTORY 'analysis_result/monthly'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT
    month,
    SUM(ride_passenger)
FROM mju_bus
GROUP BY month
ORDER BY month;

INSERT OVERWRITE LOCAL DIRECTORY 'analysis_result/dayofweek'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT
    day_of_week,
    SUM(ride_passenger)
FROM mju_bus
GROUP BY day_of_week
ORDER BY day_of_week;

INSERT OVERWRITE LOCAL DIRECTORY 'analysis_result/routes'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT
    route_id,
    SUM(ride_passenger)
FROM mju_bus
GROUP BY route_id
ORDER BY SUM(ride_passenger) DESC
LIMIT 10;

INSERT OVERWRITE LOCAL DIRECTORY 'analysis_result/station'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT
    station_ars_id,
    SUM(ride_passenger),
    SUM(alight_passenger)
FROM mju_bus
GROUP BY station_ars_id;
