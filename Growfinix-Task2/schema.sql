
CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY,
    season INTEGER,
    team1 TEXT,
    team2 TEXT,
    winner TEXT,
    venue TEXT,
    city TEXT
);

SELECT name
FROM sqlite_master
WHERE type = 'table';
