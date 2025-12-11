def emp_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Employee Department: {department}\n"
        f"Employee Salary: {salary}\n"
    )
    return result

if __name__ == "__main__":
    name = "pradeep"
    emp_id = "125"
    department = "IT"
    salary = "55000"
    
    print(emp_details(name, emp_id, department, salary))
