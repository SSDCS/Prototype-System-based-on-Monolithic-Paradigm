# Prototype-System-based-on-Monolithic-Paradigm

- [Prototype-System-based-on-Monolithic-Paradigm](#prototype-system-based-on-monolithic-paradigm)
  - [Secure Software Development Practices](#secure-software-development-practices)
    - [Architectural Patterns](#architectural-patterns)
      - [Model View Controller](#model-view-controller)
    - [Design Patterns](#design-patterns)
      - [Flask Blueprints](#flask-blueprints)
      - [Flask Application Factory](#flask-application-factory)
    - [Regular Expressions](#regular-expressions)
    - [Python Linters](#python-linters)
    - [Cryptography](#cryptography)
  - [Dependencies](#dependencies)
  - [Run Application](#run-application)
    - [VirtualBox Environement](#virtualbox-environement)
    - [Run VirutalBox](#run-virutalbox)
      - [Login to Virutal Box](#login-to-virutal-box)
      - [Run Application](#run-application-1)
  - [References](#references)

## Secure Software Development Practices

### Architectural Patterns

#### Model View Controller

Flask provides a concise foundation for the model view controller architecture. The models.py (Model) file represents the database tables within the system, while the templates (Views) create a graphical user interface that the user will engage with. Finally, the routes.py (Controller) files found in each blueprint provide a means of controlling the data in the database (RealPython.com, 2021).

### Design Patterns

#### Flask Blueprints

Flask blueprints create a means of creating modular applications by segmenting the code into logical units. This application uses blueprints to create logical boundaries within the application for routes such as authentication, dashboard and engineering (Flask, 2021b).

#### Flask Application Factory

The Flask application factory pattern is used in conjunction with the blueprints. The application factory helps generate multiple instances of the same application, which is particularly useful when performing testing with various application configurations (Flask, 2021a).

### Regular Expressions

A regular expression is used within the [registration form](https://github.com/SSDCS/Prototype-System-based-on-Monolithic-Paradigm/blob/397957b8d7a8bf0efce3af271fa4c22cb4214bea/Application/auth/forms.py). The expression prevents passwords weak passwords. User passwords must be at least eight characters long and include an uppercase, lowercase and a number (OWASP, 2021a).

### Python Linters

This project was run through pylint in accordance with the PEP8 style guide. Where pylint suggestions were made, the code was adjusted accordingly. In the rare case where a suggestion was not followed, the suggestions/warnings were suppressed (Logilab, 2021).

### Cryptography

The [argon2-cffi](https://pypi.org/project/argon2-cffi/) hashing library was used in accordance with the guidance provided by the OWASP Password Storage cheatsheet (OWASP, 2021b). Argon2 is often noted for winning the [2015 password hashing Competition](https://www.password-hashing.net/).

## Dependencies

```Terminal
pip install -r requirements.txt
```

## Run Application

### VirtualBox Environement

- Download [Virutal Box](https://www.virtualbox.org/wiki/Downloads)
- Download the [Virutal Box Image](https://drive.google.com/file/d/1STtKbEz8T6c1mDOCOmvEu0kT21R6xxkV/view?usp=sharing)

- Extract project and re-create virutal machine in your local environment

### Run VirutalBox

#### Login to Virutal Box

```Terminal
Username: ssdcs
Password: software
```

```Terminal
cd Prototype-System-based-on-Monolithic-Paradigm
```

```Terminal
git pull
```

```Terminal
source venv/bin/activate
```

#### Run Application

```Terminal
python3 run.py
```

## References

Flask (2021a) Application Factories. Available at: [https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/](https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/) (Accessed: 18 July 2021).

Flask (2021) Modular Applications with Blueprints. Available at: [https://flask.palletsprojects.com/en/2.0.x/blueprints/](https://flask.palletsprojects.com/en/2.0.x/blueprints/) (Accessed: 18 July 2021).

Logilab (2021) Pylint - code analysis for Python | www.pylint.org. Available at: [https://www.pylint.org/](https://www.pylint.org/) (Accessed: 18 July 2021).

OWASP (2021) Authentication - OWASP Cheat Sheet Series. Available at: [https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#implement-proper-password-strength-controls](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#implement-proper-password-strength-controls) (Accessed: 18 July 2021).

OWASP (2021b) Password Storage - OWASP Cheat Sheet Series. Available at: [https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#argon2id](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#argon2id) (Accessed: 18 July 2021).

RealPython.com (2021) Model-View-Controller (MVC) Explained – With Legos – Real Python. Available at: [https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/) (Accessed: 18 July 2021).
