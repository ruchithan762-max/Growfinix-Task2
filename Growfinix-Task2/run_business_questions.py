
import sqlite3

questions = [
    (
        "Q1. Total matches",
        "SELECT COUNT(*) AS total_matches FROM matches"
    ),
    (
        "Q2. Matches involving KKR",
        """
        SELECT COUNT(*) AS kkr_matches
        FROM matches
        WHERE team1 = 'KKR' OR team2 = 'KKR'
        """
    ),
    (
        "Q3. Total KKR wins",
        """
        SELECT COUNT(*) AS kkr_wins
        FROM matches
        WHERE winner = 'KKR'
        """
    ),
    (
        "Q4. KKR win percentage",
        """
        SELECT
            COUNT(CASE WHEN winner = 'KKR' THEN 1 END) AS wins,
            COUNT(*) AS matches_played,
            ROUND(
                100.0 * COUNT(CASE WHEN winner = 'KKR' THEN 1 END)
                / NULLIF(COUNT(*), 0), 2
            ) AS win_percentage
        FROM matches
        WHERE team1 = 'KKR' OR team2 = 'KKR'
        """
    ),
    (
        "Q5. Matches per season",
        """
        SELECT season, COUNT(*) AS total_matches
        FROM matches
        GROUP BY season
        ORDER BY season
        """
    ),
    (
        "Q6. KKR wins per season",
        """
        SELECT season, COUNT(*) AS kkr_wins
        FROM matches
        WHERE winner = 'KKR'
        GROUP BY season
        ORDER BY season
        """
    ),
    (
        "Q7. Matches won by each team",
        """
        SELECT winner, COUNT(*) AS total_wins
        FROM matches
        WHERE winner IS NOT NULL
        GROUP BY winner
        ORDER BY total_wins DESC
        """
    ),
    (
        "Q8. Top 5 venues",
        """
        SELECT venue, COUNT(*) AS total_matches
        FROM matches
        GROUP BY venue
        ORDER BY total_matches DESC
        LIMIT 5
        """
    ),
    (
        "Q9. Top 5 cities",
        """
        SELECT city, COUNT(*) AS total_matches
        FROM matches
        GROUP BY city
        ORDER BY total_matches DESC
        LIMIT 5
        """
    ),
    (
        "Q10. Top 3 seasons for KKR wins",
        """
        SELECT season, COUNT(*) AS kkr_wins
        FROM matches
        WHERE winner = 'KKR'
        GROUP BY season
        ORDER BY kkr_wins DESC
        LIMIT 3
        """
    )
]

conn = None

try:
    conn = sqlite3.connect("ipl.db")

    with open(
        "business_questions_results.txt",
        "w",
        encoding="utf-8"
    ) as report:

        for title, query in questions:
            cursor = conn.execute(query)
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            print("\n" + "=" * 50)
            print(title)
            print("-" * 50)
            print(" | ".join(columns))

            report.write(title + "\n")
            report.write(" | ".join(columns) + "\n")

            for row in rows:
                values = [str(value) for value in row]
                print(" | ".join(values))
                report.write(" | ".join(values) + "\n")

            report.write("\n")

    print("\nAll questions executed successfully!")
    print("Results saved in business_questions_results.txt")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if conn is not None:
        conn.close()
