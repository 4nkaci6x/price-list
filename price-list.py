import csv

with open("products.csv") as f:  # opens the file, closes it afterward
    for row in csv.DictReader(f):
        print(f"{row['name']:<20} {row['size']:<6} ${row['price']:>6}")
