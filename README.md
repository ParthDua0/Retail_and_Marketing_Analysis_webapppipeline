# Enterprise Retail Supply Chain Analytics & Supplier Intelligence Platform

## Overview

An end-to-end B2B supply chain analytics platform built to analyze commercial distribution operations, evaluate supplier performance, identify operational inefficiencies, and deliver executive-level business intelligence through an interactive web application.

Unlike traditional retail analytics projects that focus primarily on customer purchasing behavior, this project shifts the analytical focus toward enterprise supply chain operations, where supplier relationships, inventory movement, and distribution efficiency directly impact business performance.

The platform processes over **30,000 transaction records** and combines business analytics, machine learning, association rule mining, cohort analysis, and interactive dashboarding into a unified decision-support system.

---

## Business Problem

Large retail distribution networks frequently struggle to answer operational questions such as:

* Which suppliers contribute the highest long-term business value?
* How efficiently are products moving through warehouse and retail channels?
* Which suppliers should be prioritized strategically?
* Are internal transfer operations creating distribution bottlenecks?
* How can suppliers be segmented to improve procurement and inventory planning?

To address these challenges, this project analyzes transaction flows across three major distribution channels:

* **Warehouse Sales**
* **Retail Sales**
* **Retail Transfers**

The goal is to provide supply chain managers and business leaders with actionable operational insights and supplier intelligence.

---

## Project Architecture

### Phase 1: High-Speed Ingestion & Data Normalization

* Defensive file validation and ingestion checks
* Data loading using optimized Pandas workflows
* Schema validation and preprocessing
* Automated date normalization

### Phase 2: Exploratory Business Auditing

* Dataset profiling
* Missing value analysis
* Distribution diagnostics
* Operational KPI engineering

Key KPI:

**TRANSFER_TO_SALES_RATIO**

A custom operational metric developed to evaluate distribution efficiency and transfer friction across supply channels.

### Phase 3: Chronological KPI Aggregation

Built monthly operational datasets by aggregating transactional records into time-series business metrics.

Generated outputs include:

* Monthly sales volume
* Active SKU tracking
* Month-over-Month growth rates
* Supplier activity trends

### Phase 4: Supplier-Centric Business Framing

Reframed traditional retail analytics methodologies to focus on enterprise supply chain behavior rather than customer-level metrics.

### Phase 5: Supplier Lifecycle & Cohort Analysis

Performed retention and lifecycle analysis to evaluate supplier longevity and engagement patterns.

Key analyses:

* Supplier retention trends
* Lifecycle tracking
* Cohort behavior analysis

### Phase 6: Machine Learning Supplier Segmentation

Implemented unsupervised machine learning using **K-Means Clustering** to classify suppliers into strategic operational groups.

#### FVM Framework

Traditional customer-focused RFM analysis was adapted into a supplier-focused framework:

**Frequency (F)**

* How frequently orders are placed with a supplier.

**Volume (V)**

* Total sales volume supplied.

**Mix Strategy (M)**

* Diversity of supply distribution across warehouse and retail channels.

The clustering model automatically identified supplier segments such as:

* Omnichannel Heavyweights
* Strategic Suppliers
* Specialized Vendors
* Low-Velocity Long-Tail Suppliers

### Phase 7: Interactive Web Application Deployment

Developed a fully interactive analytics dashboard using:

* Dash
* Plotly
* Dash Bootstrap Components

Dashboard capabilities include:

* KPI monitoring
* Supplier segmentation visualization
* Cohort analysis exploration
* Revenue trend analysis
* Association rule insights
* Operational performance tracking

---

## Technical Challenges

### Challenge 1: Schema Drift & Date Parsing

#### Problem

Incoming ledger structures contained inconsistent date field naming conventions and monthly period values stored as string representations.

Examples:

* MONTH-PERIOD
* Month_Period
* Date

#### Solution

Implemented dynamic schema inspection and automated date conversion using:

```python
pd.to_datetime()
```

This created a resilient ingestion pipeline capable of adapting to future schema variations without requiring manual modifications.

---

### Challenge 2: Dash Callback Synchronization

#### Problem

The dashboard initially failed due to mismatches between frontend component identifiers and backend callback references.

#### Solution

Performed a structural audit of the Dash callback graph and synchronized all callback outputs with corresponding layout container IDs.

Result:

* Stable callback execution
* Reliable chart rendering
* Improved dashboard responsiveness

---

## Association Rule Mining

Implemented market basket analysis to uncover relationships between products and inventory movement patterns.

Generated:

* Support metrics
* Confidence scores
* Lift analysis

Outputs were exported into interactive HTML reports for business exploration.

---

## Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy

### Data Visualization

* Plotly
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* K-Means Clustering

### Association Rule Mining

* Mlxtend
* Apriori Algorithm

### Business Intelligence

* Power BI

### Web Application Framework

* Dash
* Dash Bootstrap Components

---

## Key Deliverables

* Supplier Intelligence Engine
* FVM Segmentation Framework
* Cohort Retention Analysis
* Supplier Lifetime Value Analysis
* Market Basket Analysis
* K-Means Supplier Clustering
* Interactive Dash Dashboard
* Power BI Executive Reports
* Automated KPI Aggregation Pipeline

---

## Repository Structure

```text
Retail_and_Marketing_Analysis_webapppipeline/
│
├── dashboards/
│   └── Retail_and_Sales_Analysis/
│
├── notebooks/
│   ├── notebook1.ipynb
│   ├── notebook2.ipynb
│   ├── notebook3.ipynb
│   ├── notebook4.ipynb
│   └── notebook5.ipynb
│
├── outputs/
│   ├── visualizations/
│   ├── customer_segments.csv
│   ├── supplier_clusters.csv
│   ├── supplier_lifetime_value.csv
│   ├── association_rules.html
│   └── monthly_kpis.csv
│
├── reports/
│   ├── cohort_retention.csv
│   ├── supplier_kpis.csv
│   ├── executive_summary.txt
│   ├── project_completion_summary.txt
│   └── supplier_lifecycle.csv
│
├── Retail_and_Marketing_Analysis.ipynb
├── app.py
├── README.md
└── .gitignore
```

---

## Business Impact

This platform enables supply chain teams to:

* Monitor operational efficiency across distribution channels
* Identify high-value suppliers
* Improve procurement decision-making
* Detect supply-chain bottlenecks
* Segment suppliers for targeted management strategies
* Support executive-level operational reporting

---

## Future Enhancements

* Revenue Forecasting (ARIMA / Prophet)
* Supplier Risk Scoring
* Demand Forecasting
* Inventory Optimization Models
* Automated Anomaly Detection
* Cloud Deployment (AWS / Azure)
* Real-Time Data Streaming
* Procurement Recommendation Systems

---

## Author

**Parth Dua**

Data Analytics | Business Intelligence | Machine Learning | Supply Chain Analytics
