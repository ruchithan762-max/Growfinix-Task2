
import sqlite3

connection = sqlite3.connect("ipl.db")
cursor = connection.cursor()

cursor.execute("""
SELECT
    season,
    COUNT(*) AS total_matches,
    SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END) AS kkr_wins
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR'
GROUP BY season
ORDER BY season;
""")

print("Season-wise KKR Performance")
print("---------------------------")

for row in cursor.fetchall():
    season, total_matches, wins = row
    win_percentage = round(wins * 100 / total_matches, 2)
    print(
        f"Season: {season} | Matches: {total_matches} "
        f"| Wins: {wins} | Win %: {win_percentage}%"
    )

connection.close()

import sqlite3

conn = sqlite3.connect("ipl.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    venue,
    COUNT(*) AS total_matches,
    SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END) AS kkr_wins
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR'
GROUP BY venue
ORDER BY kkr_wins DESC
""")

print("KKR Stadium-wise Results:")
for row in cursor.fetchall():
    print(row)

conn.close()

