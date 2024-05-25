-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_value
FROM temperatures
WHERE temperatures.month = 7 OR temperatures.month = 8
GROUP BY city
ORDER BY avg_value DESC
LIMIT 3;
