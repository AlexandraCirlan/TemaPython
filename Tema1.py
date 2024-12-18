class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        """Displays the number of employees"""
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


# Clasa Manager care mosteneste din Employee
class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"Team_F34_{department}"
        Manager.mgr_count += 1

    # Suprascriu metoda display_employee
    def display_employee(self):
        if X % 3 == 0:
            print(f"Name: {self.name}")
        elif X % 3 == 1:
            print(f"Salary: {self.salary}")
        elif X % 3 == 2:
            print(f"Department: {self.department}")


# Valorile X și Y
nume = "Cirlan"
prenume = "Alexandra"
X = len(nume)
Y = len(prenume)

# Nr de obiecte Manager: Y / 3
num_managers = Y // 3

# Creez 3 obiecte din clasa Manager
manager1 = Manager("John Doe", 5000, "Development")
manager2 = Manager("Jane Smith", 6000, "Marketing")
manager3 = Manager("Bob Brown", 5500, "Operations")

# Creez 1 obiect din clasa Employee
employee1 = Employee("Alice White", 4000)

# Apelez metoda display_employee pentru Manageri
print("Displaying Managers:")
manager1.display_employee()
manager2.display_employee()
manager3.display_employee()

# Apelez metoda display_employee pentru Employee
print("\nDisplaying Employee:")
employee1.display_employee()

# Afisez valorile empCount și mgr_count
print(f"\nTotal Employees: {Employee.empCount}")
print(f"Total Managers: {Manager.mgr_count}")
