
import sqlite3
import csv

conn = sqlite3.connect("ipl.db")
cursor = conn.cursor()

query = """
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
"""

try:
    cursor.execute(query)
    rows = cursor.fetchall()

    with open("combined_ipl_report.csv", "w", newline="",
              encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Season",
            "Total KKR Matches",
            "KKR Wins",
            "Win Percentage"
        ])
        writer.writerows(rows)

    print("Combined IPL report created successfully!")

    for row in rows:
        print(row)

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    conn.close()
