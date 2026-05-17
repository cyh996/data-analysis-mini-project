import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs("images", exist_ok=True)

sales = pd.DataFrame({
    "date": [
        "2024-01-01","2024-01-01","2024-01-02","2024-01-02",
        "2024-01-03","2024-01-03","2024-01-04","2024-01-04",
        "2024-01-05","2024-01-05"
    ],
    "category": [
        "Food","Drink","Food","Book",
        "Food","Drink","Book","Food",
        "Drink","Book"
    ],
    "quantity": [3,2,5,1,4,3,2,6,4,3],
    "unit_price": [5000,3000,5000,15000,5000,3000,15000,5000,3000,15000],
    "region": [
        "Seoul","Busan","Seoul","Daegu",
        "Seoul","Busan","Daegu","Seoul",
        "Busan","Daegu"
    ]
})

sales['sales_amount'] = sales['quantity'] * sales['unit_price']
sales['date'] = pd.to_datetime(sales['date'])

sales_per_category = sales.groupby('category')['sales_amount'].sum()
sales_per_category = sales_per_category.sort_values(ascending=False)

pivot_sales_date_category = sales.pivot_table(
    index='date',
    columns='category',
    values='sales_amount',
    aggfunc='sum',
    fill_value=0
)
print('\nDaily sales by category')
print(pivot_sales_date_category)

sales_per_region = sales.groupby('region')['sales_amount'].sum()
print('\nSales by Region')
print(sales_per_region)

category_per_region = sales.groupby(['region', 'category'])['quantity'].sum()
print('\nQuantity by Region and Category')
print(category_per_region.unstack(fill_value=0))

daily_trend = sales.groupby("date").agg(daily_revenue=("sales_amount", "sum"), order_count=("date", "count"))
print('\nDaily Trend')
print(daily_trend)

avg_quantity_per_order = sales.groupby('category')['quantity'].mean().reset_index(name='avg_quantity_per_order')
print('\nAverage quantity purchased per order')
print(avg_quantity_per_order)

plt.figure()
plt.plot(daily_trend.index, daily_trend['daily_revenue'], 'o-')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.title('Daily Sales')
plt.xticks(daily_trend.index, rotation=45)
plt.savefig("images/daily_sales.png", bbox_inches="tight")
plt.close()

plt.figure()
plt.bar(sales_per_category.index, sales_per_category.values, width=0.3)
plt.xlabel('Category')
plt.ylabel('Sales Amount')
plt.title('Total Sales per Category')
plt.savefig("images/total_sales_per_category.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots(figsize=(10,6))
pivot_sales_date_category.plot(ax=ax, marker='o')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.title('Daily Sales by Category')
plt.legend(title='Category')
plt.savefig("images/daily_sales_by_category.png", bbox_inches="tight")
plt.close()