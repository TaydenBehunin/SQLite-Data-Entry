import sqlite3


def connect_to_sqlite(db_name='demo_data.sqlite3'):
    return sqlite3.connect('demo_data.sqlite3')


create_table = """
CREATE TABLE IF NOT EXISTS demo(
    S varchar(30) NOT NULL,
    X INT NOT NULL,
    Y INT NOT NULL
)
"""

insert_values = """INSERT INTO demo (S, X, Y)
VALUES
    ("'g'", 3, 9),
    ("'v'", 5, 7),
    ("'f'", 8, 7);
"""

row_count_query = """
SELECT COUNT(*)
FROM demo
"""

xy_at_least_5_query = """
SELECT COUNT(*)
FROM demo
WHERE X >= 5 AND Y >= 5
"""

unique_y_query = """
SELECT COUNT(DISTINCT Y)
FROM demo
"""


def execute_query(conn, query):
    # Make a Cursor (a middle man)
    cursor = conn.cursor()
    # Execute our query
    cursor.execute(query)
    # Commit
    conn.commit()
    # Pull Results
    results = cursor.fetchall()
    return results


conn = connect_to_sqlite()
execute_query(conn, create_table)
execute_query(conn, insert_values)
row_count = execute_query(conn, row_count_query)
xy_at_least_5 = execute_query(conn, xy_at_least_5_query)
unique_y = execute_query(conn, unique_y_query)

print(row_count, xy_at_least_5, unique_y)
