from Application import create_app, db
from Application.models import Admin, Astronaut

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
