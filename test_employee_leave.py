import employee_leave

def test_eligible_leave(capfd):
    employee_leave.check_leave_eligibility("Alice", "EMP001", 10)
    captured = capfd.readouterr()
    assert "Eligible for Leave" in captured.out

def test_not_eligible_leave(capfd):
    employee_leave.check_leave_eligibility("Bob", "EMP002", 15)
    captured = capfd.readouterr()
    assert "Not Eligible for Leave" in captured.out

def test_boundary_condition(capfd):
    employee_leave.check_leave_eligibility("Charlie", "EMP003", 12)
    captured = capfd.readouterr()
    assert "Eligible for Leave" in captured.out
