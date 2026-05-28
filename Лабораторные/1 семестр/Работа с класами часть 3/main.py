
class Employee:

    def __init__(self, name = None, identification_num = None):
        self.name = name
        self.__identification_num = identification_num

    def get_info(self):
        return self.name, self.__identification_num

class Manager(Employee):
    def __init__(self, name, identification_num, department):
        self.department = department
        super().__init__(name, identification_num)

    def manage_project(self):
        pass

class Technician:

    def __init__(self, specialization):
        self.specialization = specialization

    def perform_maintenance(self):
        pass

class TechManager(Manager, Technician):

    def __init__(self, identification_num, name, department, specialization):
        Manager.__init__(self, name, identification_num, department)
        Technician.__init__(self, specialization)
        self.list = []

    def add_employee(self, identification_num, name, department, specialization):
        user_data = {'ID': identification_num, 'name': name, 'department': department, 'specialization': specialization}
        self.list.append(user_data)

    def get_team_info(self):
        return self.list

test1 = TechManager("John", 1, "Couch", '')
test1.add_employee(2, "name", "department", "spec")
test1.add_employee(3, "Name2", "Department2", "Specialization2")
print(test1.get_team_info())