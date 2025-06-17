import streamlit as st
import modules.functions as f

todos = f.get_todos()
st.title("To-Do App")
st.subheader("Manage your tasks efficiently")
st.write("This is a simple To-Do application built with Streamlit.")
st.write("You can add, edit, and delete tasks.")

for todo in todos:
    st.checkbox(todo.strip(), key=todo)

st.text_input(label=" ", placeholder="Add a new task", key="new_todo")