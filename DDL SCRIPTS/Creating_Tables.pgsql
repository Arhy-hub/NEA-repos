CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(100),
    password VARCHAR(100)
);
-- created users table. will store a hash of all the users data
-- allowing user's name and password to be 100 characters long due to it being stored as encrypted hash

CREATE TABLE assets (
    asset_id INT PRIMARY KEY,
    market_id INT,
    asset_name VARCHAR(255),
    asset_type VARCHAR (255),
    asset_value INT,
    asset_price_change INT,
    FOREIGN KEY( market_id) REFERENCES markets(market_id)
);

-- creating table storing all the relevant data to assets


CREATE TABLE markets(
    market_id INT PRIMARY KEY,
    market_name varchar(255),
    region_name varchar(255),
    market_availability BOOLEAN
);
-- creating market table that stores data about specific market

CREATE TABLE news (
    news_id BIGINT PRIMARY KEY,
    market_id INT,
    news_headline varchar(255),
    news_content varchar(255),
    news_publishing_date DATE,
    FOREIGN KEY (market_id) REFERENCES markets(market_id)
);

--creating table storing news, bigint is used for news_id as a huge volume of articles will be stored
-- foreign key market_id links it to a specific region making it easier to categorise


CREATE TABLE favourite_assets (
    user_asset_id INT PRIMARY KEY,
    user_id INT,
    asset_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id)
);

-- creating unique combination of user id and asset id so each preference has a specific identifier
