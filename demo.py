#!/usr/bin/env python3
"""
Demo script to showcase both assignments
Runs both producer-consumer and sales analysis demonstrations
"""

import sys
import os

# Add assignment directories to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'assignment-1'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'assignment-2'))

from producer_consumer import run_producer_consumer
from sales_analysis import SalesAnalysis


def demo_producer_consumer():
    """Demonstrate Assignment 1: Producer-Consumer Pattern"""
    print("=" * 60)
    print("ASSIGNMENT 1: Producer-Consumer Pattern (PC-001)")
    print("=" * 60)
    print("\nDemonstrating thread synchronization with blocking queue...")
    print("\nTest 1: Small dataset (10 items)")
    
    source = list(range(1, 11))
    print(f"Source data: {source}")
    
    result = run_producer_consumer(source)
    print(f"Result data: {result}")
    print(f"Success: {source == result}")
    
    print("\nTest 2: Large dataset (50 items)")
    source_large = list(range(1, 51))
    result_large = run_producer_consumer(source_large)
    print(f"Source: [{source_large[0]}, {source_large[1]}, ..., {source_large[-2]}, {source_large[-1]}]")
    print(f"Result: [{result_large[0]}, {result_large[1]}, ..., {result_large[-2]}, {result_large[-1]}]")
    print(f"Success: {source_large == result_large}")
    print("\n")


def demo_sales_analysis():
    """Demonstrate Assignment 2: Sales Analysis"""
    print("=" * 60)
    print("ASSIGNMENT 2: Sales Data Analysis (SA-001)")
    print("=" * 60)
    print("\nPerforming functional programming operations on CSV data...")
    
    # Get path to CSV file
    csv_path = os.path.join(os.path.dirname(__file__), "data", "sales_data.csv")
    
    # Initialize analysis
    sa = SalesAnalysis(csv_path)
    
    # Print comprehensive analysis
    print("\nSALES ANALYSIS RESULTS")
    print("-" * 60)
    sa.print_analysis()
    print("-" * 60)
    
    # Additional detailed output
    print("\nDETAILED BREAKDOWN")
    print("-" * 60)
    
    revenue_by_region = sa.revenue_by_region()
    print("\nRevenue by Region:")
    for region, revenue in sorted(revenue_by_region.items()):
        print(f"  {region:10} : ${revenue:,.2f}")
    
    print(f"\nMost Popular Item: {sa.most_sold_item()}")
    print(f"Total Units Sold: {sa.total_units():,}")
    print(f"Total Revenue: ${sa.total_revenue():,.2f}")
    print(f"Average Price: ${sa.average_price():.2f}")
    print("\n")


def main():
    """Run all demonstrations"""
    print("\n" + "=" * 60)
    print("BUILD CHALLENGE - PYTHON IMPLEMENTATION DEMO")
    print("=" * 60)
    print()
    
    try:
        # Run Assignment 1 demo
        demo_producer_consumer()
        
        # Run Assignment 2 demo
        demo_sales_analysis()
        
        print("=" * 60)
        print(" ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY")
        print("=" * 60)
        print("\nTo run unit tests, use:")
        print("  ./setup.sh")
        print("\n")
        
    except Exception as e:
        print(f"\n Error during demonstration: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
