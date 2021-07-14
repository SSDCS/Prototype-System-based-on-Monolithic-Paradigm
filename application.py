from Application import create_app, db
from Application.models import Admin, Astronaut


app = create_app()

if __name__ == '__main__':
    target = app.run(host='0.0.0.0', port=5000, debug=False)
