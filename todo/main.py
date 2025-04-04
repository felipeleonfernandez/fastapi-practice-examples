from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    name: str
    description: str
    label: str

task_list = [Task(id=0, name="Create an API", description="Create an API using Python FastAPI", label="learning"),
              Task(id=1, name="Containerize the API", description="Create an image with the API inside", label="learning")]

@app.get("/")
async def root():
    return {"message": "This is a To Do API"}

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    ## Filter function
    ## Syntax:
    ##   filter(function, iterable)
    ##
    ## - 'function' is a callable that takes one argument and returns True if
    ##    the element should be included in the output.
    ## - 'iterable' is the collection to be filtered (e.g., list, tuple, set).
    ##
    ## Lambda is a small anonymous function typically used for short, throwaway functions.
    ## Think of it like:
    ##   def is_matching_id(task_id):
    ##      return task.id == task_id
    tasks = filter(lambda task: task.id == task_id, task_list)
    return list(tasks)[0]
            
@app.get("/tasks")
async def get_tasks():
    return task_list
