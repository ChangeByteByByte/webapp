from app import create_app, db
from app.utils import load_data

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        load_data()  # This will load your CSV data into the database
    app.run(debug=True)