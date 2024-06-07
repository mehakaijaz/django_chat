# ChatApp README

## Overview
ChatApp is a real-time chat application designed to provide instant messaging capabilities. The application leverages the power of Django for backend functionality, Django Channels for real-time communication, and web technologies like Bootstrap, HTML, CSS, and JavaScript for a responsive and user-friendly frontend.

## Technologies Used
### Backend
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Frontend
- **Bootstrap**: A popular CSS framework for developing responsive and mobile-first websites.
- **HTML**: The standard markup language for creating web pages.
- **CSS**: A stylesheet language used for describing the presentation of a document written in HTML.
- **JavaScript**: A programming language that enables interactive web pages.

## Installation and Setup

### Prerequisites
- Python 
- Django

### Backend Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/mehakaijaz/django_chat.git
   cd chat
   ```

2. **Install the required Python packages:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Apply database migrations:**
   ```sh
   python manage.py migrate
   ```

4. **Create a superuser to access the admin interface:**
   ```sh
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

### Frontend Setup
The frontend uses static files managed by Django. Ensure that the static files are correctly configured and collected.

1. **Collect static files:**
   ```sh
   python manage.py collectstatic
   ```

2. **Access the application:**
   Open your web browser and navigate to `http://localhost:8000` to start using ChatApp.

## Usage

### Authentication
- **Register**: Create a new account to start chatting.
- **Login**: Access your account by logging in with your credentials.

### Messaging
- **Chat**: Start a new conversation by selecting a user or joining an existing chat room.
- **Real-Time Updates**: Enjoy real-time messaging with WebSockets.

## Project Structure
- `chatapp/`: Main project directory.
  - `settings.py`: Configuration for the Django project.
  - `urls.py`: URL routing for the project.
  - `wsgi.py`: WSGI entry point for the application.
  - `asgi.py`: ASGI entry point for the application.
- `chat/`: App directory containing the chat application.
  - `models.py`: Database models for the chat application.
  - `urls.py`: URL routing for the chat application.
  - `views.py`: Views for handling HTTP requests.
- `manage.py`: Command-line utility for administrative tasks.
- `templates/`: HTML templates for rendering the frontend.
- `static/`: Static files (CSS, JavaScript, images).
