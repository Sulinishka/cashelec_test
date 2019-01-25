import asyncio
import numpy as np
import requests
import functools
import random
import time
from concurrent.futures import ThreadPoolExecutor
import test_wrapper


class Benchmark():
    MAX_WORKERS = 8
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    
    def __init__(self):
        self.responses = []
        self.request_api = test_wrapper.RequestAPI()
        self.loop = asyncio.get_event_loop()
        start_time = time.time()
        self.loop.run_until_complete(self.parallel_request())
        self.elapsed_time = time.time() - start_time
        self.rps = self.MAX_WORKERS/self.elapsed_time
        self.percentile_80 = np.percentile(self.responses, 80)

    async def parallel_request(self): 
        futures = []
        for n in range(self.MAX_WORKERS):
            future = self.loop.run_in_executor(self.executor, self.request_api.get_ping)
            futures.append(future)

        for each in futures:
            self.responses.append(await each)