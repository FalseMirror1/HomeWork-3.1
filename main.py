import datetime
from Application.DB.People import get_employees
from Application.Salary import calculate_salary


if __name__ == '__main__':
    print(datetime.datetime.now())
    calculate_salary()
    get_employees()
