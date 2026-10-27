from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

new_person: Person = {'age': 30, 'name': 'John Doe', 'email': 'john.doe@example.com'}

print(new_person)