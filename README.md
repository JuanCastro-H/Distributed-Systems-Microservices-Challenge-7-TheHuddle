# 🐧 Los Pingüinos del Monolito — "Streaming Beyond the Monolith" 🎬❄️

> "One service fails. The platform survives."

Distributed streaming platform architecture built with microservices, FastAPI, Docker, and PostgreSQL.

---

## 🎬 Description

This project simulates a distributed backend architecture inspired by streaming platforms like Netflix.

Instead of relying on a monolithic backend, the platform is divided into multiple autonomous microservices, where each service is responsible for a single business domain.

The system includes:

- Authentication service
- Movie catalog service
- Watchlist service
- Viewing history service

Each microservice:
- has its own database,
- exposes its own REST API,
- contains isolated business logic,
- communicates through HTTP,
- and uses JWT authentication for security.

---

## 🧠 Objective

Build a realistic distributed system to practice:

- Microservices architecture
- Distributed systems design
- REST API development with FastAPI
- JWT authentication
- Docker orchestration
- Inter-service communication
- Database isolation
- Layered backend architecture
- Service scalability and separation of concerns

---

## 🛠️ Technologies Used

### Backend
- **Python**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **Uvicorn**

### Security
- **JWT Authentication**
- **OAuth2PasswordBearer**
- **Passlib**
- **Python-Jose**

### Database
- **PostgreSQL**

### DevOps
- **Docker**
- **Docker Compose**

### Communication
- **HTTPX**

---

## 🧩 Distributed Architecture

The platform follows a distributed microservices architecture.

Each service owns:
- its own PostgreSQL database
- its own REST API
- its own business rules
- its own Docker container

No databases are shared between services.

---

## 📦 Microservices

| Service | Responsibility |
|---|---|
| Auth Service | User registration, login, JWT generation |
| Catalog Service | Manage movies and metadata |
| Watchlist Service | Store user favorite/watchlist movies |
| History Service | Store watched movie history |

---

## ⚙️ System Flow

### 🔹 General Flow

1. Users authenticate through the Auth Service
2. The Auth Service generates a JWT token
3. The token is used to access protected endpoints
4. Other services validate the JWT locally
5. Services communicate through HTTP APIs when data is required

---

## 🌐 Distributed Communication

Some services communicate dynamically with others to enrich responses.

Example:

```text
History Service
      ↓
GET /catalog/movies/{id}
      ↓
Catalog Service
      ↓
Movie information returned
```

This architecture allows:
- independent databases,
- domain separation,
- distributed data composition,
- and service scalability.

---

## 🔐 Authentication

The platform uses JWT authentication shared across all microservices.

Flow:
- `auth_service` generates JWT tokens
- other services validate the token using the same secret key

Protected requests require:

```http
Authorization: Bearer your_token
```

---

## 📂 Project Structure

```text
los-pinguinos-del-monolito/

├── auth_service/
├── catalog_service/
├── watchlist_service/
├── history_service/
│
├── docker-compose.yml
└── README.md
```

---

## 🚀 Installation

### 1. Clone repository

```bash
git clone <repository-url>
```

---

### 2. Enter project folder

```bash
cd los-pinguinos-del-monolito
```

---

### 3. Create environment variables

Environment files are required for each microservice.

For security reasons, real `.env` files are not included in the repository.

Create a `.env` file inside each service directory using the provided `.env.example` as reference.

Example structure:

```text
auth_service/
│── .env.example
│── .env

catalog_service/
│── .env.example
│── .env

watchlist_service/
│── .env.example
│── .env

history_service/
│── .env.example
│── .env
```

---

### 📄 Example `.env`

```env
DATABASE_URL=postgresql://postgres:password@auth_db:5432/auth_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

### 📌 Environment Variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key used for JWT signing |
| `ALGORITHM` | JWT encryption algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiration time |

---

### ⚠️ Important Notes

When running with Docker Compose:

- `auth_db`, `catalog_db`, etc. are Docker service hostnames
- `localhost` should only be used for local non-Docker execution

Example for Docker:

```env
DATABASE_URL=postgresql://postgres:password@auth_db:5432/auth_db
```

Example for local execution:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/auth_db
```

---

### 4. Build containers

```bash
docker compose build
```

---

### 5. Start services

```bash
docker compose up
```

---

## ▶️ Usage

After starting the containers:

| Service | URL |
|---|---|
| Auth Service | http://127.0.0.1:8001/docs |
| Catalog Service | http://127.0.0.1:8002/docs |
| Watchlist Service | http://127.0.0.1:8003/docs |
| History Service | http://127.0.0.1:8004/docs |

---

## 🔄 Example Workflow

1. Register a user
2. Login to obtain JWT token
3. Authenticate through Swagger Authorize
4. Create movies in catalog
5. Add movies to watchlist
6. Store watched movies in history
7. Retrieve enriched distributed data

---

## 🧱 Internal Architecture

Each microservice follows a layered architecture:

```text
Routes
   ↓
Services
   ↓
Repositories
   ↓
Database
```

This separation improves:
- maintainability,
- scalability,
- readability,
- and code organization.

---

## 📈 Key Features

✔ Distributed microservices architecture  
✔ JWT authentication across services  
✔ Independent PostgreSQL database per service  
✔ RESTful APIs with FastAPI  
✔ Dockerized environment  
✔ Inter-service HTTP communication  
✔ Layered architecture design  
✔ CRUD operations  
✔ Environment-based configuration  
✔ Distributed data enrichment  
✔ Error handling with HTTP exceptions  

---

## 🧃 Possible Improvements

- API Gateway implementation
- Service discovery
- Centralized logging
- Refresh tokens
- Redis caching
- Asynchronous messaging with RabbitMQ/Kafka
- Role-based authorization
- Automated testing
- CI/CD pipeline
- Kubernetes deployment
- Recommendation system

---

## 👨‍💻 Author

**Juan Castro**

---

# 🇪🇸 Resumen en Español

Los Pingüinos del Monolito es una arquitectura distribuida de microservicios inspirada en plataformas de streaming como Netflix.

El sistema divide el backend en múltiples servicios independientes encargados de diferentes dominios:
- autenticación,
- catálogo,
- watchlist,
- e historial.

Cada microservicio:
- posee su propia base de datos PostgreSQL,
- expone su propia API REST,
- utiliza JWT para autenticación,
- y funciona dentro de contenedores Docker.

---

## 🎯 Objetivo

El proyecto fue desarrollado para practicar conceptos relacionados con:

- arquitectura de microservicios,
- sistemas distribuidos,
- desarrollo de APIs REST,
- autenticación JWT,
- Docker,
- PostgreSQL,
- y comunicación entre servicios.

---

## ⚙️ Funcionamiento

- Los usuarios se autentican mediante el Auth Service
- El sistema genera tokens JWT
- Los demás servicios validan el token localmente
- Algunos microservicios se comunican entre sí vía HTTP para obtener datos adicionales
- Cada servicio mantiene independencia total sobre su lógica y datos

---

## 📊 Características destacadas

- Arquitectura distribuida
- Bases de datos independientes
- APIs REST con FastAPI
- Comunicación entre microservicios
- Autenticación centralizada con JWT
- Docker Compose para orquestación
- Arquitectura en capas
- Separación de responsabilidades

---

## 🧠 Conclusión

El proyecto demuestra cómo construir una arquitectura moderna basada en microservicios, donde cada componente funciona de forma autónoma y escalable.

Este enfoque permite:
- mejorar la mantenibilidad,
- aislar responsabilidades,
- facilitar la escalabilidad,
- y simular entornos backend reales utilizados en sistemas distribuidos modernos.