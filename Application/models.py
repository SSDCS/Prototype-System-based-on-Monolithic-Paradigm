from Application import db, electrical, temperature
# creating Astronaut database models or table to store the values of the fields named below.


class Astronaut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    # astronauts need to have the admin ID's that created them
    admin = db.relationship('Admin', backref=db.backref('admins'))

    def __repr__(self):
        return '<Astronaut %r>' % self.username

# creating Astronaut database models or table to store the values of the fields named below.


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)

    def __repr__(self):
        return '<Admin %r>' % self.username


class Alarm_Status(db.Model):
    __bind_key__ = 'healthDB'
    id = db.Column(db.Integer, primary_key=True)        
    fire=db.Column(db.Boolean, default=False)
    electrical=db.Column(db.Boolean, default=False)
    temperature=db.Column(db.Boolean, default=False)
    oxygen=db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Alarm_Status %r>' % self.fire

class Sensor(db.Model):
    __bind_key__ = 'healthDB'
    #hypothetically all default values will be 100, we can change this later with data from real API
    id = db.Column(db.Integer, primary_key=True)        
    fire=db.Column(db.Integer, default=100)
    electrical=db.Column(db.Integer, default=100)
    temperature=db.Column(db.Integer, default=100)
    oxygen=db.Column(db.Integer, default=100)

    def __repr__(self):
        return '<Sensor %r>' % str(self.fire)
    
class Overal_Status(db.Model):
    __bind_key__ = 'healthDB'
    id = db.Column(db.Integer, primary_key=True)        
    fire=db.Column(db.String(30))
    electrical=db.Column(db.String(30))
    temperature=db.Column(db.String(30))
    oxygen=db.Column(db.String(30))

    def __repr__(self):
        return '<Overal_Status %r>' % self.fire

class AlarmStatus(db.Model):
    __bind_key__ = 'engineering_db'
    id = db.Column(db.Integer, primary_key=True)        
    fire=db.Column(db.Boolean, default=False)
    electrical=db.Column(db.Boolean, default=False)
    temperature=db.Column(db.Boolean, default=False)
    oxygen=db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Alarm_Status %r>' % self.fire
class SensorData(db.Model):
    __bind_key__ = 'engineering_db'
    #hypothetically all default values will be 100, we can change this later with data from real API
    id = db.Column(db.Integer, primary_key=True)        
    fire=db.Column(db.Integer, default=100)
    electrical=db.Column(db.Integer, default=100)
    temperature=db.Column(db.Integer, default=100)
    oxygen=db.Column(db.Integer, default=100)

    def __repr__(self):
        return '<Sensor %r>' % str(self.fire)

class OveralStatus(db.Model):
    __bind_key__ = 'engineering_db'
    id = db.Column(db.Integer, primary_key=True)        
    fire=db.Column(db.String(30))
    electrical=db.Column(db.String(30))
    temperature=db.Column(db.String(30))
    oxygen=db.Column(db.String(30))

    def __repr__(self):
        return '<Overal_Status %r>' % self.fire
# db.create_all()  # it actually creates the table on the database.
