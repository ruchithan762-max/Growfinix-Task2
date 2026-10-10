
import sqlite3
import csv

conn = sqlite3.connect("ipl.db")
cursor = conn.cursor()

query = """
SELECT
    season,
    COUNT(*) AS total_matches,
    SUM(CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END) AS wins
FROM matches
WHERE team1 = 'KKR' OR team2 = 'KKR'
GROUP BY season
ORDER BY season
"""

cursor.execute(query)
rows = cursor.fetchall()

with open("kkr_season_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Season", "Total Matches", "KKR Wins", "Win Percentage"])

    for season, matches, wins in rows:
        percentage = (wins / matches * 100) if matches else 0
        writer.writerow([season, matches, wins, round(percentage, 2)])

conn.close()

print("Report generated successfully: kkr_season_report.csv")
