class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self):
        return all(score >= 50 for score in self.scores)  # Assuming 50 is the passing grade


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        for student in self.students.values():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Student: {student.name}, Average: {average:.2f}, Status: {status}")


def main():
    tracker = PerformanceTracker()

    while True:
        try:
            name = input("Enter the student's name (or 'quit' to finish): ")
            if name.lower() == 'quit':
                break
            
            scores = []
            for i in range(1, 4):  # For three subjects
                score = float(input(f"Enter score for subject {i}: "))
                scores.append(score)
            
            student = Student(name, scores)
            tracker.add_student(student)
        
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")

    print("\nClass Performance:")
    tracker.display_student_performance()
    class_average = tracker.calculate_class_average()
    print(f"\nClass Average: {class_average:.2f}")


if __name__ == "__main__":
    main()
