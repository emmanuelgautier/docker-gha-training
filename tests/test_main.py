import pytest
import json
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from main import app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_all_books(client):
    """Test getting all books."""
    response = client.get('/books')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, dict)
    assert len(data) >= 2  # We should have at least the initial 2 books


def test_get_book_by_id(client):
    """Test getting a specific book by ID."""
    response = client.get('/books/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == '1984'
    assert data['author'] == 'George Orwell'
    assert data['year'] == 1949


def test_get_nonexistent_book(client):
    """Test getting a book that doesn't exist."""
    response = client.get('/books/999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data


def test_add_book(client):
    """Test adding a new book."""
    new_book = {
        'title': 'Test Book',
        'author': 'Test Author',
        'year': 2023
    }
    response = client.post('/books', 
                          data=json.dumps(new_book),
                          content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Test Book'
    assert data['author'] == 'Test Author'
    assert data['year'] == 2023


def test_add_book_missing_data(client):
    """Test adding a book with missing data."""
    incomplete_book = {
        'title': 'Incomplete Book'
        # Missing author and year
    }
    response = client.post('/books',
                          data=json.dumps(incomplete_book),
                          content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data


def test_update_book(client):
    """Test updating an existing book."""
    update_data = {
        'title': 'Updated Title',
        'year': 2024
    }
    response = client.put('/books/1',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'Updated Title'
    assert data['year'] == 2024
    assert data['author'] == 'George Orwell'  # Should keep original author


def test_update_nonexistent_book(client):
    """Test updating a book that doesn't exist."""
    update_data = {'title': 'Updated Title'}
    response = client.put('/books/999',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == 404


def test_delete_book(client):
    """Test deleting a book."""
    response = client.delete('/books/2')
    assert response.status_code == 204


def test_delete_nonexistent_book(client):
    """Test deleting a book that doesn't exist."""
    response = client.delete('/books/999')
    assert response.status_code == 404
