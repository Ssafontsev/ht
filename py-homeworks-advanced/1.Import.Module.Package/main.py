from datetime import datetime
from application.salary import calculate_salary
from db.people import get_employees

if __name__ == '__main__':
    current_date = datetime.now().date()
    print(current_date)
    calculate_salary()
    get_employees()