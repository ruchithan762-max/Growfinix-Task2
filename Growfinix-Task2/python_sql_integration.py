
import pandas as pd
from sqlalchemy import create_engine, text

# Connect to the existing SQLite database
engine = create_engine("sqlite:///ipl.db")

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
    # Execute SQL and load the results into a pandas DataFrame
    with engine.connect() as connection:
        df = pd.read_sql(text(query), connection)

    print("KKR Season-wise Performance")
    print(df.to_string(index=False))

    # Export the extracted data
    df.to_csv("kkr_sqlalchemy_report.csv", index=False)

    print("\nReport saved: kkr_sqlalchemy_report.csv")

except Exception as error:
    print("Error:", error)

finally:
    engine.dispose()
