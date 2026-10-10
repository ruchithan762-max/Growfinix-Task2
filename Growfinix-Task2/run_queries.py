
import sqlite3

DATABASE = "ipl.db"
SQL_FILE = "task2_queries.sql"

conn = None

try:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Read the complete SQL file
    with open(SQL_FILE, "r", encoding="utf-8") as file:
        sql_script = file.read()

    print("=" * 60)
    print("GROWFINIX TASK 2 - IPL SQL ANALYSIS")
    print("=" * 60)

    # Execute the SQL script
    cursor.executescript(sql_script)
    conn.commit()

    print("\nSQL script executed successfully!")

    # 1. KKR season-wise performance
    print("\n1. KKR SEASON-WISE PERFORMANCE")
    print("-" * 60)

    cursor.execute("""
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
        ORDER BY season
    """)

    print("Season | Matches | Wins | Win Percentage")

    for row in cursor.fetchall():
        print(row)

    # 2. KKR stadium-wise performance
    print("\n2. KKR STADIUM-WISE PERFORMANCE")
    print("-" * 60)

    cursor.execute("""
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
        ORDER BY win_percentage DESC
    """)

    print("Venue | Matches | Wins | Win Percentage")

    for row in cursor.fetchall():
        print(row)

    # 3. Advanced SQL analysis using window functions
    print("\n3. KKR ADVANCED SQL ANALYSIS")
    print("-" * 60)

    cursor.execute("""
        WITH season_wins AS (
            SELECT
                season,
                COUNT(*) AS total_matches,
                SUM(
                    CASE WHEN winner = 'KKR' THEN 1 ELSE 0 END
                ) AS wins
            FROM matches
            WHERE team1 = 'KKR' OR team2 = 'KKR'
            GROUP BY season
        )
        SELECT
            season,
            total_matches,
            wins,
            ROUND(100.0 * wins / total_matches, 2) AS win_percentage,
            RANK() OVER (ORDER BY wins DESC) AS season_rank,
            LAG(wins) OVER (ORDER BY season) AS previous_season_wins,
            LEAD(wins) OVER (ORDER BY season) AS next_season_wins
        FROM season_wins
        ORDER BY season
    """)

    print(
        "Season | Matches | Wins | Win % | Rank | "
        "Previous Wins | Next Wins"
    )

    for row in cursor.fetchall():
        print(row)

    print("\nAnalysis completed successfully!")

except (sqlite3.Error, OSError) as error:
    print("\nError:", error)

finally:
    if conn is not None:
        conn.close()
