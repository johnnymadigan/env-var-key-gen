#!/bin/bash

# Assign API KEY CSV values to the API_KEY env variable (comma-separated)

csvfile="out/api-keys-db.csv"
keys=""

while IFS= read -r line; do
    line=$(echo "$line" | tr -d '[:space:]')  # strip leading and trailing spaces
    keys="$keys,$line"
done < "$csvfile"

keys=${keys:1} # remove leading ','

export API_KEY="$keys"

echo $API_KEY
