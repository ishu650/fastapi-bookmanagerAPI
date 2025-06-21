# fastapi-bookmanagerAPI
A simple, clean, and RESTful API built with FastAPI that allows users to add, view, update, and delete books. The application uses Pydantic for data validation and is built with an in-memory data store, making it perfect for learning, prototyping, or as a foundation for more complex backend services.


##  Features
- Add, update, delete, and get books
- Validated with Pydantic
- In-memory storage
- Interactive Swagger UI

##  How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
