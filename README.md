# Data4Good Webapp

## Overview
An interface for German politicians to analyze climate and socioeconomic metrics in their districts. The application provides data visualization and insights to support informed decision-making.

## Prerequisites
- Python 3.8+
- pip
- Git

## Installation

1. Clone the repository
```bash
git clone https://github.com/ChangeByteByByte/webapp.git
cd webapp
```

2. Create and activate virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Configuration
1. Create `.env` file in the project root
2. Add required environment variables (contact administrator for values):
```
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=your_database_url
```

## Running the Application
1. Ensure your virtual environment is activated
2. Start the Flask development server:
```bash
flask run
```
3. Access the application at `http://localhost:5000`

## Development
- Format code: `black .`
- Lint code: `flake8`

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License
[MIT License](LICENSE)

## Contact
For support or queries, please contact [Project Manager Name] at [email]