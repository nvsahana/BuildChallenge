import unittest
from producer_consumer import run_producer_consumer


class TestProducerConsumer(unittest.TestCase):
    
    def test_producer_consumer_simple(self):
        print("\nTest 1: Simple test with 5 items")
        source = [1, 2, 3, 4, 5]
        result = run_producer_consumer(source)
        self.assertEqual(result, source)
        print("Successfully transferred 5 items through producer-consumer queue")

    def test_producer_consumer_large(self):
        print("\nTest 2: Large dataset with 100 items")
        source = list(range(100))
        result = run_producer_consumer(source)
        self.assertEqual(result, source)
        print("Successfully transferred 100 items with thread synchronization")

    def test_producer_consumer_empty(self): 
        print("\nTest 3: Empty source")
        source = []
        result = run_producer_consumer(source)
        self.assertEqual(result, [])
        print("Handled empty source correctly")


if __name__ == "__main__":
    unittest.main()
