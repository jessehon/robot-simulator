import sys
from simulation import Simulation

if __name__ == "__main__":
    simulation = Simulation()

    for line in sys.stdin:
        simulation.run(line)
