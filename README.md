# Automated Procurement Insights

## Overview
This project demonstrates automated procurement and maintenance data analytics using Python. It integrates **Oracle Fusion procurement data** and **Maximo maintenance data**, performs spend and supplier analysis, and generates actionable reports and dashboards.  

It is designed to showcase skills relevant for **Sourcing & Analytics Specialist / Procurement Analyst** roles, including data integration, KPI tracking, automation, process standardization, and supporting full-cycle sourcing decisions.

---

## Features
- Merge procurement and maintenance datasets (Oracle Fusion + Maximo)  
- Calculate total spend, supplier spend, category spend, and maintenance %  
- Track KPIs: PO count, average spend per PO, supplier performance  
- Simulate contract creation and mapping in Oracle Fusion  
- Full RFP process simulation: supplier ranking based on cost, reliability, and maintenance  
- Generate Excel reports ready for dashboards  
- Multiple visualizations:  
  - Supplier Spend (Bar Chart)  
  - Category Spend (Pie Chart)  
  - Procurement vs Maintenance Spend (Bar Chart)  
  - Maintenance % per Supplier (Bar Chart)  
  - Monthly Spend Trend (Line Chart)  
- Workflow designed for extendability: punchout/catalog integration, ARO shared services opportunities  
- Lightweight and runnable on Google Colab, PC, or Mac  

---

## Folder Structure
automated-procurement-insights/
├── Data/                  # Input CSVs (Oracle + Maximo)
├── Scripts/               # Python analytics script
├── Notebooks/             # Optional: exploratory analysis
├── Reports/               # Generated Excel reports
├── Visuals/               # Generated charts (PNG)
└── README.md              # Project documentation

---

## Usage Instructions

### Google Colab
1. Open a new notebook in [Google Colab](https://colab.research.google.com)  
2. Copy the `procurement_analytics.py` code into a cell  
3. Run the cell  
4. Outputs:  
   - Excel reports saved in `Reports/`  
   - Charts saved in `Visuals/`  

### Local Python
1. Install dependencies:
```bash
pip install pandas matplotlib openpyxl

