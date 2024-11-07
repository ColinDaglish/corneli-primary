[!image](/static/website/images/corneli-primary-logo.png)
# Corneli Primary

**Corneli Primary** is a Django-based web application for Corneli Primary School, providing a public-facing static website and a secure portal for parent-teacher communication. The app is designed to offer essential information for parents and students and features a parent-teacher portal accessible with a login.

---

## Features

- **Static Website**: A public-facing page where the school shares announcements, events, resources, and contact information.
- **Parent-Teacher Portal**: A secure portal for parents and teachers to communicate, view student progress, access important documents, and stay informed.
- **Modular Authentication**: Uses a submodule for handling user authentication, which provides secure access to the portal.

---

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML/CSS, JavaScript
- **Authentication**: Submodule for secure user login
- **Database**: (Specify your choice, e.g., SQLite, PostgreSQL, etc.)

---

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ColinDaglish/corneli-primary.git

2. Initialize the authentication submodule:

git submodule update --init --recursive


3. Navigate to the project directory:

cd corneli-primary


4. Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


5. Install dependencies:

pip install -r requirements.txt


6. Run database migrations:

python manage.py migrate


7. Create a superuser (for admin access):

python manage.py createsuperuser


8. Run the development server:

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the app.




---

## Usage

**Public Website:** Available at the root URL. This page provides general information for visitors and parents.

**Parent-Teacher Portal:** After logging in through the secure authentication module, parents and teachers can access the portal's features, including student reports, event information, and messaging.



---

## Configuration

1. Environment Variables:

Use a .env file to securely store environment variables.

Make sure to configure variables for database settings, secret key, and any other sensitive information.



2. Submodule Authentication:

The authentication submodule manages all user authentication and authorization. Ensure that it’s configured and up-to-date before deployment.





---

## Contributing

If you would like to contribute to this project:

1. Fork the repository.


2. Create a new branch: git checkout -b feature-name.


3. Make your changes and commit them: git commit -m 'Add some feature'.


4. Push to the branch: git push origin feature-name.


5. Submit a pull request.




---

## License

This project is licensed under the MIT License.


---

## Contact

For questions or collaboration, please contact ColinDaglish.

