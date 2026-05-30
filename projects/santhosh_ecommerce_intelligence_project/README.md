# README.md

# End-to-End E-commerce Intelligence System: Building a Customer 360 Analytics Framework

---

## Project Overview

This project focuses on building an End-to-End E-commerce Intelligence System using a multi-table relational e-commerce dataset. The project simulates a real-world business analytics workflow where data from multiple sources is integrated into a unified master dataset to generate actionable business insights.

The project covers:

* Data Cleaning and Preprocessing
* Data Integration
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Data Visualization
* Business Insights and Recommendations

The final output is a Customer 360 Analytics Framework that helps understand customer behavior, product performance, seller performance, operational efficiency, and revenue trends.

---

## Project Objectives

The main objectives of this project are:

* Integrate multiple relational datasets
* Build a consolidated master dataset
* Analyze customer purchasing behavior
* Identify top revenue-driving factors
* Evaluate seller and product performance
* Analyze customer satisfaction and review patterns
* Generate actionable business recommendations

---

## Dataset Overview

The project uses 9 relational datasets:

| Dataset                  | Description                   |
| ------------------------ | ----------------------------- |
| customers.csv            | Customer information          |
| orders.csv               | Order lifecycle details       |
| order_items.csv          | Product-level order details   |
| payments.csv             | Payment details               |
| reviews.csv              | Customer reviews and ratings  |
| products.csv             | Product information           |
| sellers.csv              | Seller details                |
| geolocation.csv          | Geographic information        |
| category_translation.csv | Product category translations |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Project Workflow

### Step 1: Data Loading and Initial Exploration

* Loaded all datasets using Pandas
* Explored datasets using:

  * `.head()`
  * `.info()`
  * `.describe()`
* Identified primary and foreign keys
* Understood table relationships

---

### Step 2: Data Cleaning and Preprocessing

#### Missing Value Handling

Handled missing values using:

* Dropping inconsistent rows
* Median imputation
* Placeholder value filling
* Business logic validation

Examples:

* Filled missing review comments with:

  * `No Title`
  * `No Comment`
* Removed inconsistent delivered orders with missing delivery timestamps
* Filled missing product dimensions using median values

#### Duplicate Removal

* Identified duplicate records
* Removed exact duplicate rows from geolocation dataset

#### Datetime Conversion

Converted date columns using:

```python
pd.to_datetime()
```

#### Data Validation

Validated:

* Review score ranges
* Product dimensions
* Payment values
* Delivery timelines

#### Standardized Column Names

Renamed inconsistent column names:

* `product_name_lenght` → `product_name_length`
* `product_description_lenght` → `product_description_length`

---

### Step 3: Data Integration

Created a Master Dataset by merging multiple relational tables.

#### Merge Sequence

1. orders + customers
2. orders + order_items
3. order_items + products
4. orders + payments
5. orders + reviews
6. order_items + sellers
7. products + category_translation

Final Output:

```python
master_df
```

A unified business dataset containing:

* Customer information
* Order information
* Product details
* Payment details
* Seller information
* Review information

---

### Step 4: Feature Engineering

Created meaningful business features:

| Feature                     | Description                     |
| --------------------------- | ------------------------------- |
| total_order_value           | Total amount spent per order    |
| delivery_time_days          | Delivery duration               |
| items_per_order             | Number of items per order       |
| customer_purchase_frequency | Number of purchases by customer |
| customer_lifetime_value     | Total spending by customer      |
| average_order_value         | Average spending per order      |

---

### Step 5: Exploratory Data Analysis (EDA)

#### Customer Analysis

* New vs Repeat Customers
* High-value vs Low-value Customers
* Geographic Customer Distribution

#### Revenue and Order Analysis

* Monthly Revenue Trends
* Order Volume Trends
* Peak Sales Periods

#### Product Analysis

* Top-selling Categories
* Revenue Contribution by Category
* Product Demand Distribution

#### Seller Analysis

* Top-performing Sellers
* Seller Revenue Contribution
* Seller Distribution

#### Review and Satisfaction Analysis

* Review Score Distribution
* Delivery Time vs Ratings
* Dissatisfaction Patterns

---

### Step 6: Data Visualization

Created visualizations using Matplotlib and Seaborn:

* Time Series Plots
* Bar Charts
* Histograms
* Box Plots
* Heatmaps

All charts were clearly labeled and interpretable.

---

### Step 7: Business Insights and Recommendations

#### Key Insights

* Certain product categories contribute significantly to overall revenue
* Repeat customers generate higher lifetime value
* Delivery delays negatively impact customer ratings
* Some sellers dominate platform revenue contribution
* High review scores are associated with faster deliveries

#### Recommendations

* Improve delivery efficiency
* Focus on customer retention strategies
* Promote high-performing product categories
* Support high-performing sellers
* Reduce operational delays
* Use customer behavior for personalized marketing

---

## Project Structure

```text
Ecommerce_Intelligence_Project/
│
├── datasets/
├── notebook/
├── visuals/
├── README.md
├── project_report.pdf
└── requirements.txt
```

---

## Conclusion

This project successfully demonstrates a complete end-to-end data analytics workflow using real-world e-commerce datasets.

The project showcases:

* Data preprocessing
* Multi-table data integration
* Feature engineering
* Exploratory data analysis
* Visualization
* Business insight generation

The final Customer 360 Analytics Framework provides a strong foundation for future Machine Learning applications such as:

* Customer Segmentation
* Recommendation Systems
* Churn Prediction
* Sales Forecasting
* Delivery Time Prediction

