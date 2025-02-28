from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base  # Updated import here

app = Flask(__name__, 
           static_folder='static',
           template_folder='templates')

# Database Configuration (Replace with your actual credentials)
DB_HOST = "localhost"  # Or your PostgreSQL server address
DB_NAME = "student_app_db"
DB_USER = "postgres"  # Replace with your PostgreSQL username
DB_PASSWORD = "postgres" # Replace with your PostgreSQL password
DB_PORT = "5432"  # Default port for PostgreSQL

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define the student_info table using SQLAlchemy's Table object (Core)
# student_info_table = Table(
#     'student_info', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(255), nullable=False),
#     Column('email', String(255))
# )

# Alternatively, you could use SQLAlchemy ORM (Declarative Base) to define the table as a class:
Base = declarative_base()
class StudentInfo(Base):
    __tablename__ = 'student_info'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255))
Base.metadata.bind = engine # Bind metadata to the engine


Session = sessionmaker(bind=engine) # Create a session factory

# Add route for the main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    """Handles form submission, inserts data into the database using SQLAlchemy."""
    data = request.form  # Get data from the form

    name = data.get('name')
    email = data.get('email')

    if not name:
        return jsonify({'message': 'Name is required'}), 400  # Bad request

    session = Session() # Create a session instance
    try:
        # Using SQLAlchemy Core (Table object)
        # stmt = insert(student_info_table).values(name=name, email=email)
        # session.execute(stmt)
        # session.commit()  # Save changes to the database

        # If you used SQLAlchemy ORM (Declarative Base), it would look like this:
        new_student = StudentInfo(name=name, email=email)
        session.add(new_student)
        session.commit()

        session.close()
        return jsonify({'message': 'Data submitted successfully!'}), 201 # Created
    except Exception as e: # Catch any potential exceptions during database operation
        session.rollback() # Rollback transaction in case of error
        session.close()
        print(f"Database error: {e}")
        return jsonify({'message': 'Database error occurred'}), 500 # Internal Server Error


if __name__ == '__main__':
    app.run(debug=True) # Run the Flask app in debug mode (for development)
