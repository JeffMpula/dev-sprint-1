def add_course(courses_dict):
    course_name = input("enter course code (eg MAT1100): ").strip().upper()

    while True:
        try:
            score = float(input(f"Enter marks for {course_name} (0-100): "))
            if 0 <= score <= 100:
                courses_dict[course_name] = score
                print(f"✓ Added {course_name} with score: {score}\n")
                break
            else:
                print("Error: score mus be between 0 and 100.")
        except ValueError:
                print("Error: invalide input please enter numerical mark.")
            

def calculate_avarage(courses_dict):
    if not courses_dict:
        return 0.0
    
    total = sum(courses_dict.values())
    avarage = total / len(courses_dict)
    return avarage

def display_summary(courses_dict):
    print("=" * 30)
    print("      ACADEMIC SUMMARY     ")
    print("=" * 30)

    if not courses_dict:
        print("No courses recorded yet.")
        return

    for course, mark in courses_dict.items():
        print(f"- {course}: {mark:.1f}%")

    avg = calculate_avarage(courses_dict)
    print("-" * 30)
    print(f"0verall avarage: {avg:.2f}%")

    if avg >= 50:
        print("Status: Satisfactory Progress")
    else:
        print("Status: Needs Improvement")
    print("=" * 30)

def main():
    student_courses = {}

    print("--- UNZA Course Tracker Setup ---")

    for i in range(3):
        print(f"\nCourse {i + 1} of 3:")
        add_course(student_courses)

    display_summary(student_courses)

if __name__ == "__main__":
    main()