from fastapi import FastAPI, Path, HTTPException, Query
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
    # return {'message': f'Patient with ID {patient_id} not found.'}
    raise HTTPException(status_code=404, detail=f'Patient with ID {patient_id} not found.')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="sort on the basis of height, weight or bmi"), order: str = Query('asc', description="sort in ascending or descending order")):
    valid_field = ['height', 'weight', 'bmi']
    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Please choose from {valid_field}.")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Please choose 'asc' or 'desc'.")
    sorted_data = sorted(load_data().values(), key=lambda x: x.get(sort_by, 0), reverse=(order == 'desc'))
    return sorted_data