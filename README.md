# Docker GHA Training

The goal of this training is to learn how to use Docker and GitHub Actions to build, test and deploy a simple web application. In this training, we will use a simple web application written in Python and Flask.

## Project Structure

- `app/` - Flask application
- `myapp/` - Docker Compose configuration
- `tests/` - Unit tests
- `.github/workflows/` - GitHub Actions workflows

## GitHub Actions Workflows

### 1. Docker Build and Push (`docker-build-push.yml`)

This workflow:
- Triggers on pushes to `main` and pull requests
- Builds Docker image for all branches
- **Pushes image only if branch is `main`**
- Uses Docker Hub as registry
- Supports multi-architecture (amd64, arm64)
- Uses GitHub Actions cache to optimize builds

**Required secret variables:**
- `DOCKER_USERNAME` - Docker Hub username
- `DOCKER_PASSWORD` - Docker Hub access token

### 2. Build and Test (`build-test.yml`)

This workflow:
- Triggers on pushes to `main`/`develop` and pull requests
- Tests application with multiple Python versions (3.11, 3.12)
- Uses PostgreSQL database for testing
- Performs linting with flake8
- Runs tests with pytest and generates coverage report
- Builds and tests Docker image

## Local Setup

### Prerequisites
- Docker and Docker Compose
- Python 3.11+

### Launch with Docker Compose
```bash
cd myapp
docker-compose up -d
```

The application will be accessible at `http://localhost:8080`

### Local Testing
```bash
pip install -r requirements.txt
pip install pytest pytest-cov flake8
pytest
```

## API Endpoints

- `GET /books` - List all books
- `GET /books/{id}` - Retrieve a book by ID
- `POST /books` - Add a new book
- `PUT /books/{id}` - Update a book
- `DELETE /books/{id}` - Delete a book

## Security Configuration

- PostgreSQL passwords are stored in Docker secrets
- Docker Hub tokens are stored in GitHub secrets
- Docker images are scanned for vulnerabilities


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
