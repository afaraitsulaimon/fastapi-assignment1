from fastapi import FastAPI
# from uuid import UUID


app = FastAPI()

students = {}


student_data = {
    'id': 0,
    "name": "",
    "age" : 0,
    "sex" : "",
    "height" : 0
}

@app.get("/")
def home():
    return {'message':'Welcome Home'}


# to create a student
@app.post("/students")
def create_student(name: str, age: int, sex: str, height:float):
    # copy the student data and update it with the data gotten from client 
    new_student = student_data.copy()

    id_ = len(students) + 1
   
    new_student['id'] = id_
    new_student['name'] = name
    new_student['age'] = age  
    new_student['sex'] = sex  
    new_student['height'] = height

    students[new_student['id']] = new_student
    return {'message': 'Student Successfully created', 'data':new_student}  


# to fetch all students
@app.get("/all_students")
def get_all_students():
    return {'message':'All student successfully Retrieved', 'data':students}


# to fetch single student
# @app.get("/all_students/{id}")
# def get_single_students(id: str):
#     if id in students:
#         student = students[id]
#         return {'message': 'Student data Retrieved successfully', 'data': student}
#     else:
#         return {'message': 'Student not found'}


@app.get("/students/{id}")
def get_single_students(id: int):
    student = students[id]
    if not student:
        return {"error": "student not found"}
    
    return student
        


# to update a student data
@app.put("/students/{id}")
def update_students(id: int, name: str, age: int, sex: str, height: float):
    # fetch the id of the student we want to update the profile
    # as you know that the id is the key to the dictionary taht holds the profile details like this
    # 0001:{
    #      'id': 0001,
    #   "name": "famzy",
    #  "age" : 23,
    #  "sex" : "m",
    #  "height" : 34
    # }
    student = students[id]

    if not student:
        return {"error":"Student not found"}
    
    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height

    return {"message":"Student data updated", "data":student}


# to delete a student

@app.delete("/students/{id}")
def delete_single_student(id: int):
    # getting the student here is to check if it is the student you clicked
    student = students[id]
    if not student:
        return {"error": "Not This student"}

# then delete the user profile
    
    del students[id]
    return {"message":"Student profile deleted Successfully"}

    
        