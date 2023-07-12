import sqlite3

try:
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    # cursor.execute("""CREATE TABLE employee
    #               (ID integer primary key , name text , email text , salary real )
    #                """)
    # insert into database
    # cursor.execute("""INSERT INTO employee(name,email,salary)
    #                 VALUES("tejal","tejal8079@gmail.com",1000)""")
    # print(cursor.execute("""SELECT* FROM employee""").fetchone())
    # connection.commit()
    # connection.close()

    rows = cursor.execute("""SELECT* FROM employee""")
    for row in rows:
        print("id = " + str(row[0]))
        print("name = " + (row[1]))
        print("email = " + (row[2]))
        print("salary = " + str(row[3]))

        rows = cursor.execute("""SELECT id, name FROM employee""")
        for row in rows:
            print("id = " + str(row[0]))
            print("name = " + (row[1]))
            # print("email = " + (row[2]))
            # print("salary = " + str(row[3]))

    # delete
    # cursor.execute("DELETE FROM employee")

    name = "peter"
    salary = 5000

    # update
    # cursor.execute("UPDATE employee SET name = '%s',salary = '%d'" % (name, salary))
    # cursor.execute("UPDATE employee SET name =' Anish ' ,email = 'anish8079@gmail.com' ,salary = 2000 WHERE id = 2")
    cursor.execute("UPDATE employee SET name = ? ,salary = ? " ,(name, salary))

    # where clause
    rows = cursor.execute("""SELECT* FROM employee where id = 2""")
    for row in rows:
        print("id = " + str(row[0]))
        print("name = " + (row[1]))
        print("email = " + (row[2]))
        print("salary = " + str(row[3]))

except Exception as e:
    print(e)