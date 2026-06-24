# Forge Resume Builder

## Backend Setup & Run Guide

### 1. Set Up Virtual Environment
Ensure you are in the `backend` directory, then create and activate a Python virtual environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
Install the required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Server
To run the server in development mode, run the following command from the `backend/` folder:

```bash
fastapi dev app/main.py
```

Once running, the API will be available at `http://127.0.0.1:8000` and the interactive Swagger documentation can be accessed at `http://127.0.0.1:8000/docs`.

