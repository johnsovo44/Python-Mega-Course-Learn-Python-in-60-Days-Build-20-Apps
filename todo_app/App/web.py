import streamlit as st
import modules.functions as f

todos = f.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    # session state is used to store the value of the input field
    todos = f.get_todos()
    todos.append(new_todo)
    f.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear the input field after adding

st.title("To-Do App")
st.subheader("Manage your tasks efficiently")
st.write("This is a simple To-Do application built with Streamlit.")
st.write("You can add, edit, and delete tasks.")

for todo in todos:
    st.checkbox(todo.strip(), key=todo)

st.text_input(label=" ", placeholder="Add a new task", key="new_todo"
              , on_change = add_todo)

st.session_state
# this helps you see what is going on in the session state