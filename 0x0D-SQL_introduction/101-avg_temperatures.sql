-- Select the city and calculate the average temperature for each city
SELECT city, AVG(temperature) AS avg_temp
-- From the table that stores temperature data
FROM temperatures
-- Group the results by city, so the average is calculated for each city
GROUP BY city
-- Order the results by the average temperature in descending order
ORDER BY avg_temp DESC;
