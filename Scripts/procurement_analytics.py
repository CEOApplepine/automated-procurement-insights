import pandas as pd

# 1. Extract Data
procurement = pd.read_csv('data/oracle_procurement.csv')
maintenance = pd.read_csv('data/maximo_maintenance.csv')
print("Data loaded successfully!")

# 2. Merge Data on PO_ID
merged = pd.merge(procurement, maintenance, on='PO_ID', how='left')
merged.to_csv('data/merged_data.csv', index=False)
print("Data merged successfully!")

# 3. Analytics
# Total spend
total_procurement = merged['Amount'].sum()
total_maintenance = merged['Maintenance_Cost'].sum()
print(f"Total Procurement Spend: ${total_procurement}")
print(f"Total Maintenance Spend: ${total_maintenance}")

# Spend by Supplier
supplier_spend = merged.groupby('Supplier')['Amount'].sum().reset_index()
supplier_spend = supplier_spend.sort_values(by='Amount', ascending=False)
print("\nSupplier Spend:")
print(supplier_spend)

# Spend by Category
category_spend = merged.groupby('Category')['Amount'].sum().reset_index()
print("\nCategory Spend:")
print(category_spend)

# 4. Save Reports
supplier_spend.to_csv('reports/supplier_spend_summary.csv', index=False)
category_spend.to_csv('reports/category_spend_summary.csv', index=False)
print("\nReports saved in 'reports/' folder.")
