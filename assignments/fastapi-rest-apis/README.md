# FastAPI REST APIs

## 🎯 Objective

Build a REST API using the FastAPI framework. Students will define endpoints, request/response models, and implement CRUD operations for a simple resource.

## 📝 Tasks

### 🛠️ 1. Create the API structure

#### Description
Create a FastAPI application with a root endpoint and at least one resource endpoint for managing todo items.

#### Requirements
Completed program should:

- Use FastAPI and define a `FastAPI()` app instance
- Include at least one root endpoint at `/`
- Return JSON responses from endpoints

### 🛠️ 2. Add CRUD endpoints for todo items

#### Description
Implement create, read, update, and delete endpoints for a `TodoItem` resource. Use Pydantic models for request validation.

#### Requirements
Completed program should:

- Define a Pydantic model for todo items
- Implement endpoints for `GET /todos`, `POST /todos`, `PUT /todos/{id}`, and `DELETE /todos/{id}`
- Store todo items in an in-memory list or dictionary

### 🛠️ 3. Validate data and use API docs

#### Description
Ensure the API validates incoming data and supports automatic OpenAPI documentation.

#### Requirements
Completed program should:

- Validate required fields and data types using Pydantic
- Return meaningful error responses for invalid data or missing items
- Allow inspection of the API schema via the FastAPI docs at `/docs`
