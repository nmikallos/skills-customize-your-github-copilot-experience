"""Starter code for Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Assignment API")


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# In-memory storage for this assignment.
items: dict[int, Item] = {
    1: Item(name="Notebook", price=4.99, in_stock=True),
    2: Item(name="Headphones", price=24.50, in_stock=False),
}
next_item_id = 3


# TODO: Task 1 - Add GET / endpoint that returns a welcome message.


# TODO: Task 1 - Add GET /health endpoint that returns {"status": "ok"}.


# TODO: Task 2/3 - Add GET /items endpoint with optional min_price and limit query params.


# TODO: Task 2 - Add GET /items/{item_id} endpoint.


# TODO: Task 2 - Add POST /items endpoint.
# Hint: remember to declare `global next_item_id` when incrementing the id.


# Optional: Run locally with:
# uvicorn starter-code:app --reload
