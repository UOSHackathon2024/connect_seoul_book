CREATE DATABASE hackathon;
USE hackathon;

CREATE TABLE library (
    library_id     integer AUTO_INCREMENT PRIMARY KEY,
    library_name   VARCHAR(100) NOT NULL,
    is_connected     BOOL,
    longitude       REAL,
    latitude        REAL
) CHARSET=utf8;

CREATE USER crawler IDENTIFIED BY 'crawler';

GRANT INSERT, SELECT ON hackathon.library          TO 'crawler';