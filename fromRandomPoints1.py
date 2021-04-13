import random
import math
import sys
import time

# Calculate Pi based on two random points.
# If these two random points have a distance <= 1 from the 'origin' we can count if they were in the upper right quater of a circle with r=1
# Then if we substitute in the area formula of a circle the relation between 'points_in_circle' 'total_points' we can estimate pi

# run_for_n_sec:
# - calculates 100 iterations at a time for n sec
# - v... Verbose mode for dymamically displaying the current estimation in the command line (performance decrease, ≈half as fast)

# run_for_n_iter:
# - calculates n iterations
# - v... Verbose mode for dymamically displaying the current estimation in the command line (performance decrease, ≈half as fast)

class pi_calculator():

    def __init__(self):
        self.points_in_circle = 0
        self.cnt_points_total = 0
        self.pi = 0
        self.iteratons = 0

    def estimate_pi(self, iterations):
        for i in range(iterations):
            xCor = random.uniform(0,1)
            yCor = random.uniform(0,1)
            distance_to_origin = math.pow(xCor,2) + math.pow(yCor,2)
            if distance_to_origin <= 1: self.points_in_circle += 1
            self.cnt_points_total += 1
        self.iteratons += iterations

    def calculate(self):
        self.pi = '{:.15f}'.format(4 * self.points_in_circle / self.cnt_points_total)

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
    instance.run_for_n_sec(60)
    # instance.run_for_n_iter(5000000)