CREATE TABLE users (
    user_id uuid DEFAULT gen_random_uuid(),
    user_name VARCHAR(100) NOT NULL,
    password TEXT NOT NULL,
    PRIMARY KEY (user_id)
);
-- created users table. will store a hash of all the users data
-- allowing user's name and password to be 100 characters long due to it being stored as encrypted hash

CREATE TABLE markets(
    market_id uuid DEFAULT gen_random_uuid(),
    market_name  VARCHAR(100) NOT NULL,
    region_name VARCHAR(100) NOT NULL,
    market_availability BOOLEAN NOT NULL,
    PRIMARY KEY (market_id)
);
-- creating market table that stores data about specific market


CREATE TABLE assets (
    asset_id uuid DEFAULT gen_random_uuid(),
    market_id uuid,
    asset_name VARCHAR(100) NOT NULL,
    asset_type VARCHAR(100) NOT NULL,
    asset_value INT NOT NULL,
    asset_price_change FLOAT NOT NULL,
    asset_vol bigint NOT NULL,
    PRIMARY KEY (asset_id),
    FOREIGN KEY( market_id) REFERENCES markets(market_id)
);

-- creating table storing all the relevant data to assets


CREATE TABLE news (
    news_id uuid DEFAULT gen_random_uuid(),
    market_id uuid,
    news_headline VARCHAR(255)NOT NULL,
    news_content TEXT NOT NULL,
    news_publishing_date DATE,
    PRIMARY KEY (news_id),
    FOREIGN KEY (market_id) REFERENCES markets(market_id)
);

--creating table storing news, bigint is used for news_id as a huge volume of articles will be stored
-- foreign key market_id links it to a specific region making it easier to categorise


CREATE TABLE favourite_assets (
    user_asset_id uuid DEFAULT gen_random_uuid(),
    user_id uuid,
    asset_id uuid,
    PRIMARY KEY (user_asset_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id)
);

-- creating unique combination of user id and asset id so each preference has a specific identifier

