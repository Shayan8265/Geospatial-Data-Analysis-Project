# Geospatial Data Analysis Tool

A Python tool for efficient geospatial data querying and processing, vital for environmental monitoring and urban planning. Key features include dynamic WCPS query generation and lazy evaluation for optimal performance. It allows flexible query customization, meeting diverse analysis requirements.

## Usage

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Explore and run scripts in the `src/` directory.

## Code Overview

- `database_connection.py`: Manages connections to the WCPS server (class in `classes.py`).
- `datacube.py`: Interacts with the WCPS server and performs datacube operations (class in `classes.py`).
- `main.py/`: Contains implementation and unit tests for `DatabaseConnection` and `Datacube` classes.
- `docs/`: Documentation including docstrings and user training material.
