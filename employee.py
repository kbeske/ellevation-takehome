from sqlite_functions import connect_to_database, execute_query, execute_read_query

class Employee:
    # employees have salary, salary history, vacation balance, and annual bonus
    # I am also adding an employee id, first and last names, manager id, a HR boolean
    #    and an admin boolean
    # I am assuming all managers, hr personnel, and admins are employees
    def __init__(self, name, salary=0, salary_history=[], vacation_hours=0,
            bonus=0, manager_id=None, is_hr=False, is_admin=False):
        self.name = name # string
        self.salary = salary # number
        self.salary_history = salary_history # list
        self.vacation_hours = vacation_hours # number of hours
        self.bonus = bonus # number
        self.manager_id = manager_id # number, can be none in case you're adding the CEO or something
        self.is_hr = is_hr # boolean
        self.is_admin = is_admin # boolean

        print("Hello")
        
        insert_query = f"""
        INSERT INTO
            employees (name, salary, salary_history, vacation_hours, bonus, manager_id,
                       is_hr, is_admin)
        VALUES
            (${self.name}, ${self.salary}, '${self.salary_history}', ${self.vacation_hours},
             ${self.bonus}, ${self.manager_id}, ${1 if self.is_hr else 0}, ${1 if self.is_admin else 0});
        """

        get_id_query = "SELECT last_insert_rowid()"

        connection = connect_to_database('hr-app.db')
        execute_query(connection, insert_query)
        print("Test")
        self.employee_id = execute_read_query(connection, get_id_query)
        print("Test 2")
        connection.close()

    # two ways to add employees? one by doing __init__() and the other with an INSERT?

    # make a new AuthenticationSystem class that takes in the person's employee id at init and then
    #    has methods that check if they have the permissions

    # for all below methods:
    #    - need to add sql UPDATEs
    #    - add some sort of authentication - should every method also take in an id?

    def make_admin():
        self.is_admin = True

    def revoke_admin():
        self.is_admin = False

    def update_salary(new_salary):
        self.salary_history.push(self.salary)
        # ^ need to figure out a better way for this. There's no way to see when someone was being
        #    paid a certain amount.  Maybe have a salary class with amounts and dates?
        self.salary = new_salary

    def update_vacation_hours(new_hours):
        self.vacation_hours = new_hours

    def subtract_vacation_hours(hours):
        if self.vacation_hours - hours < 0:
            raise ValueError('Not enough hours!')
        self.vacation_hours = self.vacation_hours - hours

    def update_bonus(new_bonus):
        self.bonus = new_bonus

    def is_manager(employee_id):
        get_manager_id_query = f"SELECT manager_id FROM employees WHERE employee_id = ${employee_id}"
        connection = connect_to_database('hr-app.db')
        manager_id = execute_read_query(connection, get_manager_id_query)
        connection.close()
        if manager_id == self.employee_id:
            return True

    def can_view_other_employee_info(other_employee_id):
        if self.is_admin or other_employee_id == self.employee_id or self.is_manager(other_employee_id):
            return True

        get_other_employee_is_hr_query = f"SELECT is_hr FROM employees WHERE employee_id = ${other_employee_id}"
        connection = connect_to_database('hr-app.db')
        other_employee_is_hr = execute_read_query(connection, get_other_employee_is_hr_query)
        connection.close()

        if self.is_hr and not other_employee_is_hr:
            return True

    def can_edit_other_employee_info(other_employee_id):
        if self.is_admin or self.is_manager(other_employee_id):
            return True