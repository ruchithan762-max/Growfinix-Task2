
-- Q1. How many matches are in the dataset?
SELECT COUNT(*) AS total_matches
FROM matches;

-- Q2. How many matches did KKR play?
SELECT COUNT(*) AS kkr_matches
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR';

-- Q3. How many matches did KKR win?
SELECT COUNT(*) AS kkr_wins
FROM matches
WHERE winner = 'KKR';

-- Q4. What is KKR's overall win percentage?
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END)
        / COUNT(*), 2
    ) AS kkr_win_percentage
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR';

-- Q5. How many matches were played in each season?
SELECT season, COUNT(*) AS total_matches
FROM matches
GROUP BY season
ORDER BY season;

-- Q6. How many matches did KKR win in each season?
SELECT season, COUNT(*) AS kkr_wins
FROM matches
WHERE winner = 'KKR'
GROUP BY season
ORDER BY season;

-- Q7. Which teams appear most often as winners?
SELECT winner, COUNT(*) AS wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY wins DESC;

-- Q8. Which venues hosted the most matches?
SELECT venue, COUNT(*) AS total_matches
FROM matches
GROUP BY venue
ORDER BY total_matches DESC
LIMIT 5;

-- Q9. Which cities hosted the most matches?
SELECT city, COUNT(*) AS total_matches
FROM matches
WHERE city IS NOT NULL
GROUP BY city
ORDER BY total_matches DESC
LIMIT 5;

-- Q10. Which seasons had the highest number of KKR wins?
SELECT season, COUNT(*) AS kkr_wins
FROM matches
WHERE winner = 'KKR'
GROUP BY season
ORDER BY kkr_wins DESC, season ASC
LIMIT 3;
