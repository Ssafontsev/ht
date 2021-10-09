from datetime import datetime, date, time
import calculate_salary() from salary

if __name__ == '__main__':
    current_date = datetime.now().date()
    print(current_date)
    calculate_salary()