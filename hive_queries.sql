
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
