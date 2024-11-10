# Quiver Plots Visualization

This project visualizes wind vector fields through quiver plots, illustrating wind direction and speed over time. The scripts preprocess the data, generate quiver plots, and create animated GIFs to show temporal changes.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Dataset Download](#dataset-download)
  - [Setup Instructions](#setup-instructions)
- [Scripts](#scripts)
  - [Preprocessing and Plotting](#preprocessing-and-plotting)
  - [GIF Generation](#gif-generation)

## Overview

This project uses quiver plots to visualize wind vector fields based on meteorological data, highlighting changes in wind speed and direction over time. Quiver plots provide an intuitive view of vector fields, with arrows indicating the direction and magnitude of wind.

## Getting Started

Follow the instructions below to download the dataset, set up file paths, and run the scripts for generating quiver plots and animations.

### Dataset Download

The dataset can be downloaded from the following link:
[Northwest Knowledge Network - METDATA](https://www.northwestknowledge.net/metdata/data/)

The required files are:
- `vs_2015.nc` (Wind Speed)
- `th_2015.nc` (Wind Direction)

After downloading, place these files in your local environment and update file paths in the Python scripts accordingly.

### Setup Instructions

1. **Upload Data Files**: Ensure the downloaded files (`vs_2015.nc` and `th_2015.nc`) are accessible in your environment.
2. **Update File Paths**: Edit the file paths in `quiver__.py` and `quiver_same_sized.py` to point to the location of your dataset files.

## Scripts

### Preprocessing and Plotting

Two Python scripts are provided for preprocessing and plotting quiver plots:

- **`quiver__.py`**: This script preprocesses wind data and generates standard quiver plots to visualize wind speed and direction.
- **`quiver_same_sized.py`**: This script generates quiver plots with arrows of uniform length, focusing on the direction while normalizing magnitude for better visual clarity.

Run these scripts to generate quiver plots, which will be saved to the `images/` folder.

### GIF Generation

- The `gifs/` folder contains a Python script for creating animated GIFs from the generated quiver plots, alongside the resulting GIF files.
- **Instructions**: Run the script in the `gifs/` folder to create GIF animations that display changes in the vector fields over time.
