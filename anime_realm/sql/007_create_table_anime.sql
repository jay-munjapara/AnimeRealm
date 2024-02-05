-- jm2527 11/26/2023
CREATE TABLE IS601_anime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    anime_id INT DEFAULT NULL,
    name VARCHAR(255) NOT NULL,
    studios VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) NOT NULL,
    episodes VARCHAR(20),
    aired VARCHAR(50),
    duration VARCHAR(20),
    rating VARCHAR(50) NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY `unique_name_status_rating` (`name`, `status`, `rating`)
);
