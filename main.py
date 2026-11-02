class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)

    def display_information(self):
        average = self.calculate_average()

        print("Student:", self.name)
        print("Age:", self.age)
        print("Average:", average)

        if average >= 10:
            print("Result: Passed")
        else:
            print("Result: Failed")


def main():
    students = [
        Student("Ahmed", 20, [15, 14, 12]),
        Student("Amine", 21, [8, 9, 10]),
        Student("Sara", 19, [17, 16, 18])
    ]

    for student in students:
        student.display_information()
        print("-------------------")


if __name__ == "__main__":
    main()
