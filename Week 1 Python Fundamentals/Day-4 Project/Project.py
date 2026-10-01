# Student Management System 

class Student:
    def __init__(self, name, roll, dept, age):
        self.name = name
        self.roll = roll
        self.dept = dept
        self.age = age

class System:
    def __init__(self):
        self.all_students = []  # Sab students yahan store honge
    
    # 1. Student add karna
    def add(self):
        print("\n--- Add Student ---")
        name = input("Name: ")
        roll = input("Roll Number: ")
        dept = input("Department: ")
        age = input("Age: ")
        
        # yaha per Check hoga - kya roll number alredy hai?
        for s in self.all_students:
            if s.roll == roll:
                print("Roll number already exists!")
                return
        
        # New student banake list mein dalo
        new = Student(name, roll, dept, age)
        self.all_students.append(new)
        print("Student Added!")
    
    # 2. Sab students ko dekhana
    def view(self):
        
        if not self.all_students:
            print("No students found!")
            return
        
        print("\n--- All Students ---")
        for s in self.all_students:
            print("="*45)
            print(f"Name: {s.name}, Roll: {s.roll}, Dept: {s.dept}, Age: {s.age}")
            print("="*45)

    # 3. Student search karnaoo
    def search(self):
        roll = input("Enter Roll Number to search: ")
        
        for s in self.all_students:
            print("="*45)
            if s.roll == roll:
                print(f"Found! Name: {s.name}, Dept: {s.dept}, Age: {s.age}")
                return
        
        print("Student not found!")
    
    # 4. Student update karna
    def update(self):
        roll = input("Enter Roll Number to update: ")
        
        for s in self.all_students:
            print("="*45)
            if s.roll == roll:
                print("What to update?")
                print("1. Department")
                print("2. Age")
                choice = input("Enter 1 or 2: ")
                
                if choice == "1":
                    s.dept = input("New Department: ")
                    print("Department updated!")
                elif choice == "2":
                    s.age = input("New Age: ")
                    print("Age updated!")
                else:
                    print("Wrong choice!")
                return
            
        print("Student not found!")
    
    # 5. Student delet karna
    def delete(self):
        roll = input("Enter Roll Number to delete: ")
        
        for i in range(len(self.all_students)):
            if self.all_students[i].roll == roll:
                confirm = input(f"Delete {self.all_students[i].name}? (y/n): ")
                if confirm == "y":
                    self.all_students.pop(i)
                    print("Student deleted!")
                return
        
        print("Student not found!")
    
    # 6. Menu dikhana
    def menu(self):
        while True:
            print("\n" + "="*30)
            print("1. Add Student")
            print("2. View All")
            print("3. Search")
            print("4. Update")
            print("5. Delete")
            print("6. Exit")
            print("="*30)
            
            choice = input("Enter choice (1-6): ")
            
            if choice == "1":
                self.add()
            elif choice == "2":
                self.view()
            elif choice == "3":
                self.search()
            elif choice == "4":
                self.update()
            elif choice == "5":
                self.delete()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
            
            input("\nPress Enter to continue...")

# Program start
system = System()
system.menu()