from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int]=None
    email: EmailStr
    cgpa: Optional[float]=Field(None,ge=0.0,le=10.0)  #ge=greater than or equal to, le=less than or equal to

new_student = {'name': 'John Doe', 'age': "20", 'email': 'john.doe@example.com', 'cgpa': "8.5"}    #data validate krr paare h int nhi rkh skte yaha pe name me par it is smart enough ki int me 32 ya "32" likho wo smart h smjh jata h

student=Student(**new_student)  #pydantic model me dictionary ko unpack karke pass karte hai
print(dict(student))