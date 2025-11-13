# Build Challenge - Python Implementation

This repository contains implementations of two programming assignments demonstrating concurrent programming and data analysis.

## Overview

- **Assignment 1**: Producer-consumer pattern with thread synchronization
- **Assignment 2**: Sales data analysis using functional programming

## Requirements

- Python 3.7+
- Standard library only (no external dependencies)

## Quick Start

```bash
chmod +x setup.sh
./setup.sh
```

Or run the demo:
```bash
python3 demo.py
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/nvsahana/BuildChallenge.git
cd BuildChallenge
```

2. Make setup script executable and run:
```bash
chmod +x setup.sh
./setup.sh
```

Or run tests manually (see sections below)

## Assignment 1: Producer-Consumer Pattern (PC-001)

### Description
Implements a classic producer-consumer pattern with thread synchronization demonstrating:
- Custom blocking queue with condition variables
- Producer thread that reads from source and places items in queue
- Consumer thread that reads from queue and stores in destination
- Thread-safe operations using `threading.Condition`
- Graceful shutdown using poison pill pattern

### Key Features
- **BlockingQueue**: Thread-safe queue with wait/notify mechanism
- **Producer Thread**: Simulates data production with controlled timing
- **Consumer Thread**: Processes items with concurrent access
- **Synchronization**: Proper use of locks and condition variables

### File Structure
```
assignment-1/
├── producer_consumer.py       # Main implementation
└── main_test_producer_consumer.py  # Unit tests
```

### Running Assignment 1

```bash
cd assignment-1
python3 main_test_producer_consumer.py
```

### Code Highlights
```python
# Thread-safe blocking queue with condition variables
class BlockingQueue:
    def put(self, item):
        with self.condition:
            while len(self.queue) >= self.max_size:
                self.condition.wait()
            self.queue.append(item)
            self.condition.notify_all()
```

## Assignment 2: Sales Analysis (SA-001)

### Description
Performs comprehensive data analysis on CSV sales data demonstrating:
- Functional programming paradigms
- Data aggregation operations
- Lambda expressions and higher-order functions
- CSV parsing and validation
- Security measures (CSV injection protection, path validation)

### Key Features
- **Data Aggregation**: Sum, average, grouping operations
- **Functional Programming**: Uses `groupby`, `itemgetter`, list comprehensions
- **CSV Security**: Input validation and injection prevention
- **Path Security**: Restricts file access to authorized directories

### Analysis Operations
1. `total_units()` - Calculate total units sold across all records
2. `total_revenue()` - Calculate total revenue (units × price)
3. `revenue_by_region()` - Group and aggregate revenue by region
4. `most_sold_item()` - Find item with highest unit sales
5. `average_price()` - Calculate average price across all items

### File Structure
```
assignment-2/
├── sales_analysis.py          # Main implementation
└── main_test_sales_analysis.py     # Unit tests
data/
└── sales_data.csv             # Sample sales data
```

### Running Assignment 2

```bash
cd assignment-2
python3 main_test_sales_analysis.py
```

### Code Highlights
```python
# Functional programming with groupby
def revenue_by_region(self):
    self.records.sort(key=itemgetter("region"))
    return {
        region: sum(r["units"] * r["price"] for r in rows)
        for region, rows in groupby(self.records, key=itemgetter("region"))
    }
```

## Running Tests

### Run All Tests
```bash
./setup.sh
```

### Run Individual Assignment Tests

**Assignment 1:**
```bash
cd assignment-1
python3 main_test_producer_consumer.py
```

**Assignment 2:**
```bash
cd assignment-2
python3 main_test_sales_analysis.py
```

## Sample Output

### Assignment 1 Output
```
..
----------------------------------------------------------------------
Ran 2 tests in 1.299s

OK
```

### Assignment 2 Output
```
..INFO:SalesAnalysis:Total Units Sold: 213
INFO:SalesAnalysis:Total Revenue: 5685.0
INFO:SalesAnalysis:Revenue by Region: {'East': 1545.0, 'North': 1210.0, 'South': 1305.0, 'West': 1625.0}
INFO:SalesAnalysis:Most Sold Item: Socks
INFO:SalesAnalysis:Average Price: 37.40
....
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

### Analysis Results Breakdown

| Metric | Value |
|--------|-------|
| Total Units Sold | 213 |
| Total Revenue | $5,685.00 |
| Average Price | $37.40 |
| Most Sold Item | Socks |

**Revenue by Region:**
- East: $1,545.00
- North: $1,210.00
- South: $1,305.00
- West: $1,625.00

## Project Structure
```
BuildChallenge/
├── README.md                   # This file
├── requirements.txt            # Python dependencies (none required)
├── setup.sh                    # Quick setup and test script
├── assignment-1/
│   ├── producer_consumer.py
│   └── main_test_producer_consumer.py
├── assignment-2/
│   ├── sales_analysis.py
│   └── main_test_sales_analysis.py
└── data/
    └── sales_data.csv
```

## Implementation Highlights

### Thread Synchronization (Assignment 1)
- Uses `threading.Condition` for proper wait/notify mechanism
- Implements blocking behavior when queue is full or empty
- Demonstrates clean thread shutdown with poison pill pattern
- Includes comprehensive unit tests for simple and large datasets

### Functional Programming (Assignment 2)
- Leverages Python's functional programming features
- Uses `itertools.groupby` for efficient grouping
- Employs lambda expressions and list comprehensions
- Implements CSV security best practices
- Provides detailed logging of analysis results

## Testing

Both assignments include comprehensive unit tests:
- **Assignment 1**: Tests with simple and large datasets (100 items)
- **Assignment 2**: Tests all aggregation methods with assertions

All tests pass successfully and demonstrate correct implementation of required features.

## Author

Sahana NV

## License

This project is part of a coding challenge assessment.
