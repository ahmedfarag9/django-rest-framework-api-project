# Django REST Framework API Project

## Description
This is a Django REST Framework API project that allows users to send requests to an ecommerce store to view products, add products to their order, and checkout their order.

The API also allows users to create a user account and has token authentication for users to login and purchase products.

The project is:
- Built with Python 3.10
- Built with Django REST Framework
- integrated with a simple flask app to test the API
- configured with unit tests
- Containerized using Docker and Docker Compose
- Deployed on Back4App container cloud hosting


## Installation
1. Clone the repository

    ```
    git clone https://github.com/ahmedfarag9/django-rest-api-project.git
    ```

2. Change the directory to the project directory

    ```
    cd django-rest-api-project
    ```

3. Create a .env file in the project directory by copying the env.template file

    ```
    cp env.template .env
    ```

4. Run the docker-compose command to build the project

    ```
    docker-compose up -d --build
    ```
    This will build the project and run the containers in the background.

