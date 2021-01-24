User Documentation: Usage
---
Prereqs: pygame, matplotlib, pandas
`pip3 install pygame && pip3 install matplotlib && pip3 install pandas`

```
usage: python3 main.py [-h] [--students FILE] [--teachers FILE] [--tas FILE] [--infects FILE] [-v]

Simulate transmission of ZBY1 in a school

optional arguments:
  -h, --help       show this help message and exit
  --students FILE  CSV to load student data from
  --teachers FILE  CSV to load teacher data from
  --tas FILE       CSV to load TA data from
  --infects FILE   CSV to load infection data from
  -v, --visualize  Visualize transmissions using pygame
```

After running, a few graphs summarizing the result of the simulation over time should display

Demo: https://www.youtube.com/watch?v=iRJgq1vo3ow

Developer Documentation: Modules
---
* Person: Stores information for each person regarding their percentage of exposure
* ExposureChance: represents a specific scenario in which exposure can occur, used to calculate exposure events with a group of people
* Parsers: Reads information in from csv files
* Graph: Collects information as the simulation runs, to produce a graph at the end
* Constants: Holds all constants relating to the simulation. These are collected together so they can easily be tweaked for sensitivity testing
* Main: Command line, main simulation logic, and UI


Initial Brainstorming
---
* Components
    * Data representation
        * Exposure opportunities: situations or locations in which a group of people are together and may have a chance to expose one another to the virus
        * People: Students, teachers, and TAs who may be exposed or expose others to the virus
        * Assigned to: Callum
    * Parsing: Load data from files, and produce the corresponding objects
        * Convert XLSX -> CSV for easier parsing using pandas
        * Assigned to: Max
    * Visualization: Graphs and potentially animated UI time-permitting
        * Assigned to: Robbie
    * Main simulation loop: Using other components, step through the day by period and simulate possible exposures
        * Assigned to: Bimesh
* Virus transmission
    * Each person has a persistent probability that they have been exposed to a virus
    * Each time two people spend a time interval together, they will transmit the virus with probability (probability A has the virus at this stage \* probability A transmits the virus to B)
    * TAs work closely with teachers -> virus transmission depends on occupation of each participant
