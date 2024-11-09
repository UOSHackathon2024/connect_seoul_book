CREATE DATABASE hackathon;
USE hackathon;

CREATE TABLE library (
    library_id          integer AUTO_INCREMENT PRIMARY KEY,
    library_name        VARCHAR(100) NOT NULL,
    is_connected        BOOL,
    longitude           REAL,
    latitude            REAL,
    start_time_day      TIME,
    end_time_day        TIME,
    start_time_weekend  TIME,
    end_time_weekend    TIME,
    start_time_holiday  TIME,
    end_time_holiday    TIME
) CHARSET=utf8;

CREATE TABLE program (
    program_id          integer AUTO_INCREMENT PRIMARY KEY,
    program_name        VARCHAR(255) NOT NULL,
    library_name        VARCHAR(255),
    start_program       DATETIME,
    end_program         DATETIME,
    accept_start        DATETIME,
    accept_end          DATETIME,
    client_type         VARCHAR(255),
    category            VARCHAR(255),
    program_place       VARCHAR(255),
    program_instructor  VARCHAR(255),
    image_url           VARCHAR(255),
    program_url         VARCHAR(255)
)CHARSET=utf8;


CREATE USER crawler IDENTIFIED BY 'crawler';
GRANT INSERT, SELECT, DELETE ON hackathon.library          TO 'crawler';
GRANT INSERT, SELECT, DELETE ON hackathon.program          TO 'crawler';