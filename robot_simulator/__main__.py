import sys
import argparse
from simulation import Simulation

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Robot simulator")
    parser.add_argument("file", type=argparse.FileType('r'),
        help="input file of simulation commands")
    args = parser.parse_args()

    simulation = Simulation()
    simulation.run_file(args.file)
