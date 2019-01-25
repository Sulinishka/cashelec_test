import async_benchmark
import unittest

class TestStringMethods(unittest.TestCase):
    setup_done = False
     
    def setUp(self):
        if not self.setup_done:    
            self.__class__.benchmark = async_benchmark.Benchmark()
            self.__class__.setup_done = True

    
    def test_80_percentile_delay(self):
        self.assertTrue(self.benchmark.percentile_80<450)
    
    def test_rps(self):
        self.assertTrue(self.benchmark.rps>5)
    
if __name__ == '__main__':
    unittest.main()
