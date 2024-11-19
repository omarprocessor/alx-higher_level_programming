-- Select the city and calculate the average temperature for each city during July and August
USE `hbtn_0c_0`
SELECT city, AVG(temperature) AS avg_temp
-- From the table that stores temperature data
FROM temperatures
-- Where the month is July (7) or August (8)
WHERE MONTH(date) IN (7, 8)
-- Group by city to calculate the average for each city
GROUP BY city
-- Order by the calculated average temperature in descending order
ORDER BY avg_temp DESC
-- Limit the results to the top 3 cities
LIMIT 3;
