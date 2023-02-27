from fastapi import FastAPI, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session

from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND

from models import Todo
from database import get_db

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get('/')
def read_todo(request: Request, db_session: Session = Depends(get_db)):
    todo_list = db_session.query(Todo).all()
    return templates.TemplateResponse('main/todo_list.html', {'todo_list': todo_list, 'request': request})


@app.post('/create')
def create_todo(title: str = Form(...), db_session: Session = Depends(get_db)):
    new_todo = Todo(title=title)
    db_session.add(new_todo)
    db_session.commit()

    url = app.url_path_for('read_todo')

    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)


@app.get('/update/{todo_id}')
def update_todo(todo_id: int, db_session: Session = Depends(get_db)):
    todo = db_session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complate = not todo.complate
    db_session.add(todo)
    db_session.commit()

    url = app.url_path_for('read_todo')

    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)


@app.get('/delete /{todo_id}')
def delete_todo(todo_id: int, db_session: Session = Depends(get_db)):
    todo = db_session.query(Todo).filter(Todo.id == todo_id).first()
    db_session.delete(todo)
    db_session.commit()

    url = app.url_path_for('read_todo')

    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)
