def search_contact(contacts: dict,query: str) -> str:
    cleaned_query = ...
    for name, number in contacts.items():
        if ...:
            return number
    return "contact not found"


def count_letters(text:str) -> dict:
    counts={}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            counts[char_lower] = counts.get(char_lower, 0) + 1
    return counts


def calculate_results(score_dict:dict) -> dict:
    results ={}
    for student, scores in score_dict.items():
        avg = round(sum(scores) / len(scores), 1)
        status = "Pass" if avg >= 50 else "Fail"
        results[student]=(avg, status)
    return results


if __name__=="__main__":
    contacts_data={"Jeff": "0972652821","sharon": "0976621010","Andrew": "0978960333"}
    print("P1 test: " ,search_contact(contacts_data, "   JEFF    "))
    print("P2 test: " ,count_letters("Hello World"))
    student_scores = {"Jeff":[80,99,76],"john":[70,88,30],"Jane":[100,30,99]}
    print("P3 test: ",calculate_results(student_scores))