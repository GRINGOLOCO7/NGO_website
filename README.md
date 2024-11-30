# NGO_website
Create a website that facilitate NGO collaboration between each other




ngo-collaboration-app/
│
├── app/
│   ├── templates/          # HTML files go here
│   ├── static/             # Static files like CSS, JavaScript, images
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   ├── routes.py           # Flask routes and app logic
│   ├── __init__.py         # Initializes the Flask app
│
├── env/                    # (Optional) Virtual environment
├── requirements.txt        # Python dependencies
├── run.py                  # Entry point to start the app




python -m venv env
source env/bin/activate    # On macOS/Linux
env\Scripts\activate       # On Windows


pip install flask

pip freeze > requirements.txt


python run.py
