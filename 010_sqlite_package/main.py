import sqlite3

connection = sqlite3.connect("northwind.db")

cur = connection.cursor()
#
#
# response_from_table = cur.execute(
#     "SELECT * FROM Employees"
# )
#
# # print()
#
# for emp in response_from_table.fetchall():
#     print(emp)
#     print("++++++++++++++++++++++++++++++++++++++++++")

first_name = input("what is your first name? ")
last_name = input("what is your last name? ")

cur.execute(
    f"""
    INSERT INTO Employees(EmployeeID, LastName, FirstName)
    VALUES(10, "{last_name}", "{first_name}")
    """
)

connection.commit()
connection.close()

