def manage_student_database():
    # Step 1: Initialize an empty list and a counter for student IDs
    student_list = []
    student_id = 1

    while True:
        # Step 2: Collect student names
        name = input("Please enter the student's name (or type 'stop' to finish): ")
        
        if name.lower() == 'stop':
            break  # Exit the loop if the user types 'stop'
        
        # Step 3: Check for duplicate names
        if any(student[1] == name for student in student_list):
            print("This name is already in the list.")
        else:
            # Create a tuple with the student ID and name, then add it to the list
            student_list.append((student_id, name))
            student_id += 1  # Increment the student ID for the next entry

    # Step 4: Display the complete list of students
    print("\nComplete List of Students (Tuples):")
    print(student_list)

    # Step 5: Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Step 6: Calculate and display statistics
    total_students = len(student_list)
    total_length_names = sum(len(student[1]) for student in student_list)
    longest_name_student = max(student_list, key=lambda student: len(student[1]))
    shortest_name_student = min(student_list, key=lambda student: len(student[1]))

    # Display statistics
    print(f"\nTotal number of students: {total_students}")
    print(f"Total length of all student names combined: {total_length_names}")
    print(f"The student with the longest name is: {longest_name_student[1]}")
    print(f"The student with the shortest name is: {shortest_name_student[1]}")

# Step 7: Call the manage_student_database() function
manage_student_database()