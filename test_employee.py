from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: pradeep\n"
        "Employee ID: 125\n"
        "Employee Department: IT\n"
        "Employee Salary: 55000\n"
    )

    result = employee_details("pradeep", "125", "IT", "55000")
    assert result == expected_output
