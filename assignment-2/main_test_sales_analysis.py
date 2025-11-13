import unittest
from sales_analysis import SalesAnalysis
import os


class TestSalesAnalysisOptimized(unittest.TestCase):

    def setUp(self):
        #Get the directory of this test file and navigate to data folder
        test_dir = os.path.dirname(os.path.abspath(__file__))
        #Go up to BuildChallenge directory and then into data folder
        csv_path = os.path.join(os.path.dirname(test_dir), "data", "sales_data.csv")
        self.sa = SalesAnalysis(csv_path)

    def test_total_units(self):
        print("\nTest 1: Calculating total units sold")
        result = self.sa.total_units()
        self.assertTrue(result > 0)
        print(f" Total units: {result}")

    def test_total_revenue(self):
        print("\nTest 2: Calculating total revenue")
        result = self.sa.total_revenue()
        self.assertTrue(result > 0)
        print(f" Total revenue: ${result:,.2f}")

    def test_revenue_by_region(self):
        print("\nTest 3: Grouping revenue by region")
        regions = self.sa.revenue_by_region()
        self.assertTrue(isinstance(regions, dict))
        self.assertTrue(len(regions) >= 1)
        print(f" Found {len(regions)} regions: {list(regions.keys())}")

    def test_most_sold_item(self):
        print("\nTest 4: Finding most sold item")
        item = self.sa.most_sold_item()
        self.assertTrue(isinstance(item, str))
        print(f" Most sold item: {item}")

    def test_avg_price(self):
        print("\nTest 5: Calculating average price")
        avg = self.sa.average_price()
        self.assertGreater(avg, 0)
        print(f" Average price: ${avg:.2f}")

    def test_print_analysis(self):
        print("\nTest 6: Full analysis output")
        self.sa.print_analysis()
        print(" Analysis complete")


if __name__ == "__main__":
    unittest.main()
