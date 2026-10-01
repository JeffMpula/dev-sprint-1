def get_grade(score):
    if score >= 80 :
        return "A+ (Distinction)"
    elif score >= 70 :
        return "A (Merit)"
    elif score >= 60 :
        return "B (Credit)"
    elif score >= 50 :
        return "C (pass)"
    else:
        return "F (Fail)"

modules =["MAT1100","PHY 1010" ,"CHE 1000","BIO 1400","CSC 1100"]
results ={}

print("---UNZA GRADE PREDICTOR---\n")

for module in modules:
    while True:
        try:
            score =float(input(f"Enter predicted percentage for {module}: "))
            if 0 <=score <= 100:
                results[module]=score
                break
            print(" [!] score must be between 0 and 100.")
        except ValueError:
            print(" [!] invalid input. enter numeric value (eg,75..).")

print("\n---RESULT SUMMARY---")
total_score = 0
lowest_module = None
lowest_score = 101

for module, score in results.items():
    grade= get_grade(score)
    print(f"{module}:{score}% ->{grade}")
    total_score += score

    if score < lowest_score:
        lowest_score = score
        lowest_module = module


    avarage = total_score / len(modules)
    print(f"\n0verall avarage: {avarage:.1f}%")
    print(f"lowest subject: {lowest_module} ({lowest_score}%)")

    if avarage >= 70:
        print("status: Excellent! on tract to Computer Science selection!")
    elif avarage >= 50:
        print("status: Passing, but push harder in MAth & Physics for CS selection")
    else:
        print("status: below passing thershold. increase study block hours")