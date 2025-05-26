# Sprint 2 – Scientific Thinking and Data Analysis

## Overview

Sprint 2 focuses on developing essential skills for working with real-world data. This includes data collection and cleaning, data analysis and visualization, fundamental statistical reasoning, and the ability to communicate findings clearly through scientific writing. Technical skills like web scraping and working with data structures are also introduced.

---

## Scientific Writing

Scientific writing is a formal and objective method for communicating research results, using clear structure and precise language. This module focused on:

- **Research and Organization**:  
  How to define research questions or hypotheses, conduct literature reviews, and organize findings.

- **IMRaD Structure**:  
  Learning to write academic texts following the standard format:
  - **Introduction**: Context and motivation.
  - **Methods**: Description of the tools, procedures, and data used.
  - **Results**: Presentation of findings (often with tables and figures).
  - **Discussion**: Interpretation and implications of the results.

- **Clarity and Argumentation**:  
  Writing with logical flow, using evidence to support arguments and avoiding ambiguity.

This component helps bridge technical work and academic or professional communication.

---

## Data Structures

Understanding and working with data structures is crucial in both programming and data analysis. This topic expanded on Python’s built-in data types:

- **Lists and Tuples**:  
  Dynamic vs. immutable sequences; indexing, slicing, iteration, and built-in methods.

- **Dictionaries**:  
  Key-value pair structure, nested dictionaries, and common operations like `.get()` and `.items()`.

- **Sets**:  
  Use cases for unordered collections with no duplicates, set operations like union and intersection.

- **Custom Data Structures** (introductory):  
  Brief introduction to organizing data using classes or combining native types.

These tools are foundational for organizing and manipulating data efficiently in code.

---

## Probability and Statistics

This topic introduced fundamental concepts in statistical thinking for data-driven decision-making:

- **Descriptive Statistics**:
  - Measures of central tendency: mean, median, mode.
  - Measures of dispersion: range, variance, standard deviation.
  - Frequency distributions and histograms.

- **Basic Probability Concepts**:
  - Events, outcomes, and sample spaces.
  - Independent and dependent events.
  - Simple probability calculations.

- **Data Visualization for Statistics**:
  Using visual tools such as bar charts, boxplots, and histograms to summarize data distributions and variability.

These concepts are key to interpreting data and preparing for more advanced modeling techniques.

---

## Data Cleaning and Preparation

Before analysis, raw data often needs cleaning and restructuring. In this module, we used Python (primarily **Pandas**) to:

- Load datasets from `.csv`, `.xlsx`, and other formats.
- Inspect and understand the dataset structure (`.info()`, `.describe()`, `.head()`).
- Handle missing data: filling, removing, or imputing.
- Rename columns, change data types, and filter rows or columns.
- Format numeric and string values (e.g., removing currency symbols or standardizing text).
- Create new columns or transform existing ones.

A clean dataset is essential for meaningful and reliable analysis.

---

## Data Analysis and Visualization

After preparing the data, the next step was to explore and analyze it. Topics included:

- **Exploratory Data Analysis (EDA)**:
  - Understanding variable distributions.
  - Identifying patterns, outliers, and correlations.

- **Visualizations** (using **Matplotlib** and **Seaborn**):
  - Line plots, scatter plots, bar charts, histograms, boxplots.
  - Customizing graphs with labels, titles, and color schemes.

- **Basic Aggregations and Grouping**:
  - Grouping data by categories and computing summary statistics.

This process transforms raw data into actionable insights.

---

## Web Scraping

Web scraping is a technique for collecting data automatically from websites. We used **Selenium** and **BeautifulSoup** to:

- Navigate websites and interact with dynamic content.
- Extract information from HTML tags using CSS selectors or XPath.
- Store structured data (like prices, titles, locations) into DataFrames.
- Export the final dataset to formats like `.csv` or `.xlsx`.

Example use case: scraping real estate listings including price, location, number of rooms, and area.

This technique is essential when working with data that isn’t available through traditional APIs or databases.

---

## Recommended Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Selenium Python Docs](https://selenium-python.readthedocs.io/)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [How to Write a Scientific Paper](https://writingcenter.unc.edu/tips-and-tools/scientific-reports/)
