import pandas as pd

# Load files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Remove $ sign and convert price to float
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Calculate Sales
df["Sales"] = df["quantity"] * df["price"]

# Final columns
output = df[["Sales", "date", "region"]]
output.columns = ["Sales", "Date", "Region"]

# Save file
output.to_csv("formatted_output.csv", index=False)

print("Done!")
