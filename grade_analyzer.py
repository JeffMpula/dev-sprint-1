import json

def analyze_grade(courses_dict):
    if not courses_dict:
        return None

    top_course = max(courses_dict, key=courses_dict.get)
    lowest_course = min (courses_dict, key=courses_dict.get)

    passing_courses = [course for course, score in courses_dict.items() if score >= 50]
    failing_courses = [course for course, score in courses_dict.items() if score < 50]

    return{
        "top_course":(top_course, courses_dict[top_course]),
        "lowest_course":(lowest_course, courses_dict[lowest_course]),
        "passing":passing_courses,
        "failing":failing_courses
    }

def save_transcript(courses_dict, filename = "transcript.json"):
    try:
        with open(filename, "w") as file:
            json.dump(courses_dict, file, indent=4)
        print(f"transcript succesfully saved to '{filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

def load_transcript(filename = "transcript.json"):
    try:
        with open(filename, "r") as file:
            data =json.load(file)
            print(f"Loaded existing transcript from '{filename}'")
            return data
    except FileNotFoundError:
        print(f"Notice: '{filename}' not found. starting with new record")
        return {}
    except json.JSONDecodeError :
        print("Error: corrupted file format. starting fresh")
        return {}

def main():
    student_courses = load_transcript()

    if not student_courses:
        student_courses ={
            "MAT1100":88.0,
            "PHY1010":44.5,
            "CSC1100":92.0,
            "ENG1100":65.0
        }
        save_transcript(student_courses)

    analysis = analyze_grade(student_courses)


    if analysis:
        print("\n" + "=" * 38)
        print("         ACADEMIC PERFORMANCE           ")
        print("=" * 38)
        print(f"Top course      {analysis['top_course'][0]}({analysis['top_course'][1]}%)")
        print(f"Lowest course      {analysis['lowest_course'][0]}({analysis['lowest_course'][1]}%)")
        print("-" * 38)
        print(f"Passing  ({len(analysis['passing'])}): {', '.join(analysis['passing'])}")
        print(f"Failing  ({len(analysis['failing'])}): {', '.join(analysis['failing']) if analysis['failing'] else 'None'}")
        print("="* 38)

if __name__ == "__main__":
    main()