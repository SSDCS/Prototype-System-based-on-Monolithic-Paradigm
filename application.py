from Application import create_app, db
from Application.models import Admin, Astronaut
from Application.Monitoring import monitoring

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
