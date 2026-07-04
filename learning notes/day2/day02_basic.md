



📒 Day 2 Notes – Backend Architecture & FastAPI Fundamentals

Project: Employee Management API

Day: 2

Goal: Understand how a professional backend project is organized before writing production code.

1. What is a Backend?

A backend is responsible for:

Receiving requests from the client
Validating input
Executing business logic
Reading/Writing data
Returning a response

Example:

Browser

↓

GET /employees

↓

Backend

↓

Database

↓

JSON Response

Key Point:

The backend is the brain of the application.

2. What is an API?

API stands for Application Programming Interface.

It acts as a bridge between two applications.

Example:

Browser

↓

API

↓

Backend

↓

Database

3. What is REST?

REST (Representational State Transfer) is an architectural style for designing APIs.

REST is not just endpoint naming.

REST encourages:

Resources
HTTP Methods
Stateless communication
Standard HTTP Status Codes

GET    /employees
POST   /employees
PUT    /employees/1
PATCH  /employees/1
DELETE /employees/1

Notice:

The resource is always : employess

The action changes through HTTP methods.

4. HTTP Methods
Method	Purpose
GET	Read data
POST	Create new data
PUT	Replace entire resource
PATCH	Update part of resource
DELETE	Delete resource

6. What is FastAPI?

FastAPI is a modern Python framework used to build REST APIs.

Advantages

Fast
Automatic Validation
Swagger Documentation
Type Hints
Async Support

7. FastAPI vs Flask
Flask	FastAPI
Manual validation:	Automatic validation
No built-in Swagger:	Built-in Swagger
Less type hint support:	Full type hint support
Simpler for small apps:	Better suited for modern APIs


8. What is Uvicorn?

FastAPI defines the application.

Uvicorn runs the application.

Think:
FastAPI

↓

Application

↓

Uvicorn

↓

Server Starts

9. What is ASGI?

ASGI stands for Asynchronous Server Gateway Interface.

It allows Python applications to:

Handle asynchronous requests
Support WebSockets
Process multiple requests efficiently

Think

WSGI → Older synchronous interface

ASGI → Modern asynchronous interface

10. What happens when we open /docs?

Example

http://127.0.0.1:8000/docs

FastAPI automatically generates interactive API documentation using Swagger UI.

Benefits

View endpoints
Test APIs
See request/response models

11. Why do we use Decorators?

Example:
@app.get("/")
def home():
    return {"message": "Hello"}

The decorator tells FastAPI:

This function should handle GET requests for /.

Without the decorator, home() is just a normal Python function.

12. Separation of Concerns (SoC)

Every component should have one responsibility.

Bad Example

main.py

5000 lines

Everything is mixed together.

Good Example

Router

↓

Service

↓

Database

Each layer has a clear job.

13. Backend Layers
Client

↓

Router

↓

Service

↓

Database

↓

Service

↓

Router

↓

JSON Response

Responsibilities:

Router → Receives requests.

Service → Business logic.

Database → Stores data.

14. Why not put everything in main.py?

As applications grow, a single file becomes difficult to maintain.

Instead we separate code into modules.

Example

app/

main.py

routers/

services/

schemas/

models/

15. What is __init__.py?

__init__.py marks a directory as a Python package and allows Python to import modules from it.

It can also:

Run initialization code when the package is imported.
Expose commonly used objects (e.g., from .employee import router).
Improve package organization.

Although modern Python supports namespace packages, many projects still include __init__.py for clarity and maintainability.

16. Real Project Architecture

employee-management-api/

app/

├── main.py
├── routers/
├── services/
├── models/
├── schemas/
├── database.py

tests/

README.md

17. Interview Questions
What is REST?
Why FastAPI instead of Flask?
What is Uvicorn?
What is ASGI?
Why do we use decorators?
Why do we use Routers?
What is Separation of Concerns?
Why do we use __init__.py?
Explain the request lifecycle in FastAPI.
Difference between PUT and PATCH?

18. Key Takeaways
A backend is more than writing endpoints; it is about organizing responsibilities.
REST is an architectural style, not just endpoint naming.
FastAPI builds APIs; Uvicorn runs them.
Keep main.py small and focused.
Separate routers, services, models, and schemas as the project grows.
Every file and folder should have a clear responsibility.