import sys
from simulation import Simulation

def main():
    simulation = Simulation()

    for line in sys.stdin:
        simulation.run(line)

if __name__ == "__main__":
    main()
