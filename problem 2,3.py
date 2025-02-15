#Problem 2: Counting the number of PartTimeStudents generated (Only includes attributes and constructors)
class Student:
    def __init__(self, name, major, id: str):
        self.name = name 
        self.id = id 
        self.major = major

class FullTimeStudent(Student):
    def __init__(self, name, major, id: str):
        super().__init__(name, major, id)
        self.projects = []

class PartTimeStudent(Student):
    counter = 0
    def __init__(self, name, major, id: str, minHour, maxHour):
        super().__init__(name, major, id)
        self.minHour = minHour
        self.maxHour = maxHour
        PartTimeStudent.counter += 1
    @staticmethod
    def count():
        return PartTimeStudent.counter


class Lecturer:
    def __init__(self, id: str, name, rank, researchField):
        self.id = id
        self.name = name
        self.rank = rank
        self.researchField = researchField

class Project:
    def __init__(self, name, budget, leader=None, members=None):
        self.name = name
        self.budget = budget
        self.leader = leader  
        self.members = members if members is not None else []


#test problem 2
s1 = PartTimeStudent("Alice", "Computer Science", "PT001", 10, 20)
s2 = PartTimeStudent("Bob", "Math", "PT002", 5, 15)
print(f"Total Part-Time Students: {PartTimeStudent.count()}")
        
        
        
        # Problem 3: Manage objects using SchoolSystem (list up to 10 elements)
class Student:
    def __init__(self, name, major, id):
        self.name = name 
        self.id = id 
        self.major = major

class FullTimeStudent(Student):
    def __init__(self, name, major, id):
        super().__init__(name, major, id)
        self.projects = []

    def join_project(self, project):
        self.projects.append(project)

class PartTimeStudent(Student):
    def __init__(self, name, major, id, minHour, maxHour):
        super().__init__(name,major, id)
        self.minHour = minHour
        self.maxHour = maxHour
        

class Lecturer:
    def __init__(self, id, name, rank, researchField):
        self.id = id
        self.name = name
        self.rank = rank
        self.researchField = researchField

class Project:
    def __init__(self, name, budget, leader=None, members=None):
        self.name = name
        self.budget = budget
        self.leader = leader
        self.members = members if members is not None else []

class SchoolSystem:
    def __init__(self):
        self.students = []   
        self.lecturers = []  
        self.projects = []   

    def add_student(self, student):
        if len(self.students) < 10:
            self.students.append(student)
        else:
            print("Unable to add students: the list is full.")

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < 10:
            self.lecturers.append(lecturer)
        else:
            print("Unable to add instructors: the list is full.")

    def add_project(self, project):
        if len(self.projects) < 10:
            self.projects.append(project)
        else:
            print("Unable to add projects: the list is full.")



# ---test for Problem 3 ---

# Create a FullTimeStudent object
fts1 = FullTimeStudent("Alice", "Computer Science", "FT001")
fts2 = FullTimeStudent("Bob", "Mathematics", "FT002")

# Create a PartTimeStudent object
pts1 = PartTimeStudent("Charlie", "Biology", "PT001", 5, 10)
pts2 = PartTimeStudent("David", "Chemistry", "PT002", 4, 8)

# Create a lecturer object
lect1 = Lecturer("L001", "Prof. Smith", "Professor", "Physics")
lect2 = Lecturer("L002", "Dr. Johnson", "Assistant Professor", "Computer Science")

# Create a Project object
proj1 = Project("Project Alpha", 100000)
proj2 = Project("Project Beta", 150000)

# Initialize the SchoolSystem.
system = SchoolSystem()

# Add students to the system (both FullTimeStudent and PartTimeStudent)
system.add_student(fts1)
system.add_student(fts2)
system.add_student(pts1)
system.add_student(pts2)

# Add lecturer to the system
system.add_lecturer(lect1)
system.add_lecturer(lect2)

# Add a project to the system
system.add_project(proj1)
system.add_project(proj2)

# print list student
print("=== Students in SchoolSystem ===")
for s in system.students:
    print(f"Name: {s.name}, ID: {s.id}, Major: {s.major}")

# print list lecturer
print("\n=== Lecturers in SchoolSystem ===")
for l in system.lecturers:
    print(f"Name: {l.name}, ID: {l.id}, Rank: {l.rank}, Research Field: {l.researchField}")

# print list project
print("\n=== Projects in SchoolSystem ===")
for p in system.projects:
    print(f"Project Name: {p.name}, Budget: {p.budget}, Leader: {p.leader}, Members Count: {len(p.members)}")
