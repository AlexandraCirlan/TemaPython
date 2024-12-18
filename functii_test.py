from Tema1 import Employee, Manager

class TestEmployeeManager:
    def setup_method(self):
        # Resetăm variabilele de clasă înainte de fiecare test
        Employee.empCount = 0
        Manager.mgr_count = 0

    def test_employee_creation(self):
        emp = Employee("Alice", 4000)
        assert emp.name == "Alice"
        assert emp.salary == 4000
        assert Employee.empCount == 1

    def test_manager_creation(self):
        mgr = Manager("John Doe", 5000, "Development")
        assert mgr.name == "John Doe"
        assert mgr.salary == 5000
        assert mgr.department == "Team_Cirlan_Development"
        assert Manager.mgr_count == 1

    def test_employee_count(self):
        emp1 = Employee("Alice", 4000)
        emp2 = Employee("Bob", 5000)
        assert Employee.empCount == 2
