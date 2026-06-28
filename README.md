# Restaurant Management System Backend API ###

A backend REST API for managing restaurant operations including orders, menu items, tables, reservations, inventory tracking, and automated stock deduction. Built with Django and Django REST Framework.

---

## Features

### Core Modules
- Menu management (categories and menu items)
- Order processing system (orders and order items)
- Table management for dine-in operations
- Reservation system for customers
- Inventory tracking with automatic stock deduction
- Recipe management linking menu items to inventory usage

### Business Logic
- Automatic inventory deduction when an order is processed
- Stock validation before order confirmation
- Order status workflow (Pending, Preparing, Ready, Served)
- Payment status tracking
- Price snapshot system for order items to preserve historical pricing

### API Features
- RESTful API built with Django REST Framework
- Standardized API response structure
- Read/write serializer separation for optimized frontend consumption
- Custom viewset architecture for consistent response handling
- Nested relationship support for detailed data retrieval

---

## Tech Stack

- Python 3.13+
- Django 6.x
- Django REST Framework
- SQLite (development) / PostgreSQL (production-ready)
- Django Admin (customized)

---

## Project Architecture

### Main Apps
- `menu` – Menu categories and menu items
- `order` – Orders and order items
- `inventory` – Stock tracking and inventory management
- `recipe` – Links menu items to required inventory ingredients
- `table` – Restaurant table management
- `user` – Staff and authentication management

---

## Key Design Decisions

### Inventory Management
Each menu item is linked to multiple inventory items via recipes.  
Inventory is deducted based on recipe requirements when an order enters the **PREPARING** state.  
Pre-check ensures sufficient stock before deduction using atomic transactions.

### Order System
- Orders contain multiple order items
- Each order item stores a price snapshot at the time of purchase
- Subtotals are computed dynamically

### Pricing Strategy
- `MenuItem.price` represents current selling price
- `OrderItem.price` stores historical price at time of order
- Prevents inconsistencies when menu prices change over time

---

## API Overview

### Menu

- `GET /api/menu/` – List menu items
- `POST /api/menu/` – Create menu item
- `GET /api/menu/{id}/` – Retrieve menu item

---

### Orders

- `GET /api/orders/` – List orders
- `POST /api/orders/` – Create order
- `PATCH /api/orders/{id}/` – Update order status

---

### Order Items

- `GET /api/order-items/`
- `POST /api/order-items/`
- `DELETE /api/order-items/{id}/`

---

### Inventory

- `GET /api/inventory/`
- `POST /api/inventory/`
- `PATCH /api/inventory/{id}/`

---

## Order Workflow

1. Order is created with order items
2. Order status is set to `PENDING`
3. When status changes to `PREPARING`:
   - System checks inventory availability
   - System deducts required stock based on recipes
4. Order proceeds to `READY` and `SERVED`

---

## Inventory Logic

- Each menu item is linked to recipes
- Each recipe defines required inventory quantities
- System calculates total required stock per order
- Deduction is performed atomically using database transactions
- Prevents negative stock and race conditions

---

## Installation

### 1. Clone repository

```bash
git clone https://github.com/jhamez-cloud/CodeAlpha_RestaurantManagementSystem_Backend.git
cd restaurant-management-system