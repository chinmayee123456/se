def check_leave_eligibility(name, emp_id, leave_days):
    if leave_days <= 12:
        status = "Eligible for Leave"
    else:
        status = "Not Eligible for Leave"

    print("\n--- Employee Leave Status ---")
    print("Employee Name :", name)
    print("Employee ID   :", emp_id)
    print("Leave Days    :", leave_days)
    print("Status        :", status)
    print("-----------------------------\n")


if __name__ == "__main__":
    n = int(input("Enter number of employees: "))
    
    for _ in range(n):
        name = input("\nEnter employee name: ")
        emp_id = input("Enter employee ID: ")
        leave_days = int(input("Enter leave days taken: "))
        check_leave_eligibility(name, emp_id, leave_days)