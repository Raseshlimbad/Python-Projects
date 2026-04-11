import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Notes App (FastAPI)")

menu = ["Create", "View All", "View One", "Update", "Delete"]
choice = st.sidebar.selectbox("Select Operation", menu)

# CREATE
if choice == "Create":
    st.subheader("Create a Note")
    
    id = st.text_input("ID")
    title = st.text_input("Title")
    content = st.text_area("Content")
    
    if st.button("Create"):
        data = {
            "id": id,
            "title": title,
            "content": content
        }
        response = requests.post(f"{BASE_URL}/notes/", json=data)
        if response.status_code == 200:
            st.success("Note created successfully!")
            st.json(response.json())
        else:
            st.error("Failed to create note")

# VIEW ALL
elif choice == "View All":
    st.subheader("All Notes")

    response = requests.get(f"{BASE_URL}/notes/")
    notes = response.json()

    for note in notes:
        st.write(note)

# VIEW ONE
elif choice == "View One":
    st.subheader("Get Note by ID")

    note_id = st.number_input("Enter ID")

    if st.button("Get Note"):
        response = requests.get(f"{BASE_URL}/notes/{note_id}")

        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Note not found")

# UPDATE
elif choice == "Update":
    st.subheader("Update Note")

    note_id = st.number_input("Enter ID")
    title = st.text_input("New Title")
    content = st.text_area("New Content")

    if st.button("Update"):
        data = {
            "id": note_id,
            "title": title,
            "content": content
        }

        response = requests.put(f"{BASE_URL}/notes/{note_id}", json=data)

        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error("Note not found")

# DELETE
elif choice == "Delete":
    st.subheader("Delete Note")

    note_id = st.number_input("Enter ID")

    if st.button("Delete"):
        response = requests.delete(f"{BASE_URL}/notes/{note_id}")

        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error("Note not found")
