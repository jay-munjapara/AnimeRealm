-- # jm2527 12/09/2023

ALTER TABLE IS601_anime
ADD UNIQUE KEY `unique_name_status_rating` (`name`, `status`, `rating`);
