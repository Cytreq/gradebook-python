students = {"Cyprian" : 
            {"Matematyka" : [5, 4],
             "Polski": []},
            "Lena" : 
            {"Matematyka" : []}
            }


def add_student(student):
    if student not in students:
        students[student] = {}
    else:
        print("This student already exists")

def add_subject(student, subject):
    if student not in students:
        print("This student doesn't exist")
        return None
    if subject in students[student]:
        print("This subject already exists")
        return None
    students[student][subject] = []

def add_grade(student, subject, grade):
    if student not in students:
        print("Student doesn't exist ")
        return None
    elif subject not in students[student]:
        print("Subject doesn't exist")
        return None
    students[student][subject].append(grade)

def print_grades(student, subject):
    if student not in students:
        return None
    elif subject not in students[student]:
        return None 
    elif not students[student][subject]:
        print(f"{student} doesn't have any grades.")
        return None
    print(f"{student} have {students[student][subject]} in {subject}")

def main():
    while True: 
        ...

def delete_student(student):
    if student not in students:
        print("Student not found")
    else:
        del students[student]

def delete_latest_grade(student, subject):
    if student not in students:
        return None
    elif subject not in students[student]:
        return None
    elif not students[student][subject]:
        print("Student doesn't have any grades")
        return None
    removed_grade = students[student][subject].pop()
    print(f"Removed {removed_grade} from {student}'s {subject}")

def delete_subject(student, subject):
    if student not in students:
        return None 
    elif subject not in students[student]:
        return None
    removed_subject = students[student].pop(subject)
    print(f"Deleted {subject} from {student}'s profile")

