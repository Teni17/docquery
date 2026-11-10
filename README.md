#DocQuery

AI powered document Q&a system: upload documents, ask questions and get answers with citations

## current phase
phase 0 - early development - backend skeleton

## Run locally
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload