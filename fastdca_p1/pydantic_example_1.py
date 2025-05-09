from pydantic import BaseModel, ValidationError

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field with default None

# Valid data
user_data = {"id": 1, "name": "Syeda", "email": "syedagulzarbano@gmail.com", "age": 22}
user = User(**user_data)
print(user)  # id=1 name='Syeda' email='syedagulzarbano@gmail.com' age=22
print(user.model_dump())  # {'id': 1, 'name': 'Syeda', 'email': 'syedagulzarbano@gmail.com', 'age': 22}

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="bono", email="gulzar_bano@yahoo.com")
except ValidationError as e:
    print(e)