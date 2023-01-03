import ampelmann
from ampelmann.RoodGroen import RoodGroen

import json
import argparse
import pandas as pd

#
# Argument parsing
#

parser = argparse.ArgumentParser(description='ampelmann RoodGroen - corpus filtering for the red and green word order')
parser.add_argument('closed_items_path', type=str,
					help='Path to the JSON file containing the closed items which will narrow down the search space')
parser.add_argument('red_items_path', type=str,
					help='Path to the text file containing the corpus hits of the red order type')
parser.add_argument('green_items_path', type=str,
					help='Path to the text file containing the corpus hits of the green order type')
parser.add_argument('--output_path', type=str, nargs='?', default='RoodGroenAnthe.csv')

args = parser.parse_args()

#
# Load corpus files
#

print("DATA: Loading closed items")

# We use the "closed items" class as a way to narrow down the search space
with open(args.closed_items_path, "rt") as reader:
    closed_class_items = json.loads(reader.read())

print("DATA: Loading green sentences")

# All "green" items, thanks Bram Vanroy!
with open(args.green_items_path) as reader:
    green_sentences = reader.read().split("\n")

print("DATA: Loading red sentences")

# All "red" items, thanks Bram Vanroy!
with open(args.red_items_path) as reader:
    red_sentences = reader.read().split("\n")

# Build RoodGroen objects
green = RoodGroen(green_sentences, closed_class_items, "green")
red = RoodGroen(red_sentences, closed_class_items, "red")

print("FILTER: Filtering red and green items")

# Filter sentences and bin spurious hits
green_filtered_sentences, green_participles, green_auxiliaries = green.filter()
red_filtered_sentences, red_participles, red_auxiliaries = red.filter()

print("PANDAS: Preparing output")

# Create a dataframe with all results for the green order
green_df = pd.DataFrame({ "sentence": green_filtered_sentences,
                          "participle": green_participles,
                          "auxiliary": green_auxiliaries })
green_df["order"] = "green"

# Create a dataframe with all results for the red order
red_df = pd.DataFrame({ "sentence": red_filtered_sentences,
                        "participle": red_participles,
                        "auxiliary": red_auxiliaries })
red_df["order"] = "red"

# Combine both data frames
df = pd.concat([ green_df, red_df ])

print(f"PANDAS: Writing CSV file {args.output_path}")

# Write to CSV
df.to_csv(args.output_path, index=False)




