# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI, including path operations, request validation, and clear JSON responses.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a FastAPI app and implement foundational endpoints so the API can be started and tested in a browser or API client.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Add a root endpoint (`GET /`) that returns a welcome JSON message.
- Add a health-check endpoint (`GET /health`) that returns a status such as `{"status": "ok"}`.
- Run locally with Uvicorn and respond without errors.

### 🛠️ Build Item Endpoints

#### Description
Implement REST endpoints for managing a small in-memory item collection.

#### Requirements
Completed program should:

- Define an `Item` model using Pydantic with at least `name`, `price`, and optional `in_stock` fields.
- Add endpoint `GET /items` to return all items.
- Add endpoint `GET /items/{item_id}` to return one item by id.
- Add endpoint `POST /items` to create a new item and return it.
- Return an appropriate error when an item id is not found.

### 🛠️ Add Query Filtering

#### Description
Improve your API by supporting query parameters for filtering and limiting results.

#### Requirements
Completed program should:

- Support an optional `min_price` query parameter on `GET /items`.
- Support an optional `limit` query parameter on `GET /items`.
- Return only matching items when filters are provided.
- Keep endpoint responses in valid JSON format.
