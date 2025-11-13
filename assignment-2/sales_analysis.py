import csv
import logging
from itertools import groupby
from operator import itemgetter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SalesAnalysis")

class SalesAnalysis:
    def __init__(self, csv_file):
        self.records = self._load_csv(csv_file)

    def _load_csv(self, csv_file):
        records = []
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    records.append({
                        'id': row['id'],
                        'region': row['region'],
                        'item': row['item'],
                        'units': int(row['units']),
                        'price': float(row['price'])
                    })
                except (ValueError, KeyError) as e:
                    logger.warning(f"Skipping invalid row: {row}")
        return records

    def total_units(self):
        #use map to apply lambda function to extract units value for each row and sum them
        return sum(map(lambda r: r["units"], self.records))

    def total_revenue(self):
        #for each record, calculate revenue using units * price and then sum them up
        return sum(map(lambda r: r["units"] * r["price"], self.records))

    def revenue_by_region(self):
        # Group by region using functional approach
        self.records.sort(key=lambda r: r["region"])
        result = {}
        for region, rows in groupby(self.records, key=lambda r: r["region"]):
            # Stream operation: map to revenue values and sum
            result[region] = sum(map(lambda r: r["units"] * r["price"], rows))
        return result

    def most_sold_item(self):
        # Group items and aggregate using lambda expressions
        self.records.sort(key=lambda r: r["item"])
        item_counts = {}
        for item, rows in groupby(self.records, key=lambda r: r["item"]):
            item_counts[item] = sum(map(lambda r: r["units"], rows))
        return max(item_counts, key=lambda x: item_counts[x])

    def average_price(self):
        #map to prices and calculate average
        if not self.records: 
            return 0
        prices = list(map(lambda r: r["price"], self.records))
        return sum(prices) / len(prices)
    
    def min_price(self):
        #Aggregate to find minimum price item
        if not self.records:
            return 0
        return min(map(lambda r: r["price"], self.records))
    
    def max_price(self):
        #Aggregate to find most priced item
        if not self.records:
            return 0
        return max(map(lambda r: r["price"], self.records))

    def print_analysis(self):
        print("Total Units Sold:", self.total_units())
        print("Total Revenue:", self.total_revenue())
        print("Revenue by Region:", self.revenue_by_region())
        print("Most Sold Item:", self.most_sold_item())
        print("Average Price:", self.average_price())
        print("Price Range: ", self.min_price(), "-", self.max_price())
