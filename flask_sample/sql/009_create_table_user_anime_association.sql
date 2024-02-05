CREATE TABLE IS601_Anime_Watchlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    anime_id INT NOT NULL,
    user_id INT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY `unique_anime_user` (`anime_id`, `user_id`),
    FOREIGN KEY (anime_id) REFERENCES IS601_anime(id),
    FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
);