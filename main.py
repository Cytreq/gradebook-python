students = {"Cyprian" : 
            {"Matematyka" : [],
             "Polski ": []},
            "Lena" : 
            {"Matematyka " : []}
            }


def add_student(student):
    if student not in students:
        students[student] = {}
    else:
        print("This student already exists")

def add_subject(student, subject):
    if student not in students:
        print("This student doesn't exist")
    elif subject not in students[student]:
        students[student][subject] = []

def add_grade(student, subject, grade):
    if student not in students:
        print("Student doesn't exist ")
    elif subject not in students[student]:
        print("Subject doesn't exist")
    students[student][subject].append(grade)
    





        


