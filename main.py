import argparse
from mylib.extract import extract
from mylib.transform_load import create_and_load_db
from mylib.query import query

parser = argparse.ArgumentParser(description="Process some data.")
parser.add_argument("-e", "--extract", action="store_true", help="Extract data")
parser.add_argument("-l", "--load", action="store_true", help="Load data")
parser.add_argument("-q", "--query", action="store_true", help="Query data")

args = parser.parse_args()

if args.extract:
    print("Extracting data...")
    extract()

if args.load:
    print("Creating DB and loading data...")
    create_and_load_db()

if args.query:
    print("Querying data...")
    query()
