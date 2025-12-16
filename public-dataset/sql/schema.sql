-- CLEAN DATASET
CREATE TABLE universities (
    university_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    country TEXT
);

CREATE TABLE rankings (
    ranking_id SERIAL PRIMARY KEY,
    university_id INT NOT NULL,
    year INT,
    rank INT,
    score NUMERIC,
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);

-- MESSY DATASET
CREATE TABLE restaurants (
    restaurant_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    borough TEXT
);

CREATE TABLE inspections (
    inspection_id SERIAL PRIMARY KEY,
    restaurant_id INT NOT NULL,
    inspection_date DATE,
    score INT,
    grade TEXT,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);
