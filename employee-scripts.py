from employee import Employee

# CREATE TABLE IF NOT EXISTS employees (
#     employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name INTEGER NOT NULL,
#     salary REAL NOT NULL,
#     salary_history BLOB,
#     vacation_hours REAL NOT NULL,
#     bonus REAL NOT NULL,
#     manager_id INTEGER,
#     is_hr INTEGER NOT NULL,
#     is_admin INTEGER NOT NULL
# );

# INSERT INTO employees (employee_id, name, salary, salary_history, vacation_hours, bonus, manager_id,
#                        is_hr, is_admin)
# VALUES (0, "Samwise Gamgee", 1000, '[]', 20, 100, null, 0, 0);

frodo = Employee('Frodo Baggins')
str(frodo)