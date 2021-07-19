from Application import db, electrical, temperature
# creating Astronaut database models or table to store the values of the fields named below.


class Astronaut(db.Model):
    """ Define the model of Astronaut user

    Args:
        Form: Inherits the db.Model library

    Returns:
        None

    Attributes:
        id - Primary key, must be an integer
        name - Must be string of max length 30
        username - Can't be null, can be only one in the database, up to 80 characters
        email - Must be unique, can't be null and it's string of max 120 characters
        password - Password is a string of max 180 characters, can't be null
        admin_id - Integer which is an ID of admin, who created current user

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    # astronauts need to have the admin ID's that created them
    admin = db.relationship('Admin', backref=db.backref('admins'))

    #Method returning string as representation of the object
    def __repr__(self):
        return '<Astronaut %r>' % self.username

# creating Astronaut database models or table to store the values of the fields named below.


class Admin(db.Model):
    """ Define the model of Admin for database

    Args:
        Form: Inherits the db.Model library

    Returns:
        None

    Attributes:
        id - Primary key, must be an integer
        name - Must be string of max length 30
        username - Can't be null, can be only one in the database, up to 80 characters
        email - Must be unique, can't be null and it's string of max 120 characters
        password - Password is a string of max 180 characters, can't be null
        
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    #Method returning string as representation of the object
    def __repr__(self):
        return '<Admin %r>' % self.username


class Alarm_Status(db.Model):
    """ Define the model of Alarm_Status for the database

    Args:
        Form: Inherits the db.Model library

    Returns:
        None

    Attributes:
        __bind_key__ - Contains name of the database
        id - Primary key, must be an integer
        fire - Boolean, which by default is False, indicates alarm status
        electrical - Boolean, which by default is False, indicates alarm status
        temperature - Boolean, which by default is False, indicates alarm status
        oxygen - Boolean, which by default is False, indicates alarm status

    """
    __bind_key__ = 'healthDB'
    id = db.Column(db.Integer, primary_key=True)
    fire = db.Column(db.Boolean, default=False)
    electrical = db.Column(db.Boolean, default=False)
    temperature = db.Column(db.Boolean, default=False)
    oxygen = db.Column(db.Boolean, default=False)
    #Method returning string as representation of the object
    def __repr__(self):
        return '<Alarm_Status %r>' % self.fire


class Sensor(db.Model):
    """ Define the model of Sensors for the database

    Args:
        Form: Inherits the db.Model library

    Returns:
        None

    Attributes:
        __bind_key__ - Contains name of the database
        id - Primary key, must be an integer
        fire - Contains readings from topics, integer, by default set to 100
        electrical - Contains readings from topics, integer, by default set to 100
        temperature - Contains readings from topics, integer, by default set to 100
        oxygen - Contains readings from topics, integer, by default set to 100

    """
    __bind_key__ = 'healthDB'
    # hypothetically all default values will be 100, we can change this later with data from real API
    id = db.Column(db.Integer, primary_key=True)
    fire = db.Column(db.Integer, default=100)
    electrical = db.Column(db.Integer, default=100)
    temperature = db.Column(db.Integer, default=100)
    oxygen = db.Column(db.Integer, default=100)
    #method returning string as representation of the object
    def __repr__(self):
        return '<Sensor %r>' % str(self.fire)


class Overal_Status(db.Model):
    """ Define the model of Overal_Status for the database

    Args:
        Form: Inherits the db.Model library

    Returns:
        None

    Attributes:
        __bind_key__ - Contains name of the database
        id - Primary key, must be an integer
        fire - String, up to 30 characters
        electrical - String, up to 30 characters
        temperature - String, up to 30 characters
        oxygen - String, up to 30 characters

    """
    __bind_key__ = 'healthDB'
    id = db.Column(db.Integer, primary_key=True)
    fire = db.Column(db.String(30))
    electrical = db.Column(db.String(30))
    temperature = db.Column(db.String(30))
    oxygen = db.Column(db.String(30))
    #method returning string as representation of the object
    def __repr__(self):
        return '<Overal_Status %r>' % self.fire


class AlarmStatus(db.Model):
    """ Define the model of AlarmStatus for the engineering database

    Args:
        Form: Inherits the db.Model library

    Returns:
        None

    Attributes:
        __bind_key__ - Contains name of the database
        id - Primary key, must be an integer
        fire - Boolean, which by default is False, indicates alarm status
        electrical - Boolean, which by default is False, indicates alarm status
        temperature - Boolean, which by default is False, indicates alarm status
        oxygen - Boolean, which by default is False, indicates alarm status

    """
    __bind_key__ = 'engineering_db'
    id = db.Column(db.Integer, primary_key=True)
    fire = db.Column(db.Boolean, default=False)
    electrical = db.Column(db.Boolean, default=False)
    temperature = db.Column(db.Boolean, default=False)
    oxygen = db.Column(db.Boolean, default=False)
    #method returning string as representation of the object
    def __repr__(self):
        return '<Alarm_Status %r>' % self.fire


class SensorData(db.Model):
    """ Define the model of SensorsData for the engineering database

    Args:
        Form: Inherits the db.Model library

    Returns:
        None

    Attributes:
        __bind_key__ - Contains name of the database
        id - Primary key, must be an integer
        fire - Contains readings from topics, integer, by default set to 100
        electrical - Contains readings from topics, integer, by default set to 100
        temperature - Contains readings from topics, integer, by default set to 100
        oxygen - Contains readings from topics, integer, by default set to 100

    """
    __bind_key__ = 'engineering_db'
    # hypothetically all default values will be 100, we can change this later with data from real API
    id = db.Column(db.Integer, primary_key=True)
    fire = db.Column(db.Integer, default=100)
    electrical = db.Column(db.Integer, default=100)
    temperature = db.Column(db.Integer, default=100)
    oxygen = db.Column(db.Integer, default=100)
    #method returning string as representation of the object
    def __repr__(self):
        return '<Sensor %r>' % str(self.fire)


class OveralStatus(db.Model):
    """ Define the model of Sensors for the engineering database

    Args:
        Form: Inherits the db.Model library

    Returns:
        None

    Attributes:
        __bind_key__ - Contains name of the database
        id - Primary key, must be an integer
        fire - String, up to 30 characters
        electrical - String, up to 30 characters
        temperature - String, up to 30 characters
        oxygen - String, up to 30 characters

    """
    __bind_key__ = 'engineering_db'
    id = db.Column(db.Integer, primary_key=True)
    fire = db.Column(db.String(30))
    electrical = db.Column(db.String(30))
    temperature = db.Column(db.String(30))
    oxygen = db.Column(db.String(30))
    #method returning string as representation of the object
    def __repr__(self):
        return '<Overal_Status %r>' % self.fire
# db.create_all()  # it actually creates the table on the database.
