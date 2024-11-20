-- 102-rating_shows.sql

SELECT `tv_shows`.`title`, SUM(`ratings`.`rating`) AS `rating`
  FROM `tv_shows`
 JOIN `ratings` ON `tv_shows`.`id` = `ratings`.`tv_show_id`
 GROUP BY `tv_shows`.`title`
 ORDER BY `rating` DESC;
