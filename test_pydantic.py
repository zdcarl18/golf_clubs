from pydantic import BaseModel

class TestModel(BaseModel):
    name: str
    age: int

# Test the model
test = TestModel(name="Test", age=25)
print(f"Test successful! Created model with name: {test.name} and age: {test.age}") 