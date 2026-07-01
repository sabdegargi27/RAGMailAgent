# Cold Email App - Docker Setup

This application is containerized with separate containers for frontend and backend.

## Architecture

- **Backend**: FastAPI application running on port 8000
- **Frontend**: React application running on port 3000
- **Network**: Both containers communicate via a Docker network

## Quick Start

### Using Docker Compose (Recommended)

1. **Build and run both containers:**
   ```bash
   docker-compose up --build
   ```

2. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000

3. **Stop the containers:**
   ```bash
   docker-compose down
   ```

### Individual Container Commands

#### Backend Only
```bash
# Build backend container
docker build -t cold-email-backend ./backend

# Run backend container
docker run -p 8000:8000 cold-email-backend
```

#### Frontend Only
```bash
# Build frontend container
docker build -t cold-email-frontend ./frontend/cold-email

# Run frontend container
docker run -p 3000:3000 cold-email-frontend
```

## Development Mode

For development with hot reloading:

```bash
# Backend development
docker-compose up backend

# Frontend development (run locally)
cd frontend/cold-email
npm start
```

## Production Deployment

1. **Build production images:**
   ```bash
   docker-compose -f docker-compose.yml build
   ```

2. **Run in production:**
   ```bash
   docker-compose -f docker-compose.yml up -d
   ```

## Benefits of Separate Containers

- ✅ Independent scaling of frontend/backend
- ✅ Different update cycles
- ✅ Better resource management
- ✅ Easier development workflow
- ✅ Better security isolation
- ✅ Technology-specific optimizations

## Troubleshooting

### Port Conflicts
If ports 3000 or 8000 are already in use, modify the `docker-compose.yml` file to use different ports.

### Build Issues
- Ensure Docker and Docker Compose are installed
- Clear Docker cache: `docker system prune -a`
- Rebuild: `docker-compose build --no-cache`

### Network Issues
- Check if containers can communicate: `docker network ls`
- Inspect network: `docker network inspect cold-email_cold-email-network` 