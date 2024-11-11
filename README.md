
# VShop Data Analysis Tool

This repository contains a Python script for analyzing customer behavior data from the `VShop` database, focusing on patterns like registration-to-first-order times. It also includes related visualizations.

## Features

- **Secure Database Connection**:
  - Establishes an SSH tunnel for secure access to a remote PostgreSQL database.
  - Connects to the `VShop` database using the `psycopg2` library.

- **Customer Behavior Analysis**:
  - Analyzes customer registration data and their first-order behavior.
  - Calculates the time difference (in days) between user registration and their first order.
  - Filters customer data based on statistical thresholds (mean ± a configurable range of standard deviations).

- **Statistical Insights**:
  - Customizable parameters `a` and `b` allow you to define the filtering criteria for customer data analysis.
  - Outputs a filtered dataset of users for deeper insights into user behavior.

- **Data Visualizations**:
  - The included images demonstrate comparisons of metrics such as item similarity and delivery performance, likely generated using the analysis results.

## Files

- **main.py**: The primary script for database interaction and customer behavior analysis.
- **Similarity of Items.jpg**: A visualization comparing similarity metrics between base and result datasets.
- **Delivery Note.jpg**: A visualization analyzing delivery-related metrics.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install Dependencies**:
   Ensure Python 3.x is installed, then install the required libraries:
   ```bash
   pip install psycopg2 pandas sshtunnel
   ```

3. **Configure Database Credentials**:
   Update `main.py` with your own database and SSH credentials.

4. **Run the Script**:
   Execute the script to fetch data and generate insights:
   ```bash
   python main.py
   ```

## Usage

1. **Analyze Customer Data**:
   - The function `normal_distribuation(a, b)`:
     - Fetches customer registration and first-order data from the database.
     - Computes the time difference between registration and the first order.
     - Applies a filter to include only customers whose behavior falls within a specified statistical range based on the mean and standard deviation.

2. **Customize Parameters**:
   - Modify the values of `a` and `b` in the `normal_distribuation` function to adjust the filtering range:
     - `a`: Adjusts the upper limit.
     - `b`: Adjusts the lower limit.
   - Example:
     ```python
     normal_distribuation(1, 1)
     ```

3. **Visualizations**:
   - Use the provided images (`Similarity of Items.jpg` and `Delivery Note.jpg`) as examples of insights that can be derived from the analysis.



