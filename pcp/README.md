# Parallel Coordinates Plot (PCP) Visualization

This project uses Parallel Coordinates Plots (PCP) to explore customer behavior patterns across multiple variables. PCP is a powerful tool for visualizing relationships and patterns in multivariate data, making it easier to interpret complex datasets.

## Table of Contents
- [Overview](#overview)
- [Objective](#objective)
- [Dataset](#dataset)
- [How to Run](#how-to-run)
- [Results](#results)


## Overview

The project visualizes customer behavior by mapping multiple attributes from the dataset on parallel axes. Each line represents an individual customer, showing the values for each attribute across axes. This approach highlights trends and patterns across various demographics, spending habits, and campaign engagement metrics.

## Objective

The goal of this project is to explore and understand customer behavior patterns through a multivariate data visualization. By analyzing various aspects of customer data, we can gain insights into demographic trends, spending patterns, and responses to marketing campaigns.

## Dataset

The project uses the **Customer Personality Analysis** dataset, which can be accessed on Kaggle:
[Customer Personality Analysis Dataset on Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

This dataset provides detailed information about customers, including:
- Demographics
- Spending habits
- Engagement with marketing campaigns



## How to Run

1. **Navigate to the PCP Directory**: Open your terminal or file explorer and go to the `pcp` directory containing the HTML visualization files.
2. **Open with Live Server**:
   - If you are using a code editor like VS Code, you can right-click the HTML file and select "Open with Live Server" to view the visualization in your browser.
3. **Alternatively, Start a Local Server**:
   - Run the following command in the terminal to serve the files locally:
     ```bash
     python3 -m http.server
     ```
   - Open the displayed URL (e.g., `http://localhost:8000`) in your browser to view the PCP visualizations.

## Results

The PCP visualization provides unique insights into customer behavior by allowing you to observe patterns and correlations across multiple attributes. This visualization approach makes it easier to spot trends and outliers, helping you make informed decisions based on customer demographics, spending habits, and engagement levels.

