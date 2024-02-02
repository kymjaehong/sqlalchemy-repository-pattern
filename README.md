# Hello, world!

## Reference
https://praciano.com.br/fastapi-and-async-sqlalchemy-20-with-pytest-done-right.html
https://www.youtube.com/watch?v=9ymRLDfnDKg&list=LL&index=1

## Database
```
CREATE DATABASE IF NOT EXISTS `todo` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `todo`;

CREATE TABLE `todo`.`user` (
  `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `account_id` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `phone_number` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)
ENGINE = InnoDB;

CREATE TABLE `todo`.`plate` (
  `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `content` VARCHAR(255) NOT NULL,
  `is_complete` BOOLEAN NOT NULL DEFAULT FALSE,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT UNSIGNED NOT NULL,
  FOREIGN KEY (`user_id`) REFERENCES `todo`.`user` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE)
ENGINE = InnoDB;
```
