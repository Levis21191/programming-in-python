class Employee:
    
    company_name = "TechSolutions Ltd."

    def __init__(self, name, position="Junior Developer"):
        self.name = name
        self.position = position

    def display_details(self):
        print("Employee Name:", self.name)
        print("Position:", self.position)
        print("Company:", Employee.company_name)
        print()


emp1 = Employee("Alice", "Project Manager")
emp2 = Employee("Bob") 

emp1.display_details()
emp2.display_details()
