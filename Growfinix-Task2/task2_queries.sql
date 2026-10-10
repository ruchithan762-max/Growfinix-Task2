
-- GROWFINIX TASK 2: IPL SQL ANALYSIS

-- 1. Display all matches
SELECT *
FROM matches;

-- 2. Display KKR matches
SELECT *
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR';

-- 3. Season-wise match count
SELECT season, COUNT(*) AS total_matches
FROM matches
GROUP BY season
ORDER BY season;

-- 4. KKR overall performance
SELECT
    COUNT(*) AS total_matches,
    SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END) AS kkr_wins,
    ROUND(
        100.0 * SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS win_percentage
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR';

-- 5. KKR season-wise performance
SELECT
    season,
    COUNT(*) AS total_matches,
    SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END) AS kkr_wins,
    ROUND(
        100.0 * SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS win_percentage
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR'
GROUP BY season
ORDER BY season;

-- 6. KKR stadium-wise performance
SELECT
    venue,
    COUNT(*) AS total_matches,
    SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END) AS kkr_wins,
    ROUND(
        100.0 * SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS win_percentage
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR'
GROUP BY venue
ORDER BY win_percentage DESC;

-- 7. Rank stadiums by KKR win percentage
WITH stadium_stats AS (
    SELECT
        venue,
        COUNT(*) AS total_matches,
        SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END) AS kkr_wins
    FROM matches
    WHERE team1 = 'KKR' OR team2 = 'KKR'
    GROUP BY venue
)
SELECT
    venue,
    total_matches,
    kkr_wins,
    ROUND(100.0 * kkr_wins / total_matches, 2) AS win_percentage,
    RANK() OVER (
        ORDER BY 1.0 * kkr_wins / total_matches DESC
    ) AS stadium_rank
FROM stadium_stats
ORDER BY win_percentage DESC;

-- 8. Rank seasons by KKR wins
WITH season_stats AS (
    SELECT
        season,
        SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END) AS kkr_wins
    FROM matches
    WHERE team1 = 'KKR' OR team2 = 'KKR'
    GROUP BY season
)
SELECT
    season,
    kkr_wins,
    RANK() OVER (ORDER BY kkr_wins DESC) AS season_rank
FROM season_stats
ORDER BY season;

-- 9. Compare wins across seasons
WITH season_stats AS (
    SELECT
        season,
        SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END) AS kkr_wins
    FROM matches
    WHERE team1 = 'KKR' OR team2 = 'KKR'
    GROUP BY season
)
SELECT
    season,
    kkr_wins,
    LAG(kkr_wins) OVER (ORDER BY season) AS previous_season_wins,
    LEAD(kkr_wins) OVER (ORDER BY season) AS next_season_wins
FROM season_stats
ORDER BY season;

-- 10. Show seasons with at least two matches
SELECT season, COUNT(*) AS total_matches
FROM matches
GROUP BY season
HAVING COUNT(*) >= 2
ORDER BY season;
