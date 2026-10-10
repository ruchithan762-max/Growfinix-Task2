SELECT COUNT(*) AS total_kkr_matches
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR';

SELECT COUNT(*) AS total_kkr_wins
FROM matches
WHERE winner = 'KKR';
