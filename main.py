import argparse
import logging
import sys
import time
import configparser

from blocks.Stack import Stack
from blocks.Table import Table
from blocks.Node import Node
from blocks.Adventurer import Adventurer

def parse_args(argv):
    logging.info("Parsing arguments")
    parser = argparse.ArgumentParser(description="The arguments")
    reqs = parser.add_argument_group("required named arguments")
    reqs.add_argument("-f", "--config-file", help="Name of the config file to read",
                      required=False)
    reqs.add_argument("-s", "--solver", help="Solver applied [w|d|a|I]: [w]idth, [d]epth, [a]* (recursive)," +
                                             " [i] a* iterative (default [i])", default="i")
    return parser.parse_args(argv)

def parseStates(arguments):
    if arguments.config_file:
        config = configparser.ConfigParser()
        config.read(arguments.config_file)
        s = Stack(config['initial']['stack'].split(','))
        t = Table(set(config['initial']['table'].split(',')))
        n = Node(stack_status=s, table_status=t)

        gs = Stack(config['goal']['stack'].split(','))
        gt = Table(set(config['goal']['table'].split(',')))
        gn = Node(stack_status=gs, table_status=gt, name="Goal")
    else:
        print("Using default configuration")
        s = Stack(["E", "D", "A", "K", "F", "I", "M"])
        t = Table({"L", "C", "B", "G", "H", "J"})
        n = Node(stack_status=s, table_status=t)

        gs = Stack(["J", "D", "L", "K", "C", "H", "E"])
        gt = Table({"A", "G", "B", "I", "F", "M"})
        gn = Node(stack_status=gs, table_status=gt, name="Goal")
    return n, gn

def main():
    logging.basicConfig(filename='output.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s')
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("Init!")
    argv = sys.argv
    arguments = parse_args(argv[1:])
    initial_state, goal_state = parseStates(arguments)

    print(initial_state)
    print(goal_state)
    print("START!")
    logging.info("Starting new search... \n{}\n{}".format(initial_state, goal_state))

    a = Adventurer(initial_node = initial_state, goal = goal_state)
    solution, _ = a.solve(solver=arguments.solver.lower())
    logging.info("Solution reached:\n {}\nExit\n===================================\n\n".format(solution))

    print("Exit.")

if __name__ == '__main__':
    main()




