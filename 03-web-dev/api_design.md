# Sample Web API Design

This document shows how a simple e‑commerce API could support the Fruta e Pan and Burger My Bun applications.

## Core endpoints

### Products

- `GET /api/products`
  - Returns a list of available products (name, description, price, category, is_available).
- `GET /api/products/{id}`
  - Returns details for a single product.
- `POST /api/products`
  - Admin-only: create a new product.
- `PUT /api/products/{id}`
  - Admin-only: update product information.
- `DELETE /api/products/{id}`
  - Admin-only: soft-delete or deactivate a product.

### Orders

- `POST /api/orders`
  - Creates a new order from a cart:
  - Request body includes customer info, line items, and payment metadata.
- `GET /api/orders/{id}`
  - Returns order status and summary.
- `GET /api/orders?customer_id={id}`
  - Returns recent orders for a specific customer.

### Authentication

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`

## Deployment idea

- Frontend (Fruta e Pan / Burger My Bun) served from S3 + CloudFront or a static host.
- Backend API deployed on AWS (EC2, ECS, or Lambda + API Gateway).
- Logs forwarded to CloudWatch for monitoring; API metrics used to trigger scaling events.
