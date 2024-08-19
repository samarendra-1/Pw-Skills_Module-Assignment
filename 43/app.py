from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    db.create_all()


if __name__ == '__main__':
    if not app.debug:
        # Optional: Seed the database with initial data (if desired)
        pass
    app.run()



user = User(username='admin', email='admin@example.com')
db.session.add(user)
db.session.commit()


users = User.query.all()  # Get all users
user = User.query.get(1)  # Get a user by ID

db.session.delete(user)
db.session.commit()

