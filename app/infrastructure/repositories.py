# class TodoRepository:
#     def __init__(self, db):
#         self.db = db

#     def add(self, todo):
#         self.db.session.add(todo)
#         self.db.session.commit()
#         return todo

#     def update(self, todo):
#         self.db.session.merge(todo)
#         self.db.session.commit()
#         return todo

#     def get(self, todo_id):
#         return self.db.session.query(Todo).filter_by(id=todo_id).first()

#     def get_all(self):
#         return self.db.session.query(Todo).all()

#     def delete(self, todo_id):
#         todo = self.get(todo_id)
#         if todo:
#             self.db.session.delete(todo)
#             self.db.session.commit()
#         return todo