-- 100-not_my_genres.sql

SELECT `tv_genres`.`name`
  FROM `tv_genres`
 WHERE `tv_genres`.`id` NOT IN
       (SELECT `tv_show_genres`.`genre_id`
          FROM `tv_show_genres`
         JOIN `tv_shows` ON `tv_shows`.`id` = `tv_show_genres`.`tv_show_id`
         WHERE `tv_shows`.`title` = "Dexter")
 ORDER BY `tv_genres`.`name`;
