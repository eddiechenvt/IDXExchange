import pandas as pd
from pathlib import Path

# main project folder
ROOT = Path(__file__).resolve().parents[1]

# folder where monthly CSV files are stored
CSV_DIR = ROOT / "csv"

# output folder
OUTPUT_DIR = ROOT / "csv"

# function to load and clean files
def load_monthly_files(prefix):
    files = sorted(CSV_DIR.glob(f"{prefix}*.csv"))

    dataframes = []

    print(f"\nFound {len(files)} files for {prefix}")

    for file in files:
        print(f"Reading: {file.name}")

        df = pd.read_csv(file, low_memory=False)

        # If file has _filled in name, remove last 2 columns
        if "_filled" in file.stem:
            print("  _filled file detected: dropping last 2 columns")
            df = df.iloc[:, :-2]

        print(f"  Rows: {len(df)}, Columns: {len(df.columns)}")
        dataframes.append(df)

    combined = pd.concat(dataframes, ignore_index=True)

    return combined

# before fitlering to residential
listings = load_monthly_files("CRMLSListing")
sold = load_monthly_files("CRMLSSold")
#prints before residential fitler
print("\nBefore Residential filter:")
print(f"Listings rows: {len(listings)}")
print(f"Sold rows: {len(sold)}")

# fitler to residential
listings = listings[listings["PropertyType"] == "Residential"]
sold = sold[sold["PropertyType"] == "Residential"]

# prints after fitlering to residential
print("\nAfter Residential filter:")
print(f"Listings rows: {len(listings)}")
print(f"Sold rows: {len(sold)}")

# Saves the csv files to output folder
listings.to_csv(OUTPUT_DIR / "listings.csv", index=False)
sold.to_csv(OUTPUT_DIR / "sold.csv", index=False)

# Confirms the files were saved
print("\nSaved:")
print(OUTPUT_DIR / "listings.csv")
print(OUTPUT_DIR / "sold.csv")
