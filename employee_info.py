# Define a dictionary to store employee information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def display_all_records():
    print(("Name" + "\t" + "Age" + "\t" + "Department" + "\t" + "Salary").expandtabs(14))
    for item in employee_data:
        print((item['name'] + "\t" + str(item['age']) + "\t" + item['department'] + '\t' + str(item['salary'])).expandtabs(14))

def average_salary():
    count = 0
    total = 0
    for item in employee_data:
        total += item['salary']
        count += 1
    average = total/count
    print ("average salary is" , round(average, 2))
    return round(average, 2)

def employee_by_age_range(lower, upper):
    result = []
    for item in employee_data:
        if item['age'] > lower and item['age'] < upper:
            result.append(item)
    return result

def employee_by_dept(dept):
    result = []
    for item in employee_data:
        if item['department'] == dept:
            result.append(item)
    return result

def display_record(employee_info):
        print(("Name" + "\t" + "Age" + "\t" + "Department" + "\t" + "Salary").expandtabs(14))
        for item in employee_info:
            print((item['name'] + "\t" + str(item['age']) + "\t" + item['department'] + '\t' + str(item['salary'])).expandtabs(14))

def main():
    while True:
        user_in = input("Select Option ==> ")

        if user_in == '0': display_all_records()
        if user_in == '1': average_salary()
        if user_in == '2': display_record(employee_by_age_range(20, 26))
        if user_in == '3': display_record(employee_by_dept('Sales'))
        if user_in == 'q': quit()
        else: print("Invalid")

if __name__ == "__main__":
    main()