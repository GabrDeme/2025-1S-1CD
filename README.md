<img alt="" src="/Assets/Banner.png">

# First Semester of Data Science Graduation

Welcome to the **First Semester of Data Science Graduation** repository!

## Course Content

### 1. Number Systems and Logic Gates
- **Binary**: A base-2 number system using only 0 and 1, fundamental to how computers store and process information.  
- **Decimal**: The standard base-10 number system used in everyday life, composed of digits from 0 to 9.  
- **Hexadecimal**: A base-16 number system often used in computing for compactly representing binary values, using digits 0–9 and letters A–F.  
- **Logic Gates**: Basic building blocks of digital circuits that perform logical operations (AND, OR, NOT, etc.) on binary inputs to produce a specific output.

### 2. Introduction to Python
- **Basic Concepts**: Syntax, variables, and data types.
- **Decision Structures and Loops**: Conditionals (`if`, `else`, `elif`) and loops (`for`, `while`) for flow control.
- **Collections**: Lists, tuples, dictionaries, and sets for storing and manipulating data.
- **Functions**: Creating functions to modularize code, including parameters and return values.
- **File Manipulation**: Reading and writing text and CSV files.

### 3. Python for Data Science
- **Web Scraping**: The process of extracting data from websites by parsing HTML or XML content, allowing you to collect structured information from online sources automatically.  
- **Data Treatment**: Involves cleaning, transforming, and organizing raw data into a structured format, enabling efficient analysis and preparation for modeling or visualization.  
- **Visualization and Modeling**: Creating charts and graphs to interpret data trends and applying statistical or machine learning techniques to uncover patterns, make predictions, or test hypotheses.

### 4. Scientific Writing
Scientific writing is a formal and evidence-based way of communicating research findings to the academic community. It focuses on clarity, objectivity, and logical structure, often following formats like IMRaD (Introduction, Methods, Results, and Discussion).

- **Research and Organization**: Collecting and organizing relevant information to support a research question or hypothesis.  
- **Analysis and Interpretation**: Analyzing data and interpreting results to develop clear and well-argued conclusions.  
- **Clear Communication**: Presenting findings using precise language, structured sections, and appropriate academic style.

---

### Key Data Science Techniques

- **Extracting Real Estate Information**: The code uses **Selenium** to scrape real estate listings from a website, extracting details such as the location, price, size, number of rooms, bathrooms, and parking spaces for houses, lots, and apartments available for sale or rent. 
  All of this converted to a '`xlsx`' file.

  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.chrome.service import Service
  from selenium.webdriver.common.action_chains import ActionChains
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as ec
  import pandas as pd
  import time
  from selenium.common.exceptions import TimeoutException

  chrome_driver_path = "C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe"
  ```

- **Treating Real Estate Data**: After extraction, **Pandas** is used to clean and organize the dataset for analysis:

  - Missing values in the location column are filled, and column names are renamed for clarity.
  - Prices are cleaned by removing symbols (like `R$`) and formatting the data as numerical values.
  - Property size (`metragem`) is standardized by removing text and converting to numeric form.
  - Room (`quartos`), bathroom (`banheiros`), and parking (`vagas`) data are cleaned by stripping extra text, handling unknown values, and converting to numeric types.
  - A custom function is used to extract **Condominium** and **IPTU** values from mixed text using regular expressions.
    
- **Visualizing and Interpreting the Data**: After processing, several visualizations were created to extract insights from the dataset. These include statistical summaries and graphical analyses:

  - A bar chart was used to compare the **average number of bedrooms, bathrooms, and parking spaces** among the properties.
  - A boxplot grouped properties by **size range (m²)** to analyze price distribution across different property sizes.
  - A line graph showed the **distribution of property sizes**, highlighting the average with a reference line.
  - A scatter plot and linear regression were used to explore the **relationship between the number of parking spaces and property price**.
    
  <br>
  
  > ⚠️ *Note: These are just a few examples of the visualizations. The complete notebook contains more analyses not included in this summary.*

- **Interactive Sales Dashboard with *Streamlit***: This code is a Streamlit-based web application designed to visualize and explore sales data interactively. It allows users to filter and analyze key metrics related to products and store performance using dynamic charts powered by Plotly.
  ``` python
  import streamlit as st
  import pandas as pd
  import plotly.express as px
  from streamlit_option_menu import option_menu
  ```
  
https://github.com/user-attachments/assets/3ea225ef-d688-464a-afb6-97896bd0463f

### Mora Infos, Links and Projects
- [Integration Project repository]()
- [Extension Project repository](https://github.com/GabrDeme/Waste-Data-SP)
- [Python for Data Science course repository](https://github.com/GabrDeme/PPDS-2024)
- [Coding Dojo - IMDb Top 250 movies](https://github.com/GabrDeme/2025-1S-1CD/tree/main/Sprint2/coding_dojo)
- [Hackathon - HR analysis](https://github.com/GabrDeme/2025-1S-1CD/tree/main/Sprint3/hackaton)
