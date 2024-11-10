# Treemap Visualization

This project uses Treemaps to explore and visualize customer data hierarchically, making it easier to understand the distribution and composition of various customer segments. Treemaps display data in nested rectangles, where each rectangle represents a category or subcategory based on specific attributes from the dataset.

## Table of Contents
- [Overview](#overview)
- [Objective](#objective)
- [Dataset](#dataset)
- [How to Run](#how-to-run)
- [Results](#results)


## Overview

This project visualizes customer behavior and segmentation through Treemaps, focusing on attributes like demographics, spending patterns, and engagement with marketing campaigns. Treemaps offer an effective way to view the proportional relationships within the data.

## Objective

The goal of this project is to analyze customer data and gain insights into customer distribution across various categories, such as demographics and spending habits, using Treemaps for clear, hierarchical visualization.

## Dataset

The project uses the **Customer Personality Analysis** dataset, available on Kaggle:
[Customer Personality Analysis Dataset on Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

This dataset includes:
- Demographics
- Spending habits
- Engagement with marketing campaigns

To use this dataset, download it from Kaggle and save it in the `data/` directory.

## How to Run

1. **Navigate to the Treemap Directory**: Open your terminal or file explorer and go to the `treemap` directory containing the visualization scripts or HTML files.
2. **Open with Live Server**:
   - If you are using a code editor like VS Code, right-click the HTML file and select "Open with Live Server" to view the Treemap visualization in your browser.
3. **Alternatively, Start a Local Server**:
   - Run the following command in the terminal to serve the files locally:
     ```bash
     python3 -m http.server
     ```
   - Open the displayed URL (e.g., `http://localhost:8000`) in your browser to view the Treemap visualizations.

## Results

The Treemap visualization reveals customer distribution and patterns in spending and engagement, helping identify trends within different demographic groups. This hierarchical visualization provides a clear view of how various categories contribute to the overall dataset.


