# Survey Data Analysis Dashboard

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pnettto/survey-notebooks/main?urlpath=voila%2Frender%2FRegions%2Fregions.ipynb)

An interactive dashboard for analyzing survey data across different regions, demographics, and time periods using Jupyter notebooks and Voila.

## Features

- **Regional Analysis**: Compare survey results across different regions in Skåne
- **Gender Analysis**: Analyze survey responses by gender demographics  
- **Recurring Analysis**: Track trends over time periods
- **Interactive Visualizations**: Dynamic charts and controls using ipywidgets

## Project Structure

```
Survey/
├── Regions/           # Regional analysis notebooks and data
├── Gender/            # Gender-based analysis 
├── Recurring/         # Time-series analysis
├── utils.py           # Shared utility functions
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Local Development

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Launch Jupyter: `jupyter notebook`
4. Open any of the analysis notebooks in their respective folders

## Deploy on Binder

Click the "Launch Binder" badge above to run this application in your browser without any installation.

The Binder deployment will:
- Automatically install all required dependencies
- Set up the Jupyter environment with widget extensions
- Launch the interactive dashboard using Voila

## Usage

The main dashboard (`Regions/regions.ipynb`) provides interactive controls to:
- Select different survey indicators
- Choose time ranges for analysis  
- Compare data across different regions
- Generate dynamic visualizations

## Data

The application analyzes survey data related to:
- Public safety perceptions
- Environmental concerns
- Trust in institutions
- Crime victimization
- Community problems
