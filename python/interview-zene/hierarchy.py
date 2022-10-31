# Q1. Given a string representing an organizational hierarchy, it needs to be converted in different format using
# python. Attempt any 1 output Here is how an employee information looks like in the String.

# <employee_id>:<Employee_name>:<manager_id>

class Employee:
    def __init__(self, emp_id, name, manager_id):
        self.emp_id = emp_id
        self.name = name
        self.manager_id = manager_id


employees = {}
input_string = "1:Max:4, 4:Ann:0, 2:Jim:4, 3:Tom:1"
lst_str = input_string.split(",")
for element in lst_str:
    e_id, e_name, mgr_id = element.split(':')
    employee = Employee(emp_id=e_id.strip(), name=e_name, manager_id=mgr_id)
    employees[e_id.strip()] = employee

print(employees)
for e in employees.values():
    print(f'{e.emp_id} ----- {e.name} ------ {e.manager_id}')

