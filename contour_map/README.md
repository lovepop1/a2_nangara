# Contour Maps Visualization

This project generates contour maps from meteorological data, showcasing relationships between variables like solar radiation, potential evapotranspiration, and specific humidity. The scripts provided preprocess the data, plot contour maps, and create animated GIFs for temporal visualizations.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Dataset Download](#dataset-download)
  - [Setup Instructions](#setup-instructions)
- [Scripts](#scripts)
  - [Preprocessing and Plotting](#preprocessing-and-plotting)
  - [GIF Generation](#gif-generation)


## Overview

The project visualizes relationships between key meteorological variables, aiding in understanding spatial and temporal patterns across different regions. Contour maps highlight these relationships and offer insights into variable distributions over time through animated GIFs.

## Getting Started

To begin, download the required dataset, set up the file structure, and update the file paths in the scripts.

### Dataset Download

The dataset can be downloaded from the following link:
[Northwest Knowledge Network - METDATA](https://www.northwestknowledge.net/metdata/data/)

The required files for this visualization are:
- `srad_2015.nc` (Solar Radiation)
- `pet_2015.nc` (Potential Evapotranspiration)
- `sph_2015.nc` (Specific Humidity)

After downloading, upload these files to your local environment and update the file paths in the Python scripts.

### Setup Instructions

1. **Download Data Files**: Downloaded `.nc` files (`srad_2015.nc`, `pet_2015.nc`, `sph_2015.nc`).
2. **Update File Paths**: Edit the file paths in each script (`Contour_combined_srad_pet_sph.py` and `Contour_srad-pet_and_srad-sph.py`) to match the location of your dataset files.

## Scripts

### Preprocessing and Plotting

The following Python files are provided for preprocessing and plotting contour maps:

- **`Contour_combined_srad_pet_sph.py`**: This script loads and preprocesses the data for three variables—solar radiation, potential evapotranspiration, and specific humidity—and generates combined contour maps.
- **`Contour_srad-pet_and_srad-sph.py`**: This script focuses on generating contour maps comparing two variable pairs: solar radiation vs. potential evapotranspiration, and solar radiation vs. specific humidity.

Run these scripts in your environment to generate the contour plots.

### GIF Generation

- The `gifs/` folder contains a Python file for creating animated GIFs from the generated contour maps, along with the resulting GIF files.
- **Instructions**: Run the script in the `gifs/` folder to create GIF animations that visualize changes in contour patterns over time.

