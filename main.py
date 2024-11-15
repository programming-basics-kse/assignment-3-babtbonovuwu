import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filepath', type=str, help='The path to the file with data')
parser.add_argument('-medals', '--medals', type=str, nargs=2, help="Enter '-medals country year' to see the particular country's result")
parser.add_argument('-total', '--total', type=int, nargs=1, help="Enter '-total year' to see the total result of Olympics")
parser.add_argument('-overall', '--overall', type=str, nargs='*', help="Enter '-overall country country...' to see the most successful year for each country")
parser.add_argument('--interactive', action='store_true', help="Enter '--interactive' to switch to the interactive mode (where you can enter the country and see its stats)")
args = parser.parse_args()


