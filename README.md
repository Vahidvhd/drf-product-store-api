# DRF Product Store API

A REST API built with **Django** and **Django REST Framework** for managing product categories and products.

The project includes CRUD endpoints, token authentication, permission rules, serializer validation, filtering, search, ordering, pagination, Swagger/OpenAPI documentation, and Postman-tested API workflows.

---

## Overview

This API provides endpoints for working with product categories and products.

Products are linked to categories using a `ForeignKey` relationship. The API is designed with Django REST Framework `ViewSet`s and routers, making the endpoints clean and consistent.

The permission flow is:

- Anyone can view products and categories
- Authenticated users can create and update products and categories
- Authenticated users can delete products and categories

---

## Tech Stack

- Python
- Django
- Django REST Framework
- django-filter
- drf-spectacular
- SQLite
- Git and GitHub
- Postman

---

## Features

- Category CRUD API
- Product CRUD API
- DRF `ModelViewSet`
- Router-based API URLs
- Product and Category relationship
- Nested category details in product responses
- Serializer validation
- Token authentication
- DRF permission rules
- Swagger/OpenAPI documentation
- Search by name
- Filtering by category and active status
- Ordering by fields such as price and created date
- Page number pagination
- Django Admin integration

---

## Backend Concepts Covered

- REST API design
- Django models and migrations
- One-to-many relationships using `ForeignKey`
- Serializers and nested serializers
- Field-level validation
- Authentication with DRF tokens
- DRF permission classes
- OpenAPI schema generation
- API documentation with Swagger UI and Redoc
- Filtering, search, and ordering
- Pagination
- API testing with Postman
- Version control with Git and GitHub

---

## API Permissions

| Action | Permission |
|---|---|
| View categories/products | Public |
| Create categories/products | Authenticated users |
| Update categories/products | Authenticated users |
| Delete categories/products | Authenticated users |

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/token/` | Get authentication token |

### API Documentation

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/schema/` | OpenAPI schema |
| GET | `/api/docs/` | Swagger UI documentation |
| GET | `/api/redoc/` | Redoc documentation |

### Categories

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/categories/` | List categories |
| POST | `/api/categories/` | Create category |
| GET | `/api/categories/<id>/` | Retrieve category |
| PUT | `/api/categories/<id>/` | Update category |
| PATCH | `/api/categories/<id>/` | Partially update category |
| DELETE | `/api/categories/<id>/` | Delete category |

### Products

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/products/` | List products |
| POST | `/api/products/` | Create product |
| GET | `/api/products/<id>/` | Retrieve product |
| PUT | `/api/products/<id>/` | Update product |
| PATCH | `/api/products/<id>/` | Partially update product |
| DELETE | `/api/products/<id>/` | Delete product |

---

## API Documentation

Swagger UI is available at:

```txt
http://127.0.0.1:8000/api/docs/
```

Redoc documentation is available at:

```txt
http://127.0.0.1:8000/api/redoc/
```

OpenAPI schema is available at:

```txt
http://127.0.0.1:8000/api/schema/
```

---

## Example Product Request

```json
{
  "name": "Laptop",
  "price": 50000000,
  "is_active": true,
  "category": 1
}
```

## Example Product Response

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 50000000,
  "is_active": true,
  "category": 1,
  "category_detail": {
    "id": 1,
    "name": "Electronics",
    "created_at": "2026-07-09T12:00:00Z"
  },
  "created_at": "2026-07-09T12:00:00Z"
}
```

---

## Authentication

This project uses Django REST Framework token authentication.

### Get Token

```http
POST /api/token/
```

Request body:

```txt
username: your_username
password: your_password
```

Example response:

```json
{
  "token": "your_token_here"
}
```

### Use Token in Requests

Add the token to the request headers:

```txt
Authorization: Token your_token_here
```

Authenticated requests are required for create, update, and delete operations.

---

## Filtering, Search and Ordering

### Search products by name

```http
GET /api/products/?search=laptop
```

### Filter products by category ID

```http
GET /api/products/?category=1
```

### Filter active products

```http
GET /api/products/?is_active=true
```

### Order products by price

```http
GET /api/products/?ordering=price
GET /api/products/?ordering=-price
```

### Combine filters

```http
GET /api/products/?category=1&is_active=true&ordering=-price
```

---

## Pagination

The API uses page number pagination.

```http
GET /api/products/?page=1
GET /api/products/?page=2
```

Example paginated response:

```json
{
  "count": 12,
  "next": "http://127.0.0.1:8000/api/products/?page=2",
  "previous": null,
  "results": []
}
```

---

## Validation Rules

### Category

- `name` is required
- `name` must have at least 3 characters
- `name` must not exceed 100 characters

### Product

- `name` is required
- `name` must have at least 3 characters
- `name` must not exceed 100 characters
- `price` must be greater than or equal to 1
- `category` must reference an existing category

---

## Status Codes

| Status Code | Meaning |
|---|---|
| 200 OK | Successful GET, PUT, or PATCH request |
| 201 Created | Resource created successfully |
| 204 No Content | Resource deleted successfully |
| 400 Bad Request | Validation error |
| 401 Unauthorized | Authentication credentials missing or invalid |
| 403 Forbidden | User does not have permission |
| 404 Not Found | Resource not found |

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone git@github.com:Vahidvhd/drf-product-store-api.git
cd drf-product-store-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

API root:

```txt
http://127.0.0.1:8000/api/
```

Django Admin:

```txt
http://127.0.0.1:8000/admin/
```

Swagger UI:

```txt
http://127.0.0.1:8000/api/docs/
```

---

## Postman Testing Checklist

The API has been tested with Postman for the following workflows:

- Get authentication token
- List products without authentication
- Create product with token
- Update product with token
- Delete product with token
- Test validation errors
- Test search
- Test filtering
- Test ordering
- Test pagination

---

## Future Improvements

- Add automated tests
- Move sensitive settings to environment variables
- Add Docker support
- Add PostgreSQL support
- Add product image upload
- Add deployment configuration

---

## Author

**Vahid Vahedi**
