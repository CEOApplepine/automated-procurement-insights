# automated-procurement-insights
Python project demonstrating procurement and maintenance data analytics
# Automated Procurement Data Insights

## Overview
This project demonstrates automated procurement and maintenance data analytics using Python. It integrates **Oracle Fusion procurement data** and **Maximo maintenance data**, performs spend and supplier analysis, and generates actionable reports.  

It is designed to showcase key skills for a **Sourcing & Analytics Specialist** role, including data integration, Python automation, KPI tracking, and preparing data for dashboards like Power BI.

---

## Features
- Merge procurement and maintenance datasets
- Calculate total spend, supplier spend, and category spend
- Generate CSV reports for easy visualization
- Ready for integration with Power BI or Excel dashboards
- Lightweight and runnable on iPad, PC, or Mac

---

## Folder Structure

automated-procurement-insights/
├── data/                  # Sample input data (procurement + maintenance)
├── scripts/               # Python analytics script
├── reports/               # Generated CSV reports
└── README.md              # Project documentation

---

## Sample Data
**Oracle Procurement Data (`oracle_procurement.csv`)**
| PO_ID | Supplier | Category | Amount | Order_Date | Contract_ID |
|-------|---------|----------|--------|------------|------------|
| 1001  | ABC Ltd | Maintenance | 5000 | 2025-01-15 | C001 |

**Maximo Maintenance Data (`maximo_maintenance.csv`)**
| Asset_ID | Work_Order_ID | Maintenance_Cost | Date | PO_ID |
|----------|---------------|-----------------|------|-------|
| A01      | WO001         | 2000            | 2025-01-20 | 1001 |

---

## Usage Instructions

### Step 1: Run the Python Script
```bash
python scripts/procurement_analytics.py
