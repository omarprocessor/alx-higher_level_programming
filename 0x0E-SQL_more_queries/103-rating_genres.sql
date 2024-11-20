-- 103-rating_genres.sql

SELECT `tv_genres`.`name`, SUM(`ratings`.`rating`) AS `rating`
  FROM `tv_genres`
 JOIN `tv_show_genres` ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
 JOIN `ratings` ON `ratings`.`tv_show_id` = `tv_show_genres`.`tv_show_id`
 GROUP BY `tv_genres`.`name`
 ORDER BY `rating` DESC;
