import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todo= st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My todo app")
st.subheader("This is my todo app")
st.write("this app helps you to manage your tasks")

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

selected_todo = st.selectbox("Select a todo to edit", todos)
new_value = st.text_input("Edit selected todo", value=selected_todo)
if st.button("Edit"):
    index = todos.index(selected_todo)
    todos[index] = new_value + "\n"
    functions.write_todos(todos)
    st.rerun()

st.text_input(label='', placeholder="Add a new todo",
              on_change= add_todo, key="new_todo" )

