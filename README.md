# Project 2

Our project aims to predict traffic congestion and optimize route suggestions in real-time using historical traffic and weather data. By leveraging machine learning models, the system forecasts traffic conditions and travel times, while also offering optimized routes to avoid congestion. The solution integrates real-time data and weather conditions to dynamically adjust routes, providing smarter navigation for commuters, delivery services, and smart city applications.

**Purpose** This project uses machine learning and data science to address transportation challenges, enhancing traffic management and route optimization. By leveraging real-time traffic and weather data, the solution aims to improve travel efficiency and reduce congestion, contributing to smarter urban mobility.

## Code Style and Formatting

This project follows standardized code formatting and linting rules to ensure consistency across the codebase. The tools used for this are **Black** (auto-formatter) and **Flake8** (linter).

### Setup Guide

**Create Developing Environment**

- Conda will house all the necessary packages and versioning for easy start up for development

````bash
conda create --name project_2 --file requirements.txt
```

- To active the new conda environment

```bash
conda activate project_2
```

#### Pre Commit Cleaning

1. **Black** - Code Formatter:
- Black automatically formats the code to comply with the PEP 8 style guide.
- Configuration: `pyproject.toml` (Line length: 79 characters)
2. **Flake8** - Linter:
- Flake8 checks the code for style violations and provides feedback.
- Configuration: `.flake8` (Line length: 79 characters, excluding certain warnings)

### Install Dependencies

Run command to install any remaining dependencies

```bash
pip install -r requirements.txt
````

### Code Style and Formatting

- **Black**: Code formatter for PEP 8 compliance.

  - [Black](https://black.readthedocs.io/en/stable/)

- **Flake8**: Linter for enforcing coding standards.

  - [Flake8](https://flake8.pycqa.org/en/latest/)

- **Mypy**: Static type checker for Python.

  - [Mypy](http://mypy-lang.org/)

- Black: To format the code, run the following command:

```bash
black .
```

- Flake8: To lint the code, run the following command:

```bash
flake8 .
```

- Pre-commit: Run the install command:
  **Hooks will automatically run Black and Flake8 on staged files during commits.**

```bash
pre-commit install
```

- After setting this up, Black and Flake8 will automatically run on staged files before each commit. This ensures code consistency and quality before pushing changes to the repository.

## Tech Stack

### Data

- **OpenStreetMap (OSM)**: Provides geographic data (roads, intersections, routing).

  - [OpenStreetMap](https://www.openstreetmap.org/)
  - [Auth URL](https://master.apis.dev.openstreetmap.org/oauth2/authorize)
  - [Access Token URL](https://master.apis.dev.openstreetmap.org/oauth2/token)
  - [OSM API](https://wiki.openstreetmap.org/wiki/API)

- **OpenWeather API**: For real-time weather data that impacts traffic.
  - [OpenWeather Site](https://openweathermap.org/)
  - [OpenWeather API](https://openweathermap.org/api)

### Machine Learning & Data Science

- **Scikit-learn**: For machine learning models and algorithms.
  - [Scikit-learn](https://scikit-learn.org/)
- **Prophet**: For time-series forecasting.
  - [Prophet](https://facebook.github.io/prophet/)
- **ARIMA (statsmodels)**: For time series modeling.
  - [ARIMA (statsmodels)](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html)

### Route Optimization & Algorithms

- **OSRM** or **GraphHopper**: Open-source routing engines.
  - [OSRM](http://project-osrm.org/)
  - [GraphHopper](https://www.graphhopper.com/)

### Visualization

- **Matplotlib**: For plotting traffic trends and congestion.
  - [Matplotlib](https://matplotlib.org/)
- **Plotly**: For interactive route visualizations.
  - [Plotly](https://plotly.com/)
- **Leaflet**: For interactive map visualizations.
  - [Leaflet](https://leafletjs.com/)

### Data Preprocessing

- **Pandas**: For data cleaning, manipulation, and processing.
  - [Pandas](https://pandas.pydata.org/)

### HTTP Requests/ APIs

- **Requests**: For fetching weather and traffic data via APIs.

  - [Requests](https://docs.python-requests.org/en/master/)

## Future Enhancements

- **Traffic Prediction Improvements**: Incorporate deep learning models for complex traffic patterns.
- **User Interface**: Add a front-end for commuters to interact with traffic predictions and optimized routes.
- **API Rate Limits**: Implement caching or retry mechanisms to handle API restrictions effectively.
