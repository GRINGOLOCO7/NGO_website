# NGO_website
Create a website that facilitate NGO collaboration between each other

## Our Mission

In our Synergy class we explore the challenges faced by non-profit orgaization every day. We come up with an idea of a platform that takle 3 main issues:

1. Supprt ([chat.html](https://github.com/GRINGOLOCO7/NGO_website/blob/main/app/templates/chat.html)): Trough open comunity, we implement in our website an interconnected platform where NGOs can comunicate with each other, organize, ask for help, and more. This section is a sort of NGO whatsup

2. Burocracy ([government.html](https://github.com/GRINGOLOCO7/NGO_website/blob/main/app/templates/government.html)): NGOs fight against burocracy and governament rules every day. Have all paper work done is a very time expensive taks. In our website, NGOs can find and uplad templates on how to skip this process faster

3. Delivery ([delivery.html](https://github.com/GRINGOLOCO7/NGO_website/blob/main/app/templates/delivery.html)): Delivery merchandise is expensive and continuous task. Moving materials and commodities is costly inefficient for NGOs. Here we offer a platform to share similar routes with same truck to decrease costas and increase frequency. Point of departure and point of delivery are inputed and the algorithm matck similar desire routes togheter, connecting NGOs in close collaboration.

---
In the home page ([index.html](https://github.com/GRINGOLOCO7/NGO_website/blob/main/app/templates/index.html)) the 3 containers are in this form:

```
+----------------------+
|       (Map)          |
|                      |
+----------------------+
|    Delivery Routes   |
+----------------------+
| Descriptive Text     |
|                      |
+----------------------+
|      Button          |
+----------------------+
```
You can then press the button to rederect to the desire service.

---

## File structure
```
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
```




---

## Run code
```bash
python -m venv env
source env/bin/activate    # On macOS/Linux
env\Scripts\activate       # On Windows
```


```bash
pip install flask
pip freeze > requirements.txt
```


```bash
source env/Scripts/activate
python NGO_website/run.py
```
