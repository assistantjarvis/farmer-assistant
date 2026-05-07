# Crop Prediction UI

A lightweight Flask-based web UI for uploading crop/dataset CSVs, previewing data,
requesting simple weather forecasts (via OpenWeatherMap), and interacting with
crop prediction utilities included in this repository.

## Features
- Web UI for uploading CSV datasets and previewing them
- Simple forecast lookup using OpenWeatherMap API
- Crop prediction helpers and mappings used by the backend
- Basic authentication (default development credentials: `admin` / `admin`)

## Tech stack
- Python (3.8+)
- Flask
- pandas, numpy
- scikit-learn (models/helpers present in repo)
- matplotlib (used in some analysis helpers)
- requests

## Quick start

1. Create and activate a virtual environment (Windows example):

```powershell
python -m venv venv
venv\Scripts\activate
```

2. Install required packages (no `requirements.txt` included — install common deps):

```powershell
pip install flask pandas scikit-learn matplotlib requests
```

3. Run the app (Windows CMD):

```cmd
set FLASK_APP=main.py
set FLASK_ENV=development
flask run
```

Or using Python directly:

```cmd
python -m flask run
```

The app will be available at http://127.0.0.1:5000 by default.

## Usage
- Open the app in your browser and log in (username: `admin`, password: `admin`).
- Use the `Upload` page to upload a CSV (saved into the `uploads/` folder).
- After uploading you can preview the data via the `Preview` page.
- Use the Forecast page to fetch a weather forecast by location (requires working
  internet and the OpenWeatherMap API key included in `main.py`).

## Important files
- [main.py](main.py) — Flask application and routes.
- [crop-final.py](crop-final.py) — (auxiliary) crop prediction scripts.
- [users.py](users.py) — user-related helpers.
- `uploads/` — destination for uploaded CSVs (example datasets included).
- `templates/` — HTML templates used by the Flask app (index, upload, preview, etc.).
- `static/` — static assets (CSS/JS/images) used by templates.

## Notes & next steps
- The repository includes an OpenWeatherMap API key in `main.py`; consider
  replacing it with an environment variable for production use.
- There is no `requirements.txt` or `setup.py`; consider adding one for
  reproducible installs.
- `main.py` defines `app = Flask(__name__)` but does not include an explicit
  `if __name__ == '__main__': app.run()` guard — running via `flask run`
  is the simplest approach.

## Contributing
Feel free to open issues or submit PRs. For quick improvements, consider:
- adding a `requirements.txt`
- adding tests and a basic CI workflow
- securing secrets (move API keys to environment variables)

## License
This project currently has no explicit license. Add a `LICENSE` file to clarify
permissions for reuse.
