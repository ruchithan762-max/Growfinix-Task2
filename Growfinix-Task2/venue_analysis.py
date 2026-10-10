
import sqlite3
import csv

conn = sqlite3.connect("ipl.db")
cursor = conn.cursor()

query = """
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
ORDER BY kkr_wins DESC, total_matches DESC;
"""

try:
    cursor.execute(query)
    results = cursor.fetchall()

    print("Venue-wise KKR Performance")
    print("-" * 60)

    for row in results:
        print(row)

    with open("venue_performance_report.csv", "w", newline="",
              encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Venue",
            "Total KKR Matches",
            "KKR Wins",
            "Win Percentage"
        ])
        writer.writerows(results)

    print("\nReport created: venue_performance_report.csv")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    conn.close()
