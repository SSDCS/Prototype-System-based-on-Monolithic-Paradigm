from Application import db, bcrypt
from Application.models import Admin, Astronaut


hashed_password = bcrypt.generate_password_hash("12345")

admin1 = Admin(name="Anrich Potgieter", username="admin",
               email="admin@admin.com", password=hashed_password)

db.session.add(admin1)
db.session.commit()

print("Added Admin")