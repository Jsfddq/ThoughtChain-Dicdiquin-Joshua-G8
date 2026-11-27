# ThoughtChain: Connect Ideas. Build Knowledge.

## Core Features (PD2)
* **Node Management:** Create, read, update, and delete thought nodes.
* **Node Linking:** Connect related nodes together to form a chain.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your `SECRET_KEY` and `DATABASE_URL`.
6. Run migrations: `python manage.py migrate`
7. Start the server: `python manage.py runserver`
