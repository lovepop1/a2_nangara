# Node-Link Diagrams Visualization

This project visualizes a citation network using node-link diagrams. The dataset, sourced from Stanford's SNAP repository, contains citation information between high-energy physics theory papers. We preprocess the data in Colab and generate visualizations using Gephi.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Dataset Download](#dataset-download)
- [Visualization in Gephi](#visualization-in-gephi)

## Overview

The project uses node-link diagrams to represent relationships in a citation network. Each node represents a paper, and each directed edge indicates a citation from one paper to another. This visualization enables the exploration of citation patterns, clusters, and key papers in the dataset.

## Getting Started

To replicate this project, follow these steps to download the dataset, upload it to Google Drive, preprocess it in Colab, and visualize it in Gephi.

### Dataset Download

The dataset can be downloaded from the following link:
[Stanford SNAP - cit-HepTh Dataset](https://snap.stanford.edu/data/cit-HepTh.html)

Download the `cit-HepTh.txt.gz` file, which contains the source and target node information for citations.
Download the `cit-HepTh-abstracts.tar.gz` file, which contains the paper information for a given id.

## Visualization in Gephi

After preprocessing, the data file is imported into Gephi to create and customize node-link diagrams.

### Steps to Visualize in Gephi

1. **Import Processed Data**: Load the preprocessed data file from the Colab notebook into Gephi.
2. **Analyse communities generated**: Use the paper title and abstract information to analyse all papers in a group and obtain inferences. 

