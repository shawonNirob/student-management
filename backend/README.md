# FastAPI Backend for Student Management System

## Overview

Welcome to the Student Information Management System This backend service is built with [FastAPI](https://fastapi.tiangolo.com/), MySQL database and integrates with a fine-tuned [OpenAI](https://openai.com/) model to provide AI-assisted functionalities for managing student data.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete student records.
- **AI-Powered Queries**: Interact with the student database using natural language.
- **Dockerized Setup**: Simplified deployment and environment management with Docker Compose.

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:shawonNirob/student-management.git
cd student-management/backend
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv

# Activate the virtual environment
# On Unix or MacOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

### 1. Create a `.env` File

Create a `.env` file in the `backend/` directory based on the provided example.

```bash
cp .env.example .env
```

Edit the `.env` file to include your specific configuration:

```
DATABASE_URL=mysql+pymysql://root:Admin123!@db:3306/student
OPENAI_API_KEY=your-api-key
MODEL_ID=your-fine-tuned-model-id
```

### 2. Docker Compose

The project includes a `docker-compose.yml` file to manage the backend and MySQL database services with a backup.sql file.

#### Start Services

```bash
docker-compose up --build
```

#### Access the Application

- **API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Root Endpoint:** [http://localhost:8000/](http://localhost:8000/)

## Running Without Docker

If you prefer running the application locally without Docker:

1. **Ensure MySQL is Installed and Running:**

   - Create a database named `student`.
   - Update the `DATABASE_URL` in the `.env` file if necessary.

2. **Apply AlembicMigrations:**

   ```bash
   alembic upgrade head
   ```

3. **Start the Server:**

   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- **Create a New Student:** `POST /students/`
- **Get All Students:** `GET /students/`
- **Get a Student by ID:** `GET /students/{student_id}`
- **Update a Student by Contact Number:** `PUT /students/{contact_number}`
- **Delete a Student by ID:** `DELETE /students/{student_id}`
- **AI-Asistant Query:** `POST /ai/ask`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any questions or support, please contact [sarowarnirob21@gmail.com](mailto:sarowarnirob21@gmail.com).
```
