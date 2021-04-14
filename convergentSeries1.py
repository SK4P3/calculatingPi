import sys
import math
import time


# Todo better way to save more decimal places of float

class pi_calculator():

    def __init__(self, seed='Pi!'):
        self.k = 0
        self.sum = 0
        self.const = (2 * math.sqrt(2)) / 9801
        self.pi = 0
        self.iteratons = 0

    def estimate_pi(self, iterations):
        for i in range(iterations):
            dividend = math.factorial(4*self.k) * (1103 + 26390*self.k)
            divisor = (math.factorial(self.k)**4) * 396**(4*self.k)
            self.sum += dividend / divisor
            self.k += 1
        self.iteratons += iterations

    def calculate(self):
        self.pi = '{:.50f}'.format(math.pow(self.const * self.sum, -1))

    def __repr__(self):
        return f"Estimate {self.pi} in {self.iteratons} Iterations!"

    def run_for_n_sec(self, n, v=False):
        start_time = time.time()
        curr_time = time.time()
        while (curr_time - start_time < n):
            self.estimate_pi(100)
            if v:
                self.calculate()
                sys.stdout.write(f"\r{self}")
                sys.stdout.flush()
            curr_time = time.time()
        else:
            if not v:
                self.calculate()
                print(self)
            print("\n" + f"Finished in {curr_time - start_time}s!")

    def run_for_n_iter(self, n, v=False):
        start_time = time.time()

        if v:
            for _ in range(round(n/100)):
                self.estimate_pi(100)
                self.calculate()
                sys.stdout.write(f"\r{self}")
                sys.stdout.flush()
        else:
            self.estimate_pi(n)
            self.calculate()
            print(self)

        curr_time = time.time()
        print("\n" + f"Finished in {curr_time - start_time}s!")

if __name__ == '__main__':
    instance = pi_calculator()
    instance.run_for_n_sec(.1, v=True)