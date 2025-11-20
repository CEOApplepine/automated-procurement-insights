# ========================================================
# Automated Procurement Insights - Jupyter Notebook Version
# ========================================================

# Cell 1: Import Libraries
import pandas as pd
from pathlib import Path
from IPython.display import display
import matplotlib.pyplot as plt

# ========================================================
# Cell 2: Set Paths
data_path = Path('data')
reports_path = Path('reports')
reports_path.mkdir(exist_ok=True)  # Ensure reports folder exists

# ========================================================
# Cell 3: Load Sample Data
procurement_file = data_path / 'oracle_procurement.csv'
maintenance_file = data_path / 'maximo_maintenance.csv'

procurement = pd.read_csv(procurement_file)
maintenance = pd.read_csv(maintenance_file)

print("Data loaded successfully!")
display(procurement.head())
display(maintenance.head())

# ========================================================
# Cell 4: Merge Data on PO_ID
merged = pd.merge(procurement, maintenance, on='PO_ID', how='left')
merged['Maintenance_Cost'] = merged['Maintenance_Cost'].fillna(0)
merged.to_csv(data_path / 'merged_data.csv', index=False)

print("Data merged successfully!")
display(merged.head())

# ========================================================
# Cell 5: Analytics - Total Spend
total_procurement = merged['Amount'].sum()
total_maintenance = merged['Maintenance_Cost'].sum()
total_spend = total_procurement + total_maintenance

print(f"Total Procurement Spend: ${total_procurement}")
print(f"Total Maintenance Spend: ${total_maintenance}")
print(f"Total Combined Spend: ${total_spend}")

# ========================================================
# Cell 6: Analytics - Spend by Supplier
supplier_spend = merged.groupby('Supplier')['Amount'].sum().reset_index()
supplier_spend = supplier_spend.sort_values(by='Amount', ascending=False)
print("\nSupplier Spend:")
display(supplier_spend)

# Visualization - Supplier Spend
plt.figure(figsize=(8,5))
plt.bar(supplier_spend['Supplier'], supplier_spend['Amount'], color='skyblue')
plt.title('Supplier Spend')
plt.ylabel('Amount')
plt.xlabel('Supplier')
plt.xticks(rotation=45)
plt.show()

# ========================================================
# Cell 7: Analytics - Spend by Category
category_spend = merged.groupby('Category')['Amount'].sum().reset_index()
print("\nCategory Spend:")
display(category_spend)

# Visualization - Category Spend
plt.figure(figsize=(6,4))
plt.bar(category_spend['Category'], category_spend['Amount'], color='lightgreen')
plt.title('Category Spend')
plt.ylabel('Amount')
plt.xlabel('Category')
plt.show()

# ========================================================
# Cell 8: Save Reports
supplier_spend.to_csv(reports_path / 'supplier_spend_summary.csv', index=False)
category_spend.to_csv(reports_path / 'category_spend_summary.csv', index=False)
print("\nReports saved in 'reports/' folder.")
