import sqlite3


def connect_to_sqlite(db_name='northwind_small.sqlite3'):
    return sqlite3.connect('northwind_small.sqlite3')


expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""

avg_hire_age = """
SELECT avg(HireDate - BirthDate)
FROM Employee
"""

ten_most_expensive = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product
LEFT JOIN Supplier
ON Product.SupplierId= Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""

largest_category = """
SELECT c.CategoryName, COUNT(DISTINCT p.Id)
FROM Category c, Product p
WHERE c.Id = p.CategoryId
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
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
execute_query(conn, expensive_items)
# 38	Côte de Blaye	18	1	12 - 75 cl bottles	""263.5"""	17	0	15	0
# 29	Thüringer Rostbratwurst	12	6	50 bags x 30 sausgs.	""123.79""	0	0	0	1
# 9	Mishi Kobe Niku	4	6	18 - 500 g pkgs.	""97"""	29	0	0	1
# 20	Sir Rodney's Marmalade	8	3	30 gift boxes	""81"""	40	0	0	0
# 18	Carnarvon Tigers	7	8	16 kg pkg.	""62.5"""	42	0	0	0
# 59	Raclette Courdavault	28	4	5 kg pkg.	""55"""	79	0	0	0
# 51	Manjimup Dried Apples	24	7	50 - 300 g pkgs.	""53"""	20	0	10	0
# 62	Tarte au sucre	29	3	48 pies	""49.3"""	17	0	0	0
# 43	Ipoh Coffee	20	1	16 - 500 g tins	""46"""	17	10	25	0
# 28	Rössle Sauerkraut	12	7	25 - 825 g cans	""45.6"""	26	0	0	1
execute_query(conn, avg_hire_age)
# 37.2222222222222
(execute_query(conn, ten_most_expensive))
# Thüringer Rostbratwurst	123.79	Forêts d'érables
# Mishi Kobe Niku	97	PB Knäckebröd AB
# Sir Rodney's Marmalade	81	Leka Trading
# Carnarvon Tigers	62.5	Aux joyeux ecclésiastiques
# Rössle Sauerkraut	45.6	Gai pâturage
# Schoggi Schokolade	43.9	Escargots Nouveaux
# Northwoods Cranberry Sauce	40	Specialty Biscuits, Ltd.
# Alice Mutton	39	Svensk Sjöföda AB
# Queso Manchego La Pastora	38	Plutzer Lebensmittelgroßmärkte AG
(execute_query(conn, largest_category))
# Confections
