from Tema1 import Employee, Manager

class TestEmployeeManager:
    def setup_method(self):
        # Ressetez variabilele inainte de fiecare test
        Employee.empCount = 0
        Manager.mgr_count = 0

    def test_employee_creation(self):
        emp = Employee("Andreea", 4000)
        assert emp.name == "Andreea"
        assert emp.salary == 4000
        assert Employee.empCount == 1

    def test_manager_creation(self):
        mgr = Manager("Alexandra Cirlan", 5000, "Development")
        assert mgr.name == "Alexandra Cirlan"
        assert mgr.salary == 5000
        assert mgr.department == "Team_F34_Development"
        assert Manager.mgr_count == 1

    def test_employee_count(self):
        emp1 = Employee("Andreea", 4000)
        emp2 = Employee("Vlad", 5000)
        assert Employee.empCount == 2
