class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        
    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"
    
class Course:
    students = []
    count = 0
    def __init__(self, course_name, course_code, max_capacity = 10):
        self.course_name = course_name
        self.course_code = course_code
        self.max_capacity = max_capacity
        
    def add_student(self, student):
        for i in self.students:
            if i.student_id == student.student_id:
                return "Student already exist"            
        else:
            
            self.students.append(student)
            self.count += 1
            print("student added successfully")
        return self.students
    
    def get_student_count(self):
        return self.count

    def is_full(self):
        if self.count == self.max_capacity:
            return True
        
    def list_students(self):
        print(self.students)
    
    def __str__(self):
        return f"{self.course_name} ({self.course_code}) - Enrolled: {self.count}/{self.max_capacity}"
        
                
st1 = Student("Alice", "S001")
st2 = Student("Jose", "S002")
print(st1.__str__())
cous = Course("Maths", "MATH101")
cous = Course("Algebra", "MATH102")
cous.add_student(st1)
cous.add_student(st2)
print(cous.get_student_count())
print(cous.__str__())



