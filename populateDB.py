from Application import db
from Application.models import Admin, Astronaut

admin1 = Admin(name="Anrich Potgieter", username="admin",
               email="admin@admin.com", password="12345")

db.session.add(admin1)
db.session.commit()

print("Added Admin")