# Build Challenge - Python Implementation

This repository contains implementations of two programming assignments demonstrating concurrent programming and data analysis.

## Project Structure
```
BuildChallenge/
├── assignment-1/
│   ├── producer_consumer.py
│   └── main_test_producer_consumer.py
├── assignment-2/
│   ├── sales_analysis.py
│   └── main_test_sales_analysis.py
├── data/
│   └── sales_data.csv
├── demo.py
├── setup.sh
└── README.md
```

## Quick Start

```bash
chmod +x setup.sh
./setup.sh
```

Or run the demo:
```bash
python3 demo.py
```

## Assignment 1: Producer-Consumer Pattern

Implements thread synchronization with:
- Blocking queue with condition variables
- Wait/notify mechanism
- Producer and Consumer threads
- Poison pill shutdown

**Run tests:**
```bash
cd assignment-1
python3 main_test_producer_consumer.py
```

## Assignment 2: Sales Analysis

Performs data analysis using:
- Lambda expressions and map()
- Stream operations
- Functional grouping with groupby()
- Aggregate functions (sum, min, max, avg)

**Run tests:**
```bash
cd assignment-2
python3 main_test_sales_analysis.py
```

## Sample Output

**Assignment 1:** 3 tests (simple, large dataset, empty source)
```
Ran 3 tests in 1.278s - OK
```

**Assignment 2:** 6 tests (all aggregation methods)
```
Ran 6 tests in 0.001s - OK

Total Units: 213
Total Revenue: $5,685.00
Most Sold Item: Socks
Average Price: $37.40
Price Range: $5.00 - $80.00
Revenue by Region: East ($1,545), North ($1,210), South ($1,305), West ($1,625)
```

## Requirements

- Python 3.7+
- Standard library only

## Author

Sahana NV
