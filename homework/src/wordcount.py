# python3 -m homework data/input data/output
import sys
from homework.src._internals.parse_args import parse_args


def main():
    input_folder, output_folder = parse_args()
