# 
# Imports
#

print("Initialising")

import pandas as pd

import ampelmann
from ampelmann.RoodGroen import RoodGroen

import json

#
# Load corpus files
#

print("DATA: Loading closed items")

# We use the "closed items" class as a way to narrow down the search space
with open("closed_items_Rood_Groen.json", "rt") as reader:
    closed_class_items = json.loads(reader.read())

print("DATA: Loading green sentences")

# All "green" items, thanks Bram Vanroy!
with open("WRPPB-groen.txt") as reader:
    green_sentences = reader.read().split("\n")

print("DATA: Loading red sentences")

# All "red" items, thanks Bram Vanroy!
with open("WRPPB-rood.txt") as reader:
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

print("PANDAS: Writing CSV file")

# Write to CSV
df.to_csv("RoodGroenAnthe.csv", index=False)




