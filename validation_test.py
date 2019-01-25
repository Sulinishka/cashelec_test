import unittest
import datetime
import test_wrapper


class TestStringMethods(unittest.TestCase):
    setup_done = False
    
    def setUp(self):
        if not self.setup_done:
            self.request_api = test_wrapper.Request_API()
            self.setup_done = True
    
    def test_endpoints_resp_time(self):
        pings = [self.request_api.get_ping(url) for url in self.request_api.urls]
        self.assertTrue([each<500 for each in pings])
        
    def test_endpoints_packet_size(self):
        packet_sizes = [self.request_api.get_packet_size(url) for url in self.request_api.urls]
        self.assertTrue([each<10 for each in packet_sizes])
        
    def test_endpoints_validate_day(self):
        deltas = [self.request_api.get_last_update_delta(url) for url in self.request_api.urls]
        self.assertTrue([each==0 for each in deltas])
    
if __name__ == '__main__':
    unittest.main()
