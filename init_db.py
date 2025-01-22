from app.models import Base  # Replace with your actual model file
from sqlalchemy import create_engine

def initialize_database():
    engine = create_engine("sqlite:///app.db")
    print("Dropping and recreating database tables...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database tables recreated successfully.")

if __name__ == "__main__":
    initialize_database()