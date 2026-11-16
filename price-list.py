import csv

with open("products.csv") as f:  # opens the file, closes it afterward
    for row in csv.DictReader(f):
        print(row["name"], row["size"], row["price"])
