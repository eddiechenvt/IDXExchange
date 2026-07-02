import pandas as pd
from pathlib import Path

# Root and CSV 
ROOT = Path(__file__).resolve().parents[1]
CSV_DIR = ROOT / "csv"


# File paths
sold_path = CSV_DIR / "sold.csv"
listings_path = CSV_DIR / "listings.csv"


#Reads the csv files
sold = pd.read_csv(sold_path, low_memory=False)
listings = pd.read_csv(listings_path, low_memory=False)

# Shows how many rows and columns in sold dataset
print("SOLD DATASET")
print("Rows, columns:", sold.shape)


# Shows how many rows and columns in listing dataset
print("\nLISTINGS DATASET")
print("Rows, columns:", listings.shape)

# Market Analysis Fields
market_fields = [
    "ListPrice",
    "ClosePrice",
    "LivingArea",
    "BedroomsTotal",
    "BathroomsTotalInteger",
    "PropertyType",
    "PropertySubType",
    "City",
    "CountyOrParish",
    "DaysOnMarket",
    "CloseDate",
    "ListingContractDate",
    "StandardStatus"
]

# Metadata fields
metadata_fields = [
    "ListingKey",
    "ListingId",
    "ModificationTimestamp",
    "PhotosChangeTimestamp",
    "PhotosCount",
    "BuyerAgentKey",
    "BuyerAgentEmail",
    "BuyerOfficePhone",
    "CopyrightNotice"
]