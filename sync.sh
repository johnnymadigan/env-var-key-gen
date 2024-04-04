#!/bin/bash

# Assign API KEY CSV values to API_KEY env variable (comma-separated)

csvfile="out/api-keys-db.csv"
keys=""

while IFS= read -r line; do
    line=$(echo "$line" | tr -d '[:space:]')  # Remove leading and trailing spaces
    keys="$keys,$line"
done < "$csvfile"

keys=${keys:1} # remove leading ','

# echo $keys

export API_KEY="$keys"

echo $API_KEY
