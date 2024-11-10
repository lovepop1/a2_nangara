# Color Maps Visualization

This folder contains resources for creating color map visualizations, including preprocessing, plotting, and generating GIFs. The Colab notebook provided helps process the data, create color map images, and animate these visualizations as GIFs.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Dataset Download](#dataset-download)
  - [Google Drive Setup](#google-drive-setup)
  - [Colab Notebook](#colab-notebook)

## Overview

This project focuses on generating color maps to analyse wildfires that happened in California and Washington from Aug-Sep 2015 from gridmet climate data, including visualizations of variables such as relative humidity, fuel moisture, and temperature. The visualizations help identify spatial and temporal patterns in the data and provide insights through animated GIFs.

## Getting Started

To begin with this project, follow these instructions to download the dataset, set up Google Drive, and configure the file paths.

### Dataset Download

The dataset can be downloaded from the following link:
[Gridmet Climatology Lab](https://www.northwestknowledge.net/metdata/data/)

The required files for this visualization are:
- `bi_2015.nc`
- `sph_2015.nc`
- `fm100_2015.nc`
- `fm1000_2015.nc`

Download these files and upload them to your Google Drive for easy access in the Colab notebook.

### Google Drive Setup

1. **Upload Data Files to Google Drive**: Place the downloaded files (`bi_2015.nc`, `sph_2015.nc`, `fm100_2015.nc`, `fm1000_2015.nc`) in a folder within your Google Drive.
2. **Mount Google Drive in Colab**: The Colab notebook will mount your Google Drive, giving it access to the dataset.
3. **Update File Paths**: After mounting, adjust the file paths in the notebook to point to the correct location of your data files in Google Drive.

### Colab Notebook

The main notebook for preprocessing, plotting, and generating GIFs is available at:
- `colab_notebooks/color_map.ipynb`

In this notebook, you will:
- Load and preprocess the data.
- Plot color maps of the chosen variables.
- Create GIF animations to illustrate changes over time.

