# Create a Student class with name, roll, and marks; compute average.

class Student:
    def __init__(self, name: str, roll: str, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average(self) -> float:
        return sum(self.marks) / len(self.marks) if self.marks else 0.0


def main():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks_input = input("Enter marks separated by spaces: ")
    marks = [float(m) for m in marks_input.split()] if marks_input.strip() else []
    student = Student(name, roll, marks)
    print(f"Average marks for {student.name} (Roll {student.roll}): {student.average():.2f}")


if __name__ == "__main__":
    main()
