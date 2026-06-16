# Enterprise B2B Supply Chain Logistics & Vendor Performance Dashboard

An end-to-end data engineering and predictive analytics pipeline that transforms real-world commercial wholesale logistics records (30,000+ transaction rows) into an interactive, enterprise-grade business intelligence dashboard using Python Dash, Plotly, and scikit-learn.

## 📊 Business Problem & Operational Impact
Traditional retail analytics frameworks look primarily at consumer touchpoints (B2C). This project shifts the focus to complex B2B Supply Chain constraints by analyzing how inventory moves across multiple commercial pipelines: **Retail Channels, Warehouses, and Internal Transfers**. 

By evaluating volume velocities and transfer friction metrics, this infrastructure allows inventory operations teams to pinpoint logistically weak nodes, optimize warehouse distribution, and systematically tier the vendor profile ecosystem.

## 🛠️ Core Technology Stack
* **Data Engineering & Manipulation:** Python, Pandas, NumPy
* **Interactive Frontend UI Engine:** Plotly Dash, Dash Bootstrap Components (Flatly Theme)
* **Asynchronous Server Layer:** Flask Core
* **Advanced Unsupervised Machine Learning:** Scikit-Learn (K-Means Clustering)

## 📐 Advanced Architecture Breakdown

### 1. High-Speed Schema Ingestion & Normalization
* Handled an active commercial ledger, implementing defensive validation checks (`os.path.exists`) and dynamic type coercion via vectorized date parsing to convert period text fields into 64-bit continuous timeline coordinate tracks.
* Mitigated potential upstream schema drift by integrating fallback conditional tests to discover target columns dynamically at runtime (e.g., handling variations between `Order_Date`, `Date`, and `MONTH-PERIOD`).

### 2. Transitioning from B2C RFM to B2B FVM Supplier Tiering
* Refactored classical consumer customer analytics models into an operational **FVM Framework**:
  * **Frequency (F):** Tracking the operational volume frequency of inventory shipments per vendor.
  * **Volume (V):** Calculating cumulative unit outputs (`TOTAL_SALES_VOLUME`) managed per resource node.
  * **Mix Strategy (M):** Identifying stock orientation split across retail storefronts and core logistics warehouses.
* Applied **K-Means Clustering** against scaled features to segment the merchant network into high-impact operational classifications (e.g., *Omnichannel Heavyweights* vs. *Low-Velocity / Long-Tail Vendors*).

### 3. Reactive Asynchronous Dashboard Interface
* Designed a multi-panel dashboard structured on a responsive 12-column Grid Layout via `dash-bootstrap-components`.
* Created an event-driven **Reactive Callback Graph Engine**. When frontend component states shift, asynchronous network requests update localized JSON visual components via the browser's Virtual DOM without forcing an expensive, slow page refresh.
