students = {"Cyprian" : 
            {"Matematyka" : [5, 4],
             "Polski": []},
            "Lena" : 
            {"Matematyka" : []}
            }
def check_student(student):
    if student not in students:
        return False
    return True

def check_subject(student, subject):
    if not check_student(student):
        return False
    if subject not in students[student]:
        return False
    return True

def add_student(student):
    if not check_student(student):
        students[student] = {}
        return True
    print("This student already exists")
    return False

def add_subject(student, subject):
    if check_subject(student, subject):
        print("This subject already exists")
        return False
    students[student][subject] = []
    return True

def add_grade(student, subject, grade):
    if not check_student(student):
        print("Student doesn't exist ")
        return False
    if not check_subject(student, subject):
        print("Subject doesn't exist")
        return False
    print("Grade added successfully")
    students[student][subject].append(grade)

def print_grades(student, subject):
    if not check_student(student):
        return False
    if not check_subject(student, subject):
        return False
    elif not students[student][subject]:
        print(f"{student} doesn't have any grades.")
        return False
    print(f"{student} have {students[student][subject]} in {subject}")
    return True

def main():
    while True: 
        ...

def delete_student(student):
    if not check_student(student):
        print("Student not found")
        return False
    del students[student]
    return True

def delete_latest_grade(student, subject):
    if not check_student(student):
        return False
    if check_subject(student, subject):
        return False
    elif not students[student][subject]:
        print("Student doesn't have any grades")
        return None
    removed_grade = students[student][subject].pop()
    print(f"Removed {removed_grade} from {student}'s {subject}")

def delete_subject(student, subject):
    if not check_student(student):
        return False
    if not check_subject(student, subject):
        return False
    removed_subject = students[student].pop(subject)
    print(f"Deleted {subject} from {student}'s profile")
    return True

def calculate_subject_GPA(student, subject):
    try:
        grades = students[student][subject]
        if not grades:
            return False
        return sum(grades) / len(grades)
    except KeyError:
        return False

    
def calculate_student_GPA(student):
    if not check_student(student):
        return False
    count = 0 
    sum_of_subjects = 0
    for subject in students[student]:
        subject_GPA = calculate_subject_GPA(student, subject)
        if subject_GPA is not None:
            count += 1
            sum_of_subjects += subject_GPA
    if count == 0:
        return None
    return sum_of_subjects / count
