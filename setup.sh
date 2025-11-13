#!/bin/bash

# BuildChallenge Setup Script
# This script sets up the environment and runs the tests

echo "========================================"
echo "BuildChallenge Setup"
echo "========================================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

echo ""
echo "========================================"
echo "Installing requirements..."
echo "========================================"
# Since we only use standard library, this is just a check
pip3 install -r requirements.txt 2>/dev/null || echo "No external dependencies needed - using Python standard library only"

echo ""
echo "========================================"
echo "Running Assignment 1 Tests"
echo "========================================"
cd assignment-1
python3 main_test_producer_consumer.py
cd ..

echo ""
echo "========================================"
echo "Running Assignment 2 Tests"
echo "========================================"
cd assignment-2
python3 main_test_sales_analysis.py
cd ..

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
