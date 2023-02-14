import streamlit as st
import functions

todos = functions.get_todo()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my todo list')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.title(), key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder='Add new todo...',
              on_change=add_todo, key="new_todo")

