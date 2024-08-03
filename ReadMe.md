# Advance E-Commerece API project
Author: Sara Angsioco
Date: 8/2/2024
NOTE: Python files are the same from Lesson 1 - Lesson 5. Albeit the following files were updated to satify the requirement of the project.

•	Updated customerController, customerService, customerBP
•	Updated customerAccountController, customerAccountService, customerAccountBP
•	Updated productController, productService, productBP
•	Updated orderController, orderBP
•	Updated app.py change limit from 5 to 100 in line 64

Overview:
The E-Commerce API provides a comprehensive set of endpoints for managing and interacting with an e-commerce platform. 
It supports essential operations for handling customers, customer accounts, products, orders, ordered products and employee.

File Structure:
C:.
|   .env
|   .gitignore
|   app.py
|   caching.py
|   config.py
|   database.py
|   file_structure.txt
|   limiter.py
|   requirements.txt
|   schema.py
|   
+---controllers
|   |   customerAccountController.py
|   |   customerController.py
|   |   employeeController.py
|   |   orderController.py
|   |   productController.py
|   |   productionController.py
|   |   __init__.py
|   |   

+---models
|   |   customer.py
|   |   customerAccount.py
|   |   customerManagementRole.py
|   |   employee.py
|   |   order.py
|   |   orderProduct.py
|   |   product.py
|   |   production.py
|   |   role.py
|   |   __init__.py
|   |   
|   +---schemas
|   |   |   customerAccountSchema.py
|   |   |   customerSchema.py
|   |   |   employeeSchema.py
|   |   |   orderSchema.py
|   |   |   productionSchema.py
|   |   |   productSchema.py
|   |   |   __init__.py
|   |   |             
+---routes
|   |   customerAccountBP.py
|   |   customerBP.py
|   |   employeeBP.py
|   |   orderBP.py
|   |   productBP.py
|   |   productionBP.py
|   |   __init__.py
     
+---services
|   |   customerAccountService.py
|   |   customerService.py
|   |   employeeService.py
|   |   orderService.py
|   |   productionService.py
|   |   productService.py
|   |   __init__.py
|   |   
         
+---static
|       swagger.yaml
|             
+---tests
|       test_customer.py
|       test_emplyee.py
|       test_order.py
|       test_product.py
|       test_production.py
|       __init__.py
|       
+---utils
|   |   util.py

Features
•	Customer Management
  o	Create Customer: Register a new customer with personal details.
  o	Retrieve Customer: Get information about a specific customer.
  o	Update Customer: Modify existing customer information.
  o	Delete Customer: Remove a customer from the system.
•	Product Management
  o	Add Product: Introduce a new product to the inventory.
  o	Get Product Details: Retrieve information about a specific product.
  o	Update Product: Update product details such as price and description.
  o	Delete Product: Remove a product from the inventory.
•	Order Management
  o	Create Order: Place a new order with selected products and quantities.
  o	Get Order Details: Access details about a specific order.
  o	Update Order: Modify the status or details of an existing order.
  o	Cancel Order: Cancel an existing order before it's processed.
•	Authentication and Authorization
  o	User Login: Authenticate users with their credentials.
  o	User Registration: Register new users for access to the platform.
  o	Password Reset: Facilitate password recovery for users.

Installation:
1. Clone the Module 13 MiniProject repository
2. Create a virtual environment if needed (python -m venv venv)
   2a. Activate the virtual environment
3. Install all required dependencies provided in requirements.txt
4. Run app.py
