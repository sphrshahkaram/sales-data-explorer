import csv

columns = {
    "Region": 0,
    "Country": 1,
    "Item Type": 2,
    "Sales Channel": 3,
    "Order Priority": 4,
    "Order Date": 5,
    "Order ID": 6,
    "Ship Date": 7,
    "Units Sold": 8,
    "Unit Price": 9,
    "Unit Cost": 10,
    "Total Revenue": 11,
    "Total Cost": 12,
    "Total Profit": 13
}

with open(r"E:\New folder\sales.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip the header

    user_region = input("Enter a region: ")
    user_feature = input("What information do you want? ")

    for row in reader:

        # Check if the row matches the region
        if row[0].lower() == user_region.lower():

            # Check if the requested feature exists
            if user_feature in columns:
                print(f"{user_feature}: {row[columns[user_feature]]}")
            else:
                print("Feature not found.")
