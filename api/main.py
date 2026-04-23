from fastapi import FastAPI
from backend.users.models import User
from backend.courses.models import Course

app = FastAPI()

@app.get("/users/")
def list_users():
    return [{"id": u.id, "name": u.username} for u in User.objects.all()]
