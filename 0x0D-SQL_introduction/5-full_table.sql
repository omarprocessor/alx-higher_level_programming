-- Script to print the full description of first_table
SELECT TABLE_NAME, CREATE_TABLE 
FROM information_schema.tables 
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';
