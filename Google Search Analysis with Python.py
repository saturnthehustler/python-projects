import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# Create a TrendReq object
trends = TrendReq()

# Build the payload for the search term "Machine Learning"
trends.build_payload(kw_list=["Machine Learning"])

# Retrieve the interest by region data
data = trends.interest_by_region()

# Add a geoName column to the data DataFrame
data = data.assign(geoName=data.index)

# Sort the data by search interest in descending order
data = data.sort_values(by="Machine Learning", ascending=False)

# Get the top 10 regions with the highest search interest
top_10_regions = data.head(10)

# Set the index of the top_10_regions DataFrame to the geoName column
top_10_regions = top_10_regions.set_index("geoName")

# Print the top 10 regions
print("Top 10 regions with the highest search interest for 'Machine Learning':")
print(top_10_regions)

# Plot the search interest over time for the top 10 regions
plt.figure(figsize=(10, 6))
top_10_regions.plot(y="Machine Learning", kind="bar")
plt.title("Search Interest for 'Machine Learning' by Region")
plt.xlabel("Region")
plt.ylabel("Search Interest")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Machine Learning'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data['Machine Learning'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Machine Learning', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()
