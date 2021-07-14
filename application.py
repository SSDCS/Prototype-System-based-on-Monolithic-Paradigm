from Application import create_app, db
from Application.models import Admin, Astronaut
from Application.Monitoring.monitoring import Temperature, Electrial, Oxygen, Fire
from threading import Thread


app = create_app()

if __name__ == '__main__':
    t1 = Thread(target=Temperature)
    t2 = Thread(target=Electrial)
    t3 = Thread(target=Oxygen)
    t4 = Thread(target=Fire)
    t5 = Thread(target=app.run(host='0.0.0.0', port=5000, debug=True))
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t4.setDaemon(True)
    t5.setDaemon(True)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
