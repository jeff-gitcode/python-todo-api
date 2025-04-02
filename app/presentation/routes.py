# from fastapi import APIRouter, HTTPException
# from app.core.mediator import Mediator
# from app.core.commands.create_todo import CreateTodoCommand
# from app.core.commands.update_todo import UpdateTodoCommand
# from app.core.queries.get_todo import GetTodoQuery

# router = APIRouter()

# @router.post("/todos")
# async def create_todo(title: str, description: str):
#     command = CreateTodoCommand(title=title, description=description)
#     todo = await Mediator.send(command)
#     return todo

# @router.put("/todos/{todo_id}")
# async def update_todo(todo_id: int, title: str = None, description: str = None, completed: bool = None):
#     command = UpdateTodoCommand(todo_id=todo_id, title=title, description=description, completed=completed)
#     updated_todo = await Mediator.send(command)
#     if not updated_todo:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return updated_todo

# @router.get("/todos/{todo_id}")
# async def get_todo(todo_id: int):
#     query = GetTodoQuery(todo_id=todo_id)
#     todo = await Mediator.send(query)
#     if not todo:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return todo