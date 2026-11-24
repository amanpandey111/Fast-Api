from fastapi import FastAPI, Path
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message': 'Patient Management System API is running successfully.'}

@app.get('/about')
def about():
    return {'message': "This is a Patient Management System API built using FastAPI. It allows you to manage patient records, including adding, retrieving, updating, and deleting patient information."}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="Hey Id of the patient is required", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {'message': f'Patient with ID {patient_id} not found.'}