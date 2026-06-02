
-- Monthly Analysis
SELECT
    month,
    SUM(ride_passenger) AS total_ride
FROM mju_bus
GROUP BY month
ORDER BY month;

-- Day Of Week Analysis
SELECT
    day_of_week,
    SUM(ride_passenger) AS total_ride
FROM mju_bus
GROUP BY day_of_week
ORDER BY day_of_week;

-- Top Bus Routes
SELECT
    route_id,
    SUM(ride_passenger) AS total_ride
FROM mju_bus
GROUP BY route_id
ORDER BY total_ride DESC
LIMIT 10;

-- Station Direction Analysis
-- Compare boarding and alighting passengers by station

SELECT
    station_ars_id,
    SUM(ride_passenger) AS ride,
    SUM(alight_passenger) AS alight
FROM mju_bus
GROUP BY station_ars_id;
