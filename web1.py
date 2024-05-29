import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todo = todo.split()
    todo = todo + '\n'
    todos.append(todo)
    function.write_todos(todos)
    st.text_input['']


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:

        todos.pop(index)
        function.write_todos(todos)
        st.experimental_rerun()


st.text_input(label='Enter a todo', placeholder='Add a todo...',
              on_change=add_todo, key='new_todo')