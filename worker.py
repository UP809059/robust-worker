from globals import *
from netutils import send_message_to_colleague

def _is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False

    return True


class Worker:
    _found_primes = []

    def Worker(self):
        print("Worker created")

    def handle_colleague_death(self):
        pass

    def get_progress(self):
        print("Returning progress. Vector of ", len(self._found_primes), " primes")
        to_return = self._found_primes
        print("Clearing found primes")
        self._found_primes = []
        return to_return


    def resume_work(self,start,last_value):
        print("Resuming dead nodes work")
        block_start = (start//WORK_BLOCK_SIZE)*WORK_BLOCK_SIZE
        block_end = block_start + WORK_BLOCK_SIZE
        for num in range(last_value, block_end):
            if _is_prime(num):
                # print("Found prime:", num)
                self._found_primes.append(num)
        print("Found ", len(self._found_primes), " in their remaining work unit")

    def work(self, start):
        start = int(start)
        print("Finding primes in block starting:",start)
        half_block = int(WORK_BLOCK_SIZE/2)
        for num in range(start, start + half_block):
            if _is_prime(num):
                # print("Found prime:", num)
                self._found_primes.append(num)
        print("Found ", len(self._found_primes), " in block")
        # TODO sync with colleague now
        for num in range(start+half_block, start + WORK_BLOCK_SIZE):
            if _is_prime(num):
                # print("Found prime:", num)
                self._found_primes.append(num)
        print("Found ", len(self._found_primes), " in block")
