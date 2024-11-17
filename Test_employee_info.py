import employee_info as info

def test_age_range():
    test_result = info.employee_by_age_range(30, 40)

    assert test_result == [
    {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]

def test_avg_salary():
    assert info.average_salary() == round((50000 + 60000 + 70000 + 56000 + 65000 + 60000) / 6, 2)

def test_by_dept()