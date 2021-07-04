from Application import db
from Application import ph
from Application.models import Admin, Astronaut


hashed_password = ph.hash("12345")

admin1 = Admin(name="Anrich Potgieter", username="admin",
               email="admin@admin.com", password=hashed_password)

db.session.add(admin1)
db.session.commit()

print("Added Admin")