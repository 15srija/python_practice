student_data=[
    {
        'Name':'Ram',
        'Roll_no':10,
        'age':20,
        'course':'java'
    },
    {
        'Name':'Shyam',
        'Roll_no':11,
        'age':21,
        'course':'python'
    },
]

def add_new_student(name,roll_no,age,course):
    new_student={}
    new_student["Name"]=name
    new_student["roll_no"]=roll_no
    new_student['age']=age
    new_student['course']=course
    student_data.append(new_student)
add_new_student("Shyam",13,22,"C")
print(student_data)