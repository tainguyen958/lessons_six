class Student(object) :
    def __init__(self, name, student_id, grades) :
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def add_grade(self, grades) :
        self.grades.append(grades)

    def average_grade(self) :
        return sum(self.grades) / len(self.grades)

if __name__ == '__main__':
    s1 = Student(name="John", student_id=101, grades=[85, 90, 78])
    s1.add_grade(92)
    print("Average grade:", s1.average_grade())