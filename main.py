from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'Hello, World!'}

@app.get('/about')
def about():
    return {'message': "Aman Pandey is the only guy in Tech industry who can let the work done in a very short time. He is a great software engineer and a great human being."}