# Robot Simulator

## Description
This application is completed as a task following this [brief](BRIEF.md).
The result is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units.

## Requirements
Though Python on most desktop platforms should behave the same, it may be worth noting that the application was developed on Mac OS X 10.9.4 and tested using Python 2.7.5.
The application is compatible with the following versions.

    Python >= 2.6.5

To check your version run:

    $ python --version

## Installation
To install the application and be able to use `robotsimulator` from command line, invoke

    $ python setup.py install

or alternatively you can simply run the application file without installing (see Usage below)

## Usage
A sequence of commands can be fed into the simulation to interact with the toy robot such as moving, turning or reporting location.

* `PLACE X,Y,F` will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
* `MOVE` will move the toy robot one unit forward in the direction it is currently facing.
* `LEFT` and `RIGHT` will rotate the robot 90 degrees in the specified direction without changing the position of the robot.
* `REPORT` will announce the X,Y and F of the robot.

Notes
* The origin (0,0) can be considered to be the SOUTH WEST most corner.
* The first valid command to the robot is a `PLACE` command, after that, any sequence of commands may be issued, in any order, including another `PLACE` command. The application will discard all commands in the sequence until a valid `PLACE` command has been executed

### Examples
```
a)
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH

b)
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST

c)
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
```

### Running simulation
The application can either accept commands from STDIN through interactive mode or from an input file where there is one command per line.

#### When installed
In interactive mode:

    $ robotsimulator

With input file:

    $ cat /path/to/input | robotsimulator

#### When not installed
In interactive mode:

    $ python /path/to/repo/robot_simulator

With input file:

    $ cat /path/to/input | python /path/to/repo/robot_simulator

## Testing

### Prerequisites
The nose testing library is a prerequisite for running this application's unit tests and will have to be installed.
The easiest way is running the following with `pip` if it is installed, which installs all the test prerequisites.

    $ pip install -r /path/to/repo/requirements-test.txt

More information can be found here https://nose.readthedocs.org/en/latest/

### Running unit tests
With nose installed, navigate to the repo directory and run

    $ nosetests
