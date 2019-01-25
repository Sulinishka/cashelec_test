import async_benchmark
import unittest

class TestStringMethods(unittest.TestCase):
   
    def setUp(self):
        self.benchmark = async_benchmark.Benchmark()
    
    def test_80_percentile_delay(self):
        self.assertTrue(self.benchmark.percentile_80<450)
    
    def test_rps(self):
        self.assertTrue(self.benchmark.rps>5)
    
if __name__ == '__main__':
    unittest.main()