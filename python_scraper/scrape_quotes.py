import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the website
url = "http://quotes.toscrape.com/"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

# Extract the quotes and authors
quotes = [q.get_text(strip=True) for q in soup.select(".text")][:10]
authors = [a.get_text(strip=True) for a in soup.select(".author")][:10]

# Combine into a DataFrame
df = pd.DataFrame({"quote": quotes, "author": authors})

# Save to CSV
df.to_csv("quotes.csv", index=False)

# Print the first 5 rows
print("✅ Saved CSV as quotes.csv")
print(df.head())
