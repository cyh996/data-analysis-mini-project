import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "region": ["Seoul", "Busan", "Seoul", "Daegu", "Busan"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106, 107],
    "customer_id": [1, 2, 1, 3, 4, 5, 3],
    "category": ["Food", "Drink", "Food", "Book", "Food", "Book", "Drink"],
    "amount": [12000, 5000, 18000, 15000, 22000, 17000, 8000]
})

merged_df = pd.merge(customers, orders, on='customer_id')
customer_total_amount = merged_df.groupby('name')['amount'].sum()
region_total_amount = merged_df.groupby('region')['amount'].sum()
category_total_amount = merged_df.groupby('category')['amount'].sum()
top_customer = customer_total_amount.nlargest(3)

region_aov = merged_df.groupby('region')['amount'].mean().round(2)
customer_aov = merged_df.groupby('name')['amount'].mean().round(2)
category_order_count = merged_df.groupby('category')['amount'].count()
customer_order_count = merged_df.groupby('name')['order_id'].count()

print('\nTop 3 customer')
print(top_customer)

print('\nRegion AOV')
print(region_aov)

print('\nCustomer AOV')
print(customer_aov)

print('\nCategory Order Count')
print(category_order_count)

print('\nCustomer Order Count')
print(customer_order_count)

plt.figure()
plt.pie(
    region_total_amount.values,
    labels=region_total_amount.index,
    autopct='%.1f%%',
    explode=[0, 0, 0.05]
)
plt.axis('equal')
plt.title('Sales Distribution by Region')
plt.savefig('images/Sales_Distribution_by_Region.png', bbox_inches='tight')
plt.close()

plt.figure()
plt.bar(customer_total_amount.index, customer_total_amount.values, width = 0.5)
plt.xlabel('Customer Name')
plt.ylabel('Amount')
plt.title('Total Sales by Customer')
plt.savefig('images/Total_Sales_by_Customer.png', bbox_inches='tight')
plt.close()

plt.figure()
plt.bar(category_total_amount.index, category_total_amount.values, width = 0.5)
plt.xlabel('Category')
plt.ylabel('Amount')
plt.title('Total Sales by Category')
plt.savefig('images/Total_Sales_by_Category.png', bbox_inches='tight')
plt.close()