
import sqlite3
import csv

conn = sqlite3.connect("ipl.db")
cursor = conn.cursor()

query = """
SELECT
    team,
    COUNT(*) AS total_matches,
    SUM(win) AS total_wins,
    ROUND(100.0 * SUM(win) / COUNT(*), 2) AS win_percentage
FROM (
    SELECT team1 AS team,
           CASE WHEN winner = team1 THEN 1 ELSE 0 END AS win
    FROM matches

    UNION ALL

    SELECT team2 AS team,
           CASE WHEN winner = team2 THEN 1 ELSE 0 END AS win
    FROM matches
)
GROUP BY team
ORDER BY total_wins DESC;
"""

try:
    cursor.execute(query)
    results = cursor.fetchall()

    print("Team-wise IPL Performance")
    print("-" * 60)

    for row in results:
        print(row)

    with open("team_performance_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Team",
            "Total Matches",
            "Total Wins",
            "Win Percentage"
        ])
        writer.writerows(results)

    print("\nReport created: team_performance_report.csv")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    conn.close()
