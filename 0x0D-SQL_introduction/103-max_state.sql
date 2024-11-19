-- Select the state and the maximum temperature for each state
SELECT state, MAX(temperature) AS max_temp
-- From the temperatures table
FROM temperatures
-- Group by state to find the maximum temperature per state
GROUP BY state
-- Order the results by state name in ascending order
ORDER BY state ASC;
