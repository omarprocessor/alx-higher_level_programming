-- Script to print the full description of first_table
SELECT TABLE_NAME, CREATE_TABLE 
FROM information_schema.tables 
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
