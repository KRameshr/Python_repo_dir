import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# --- 1. CONFIGURATION & REQUEST ---
wiki_link = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.get(wiki_link, headers=headers)

# --- 2. VALIDATION & STORAGE ---
if response.status_code == 200:
    print(f"Status: {response.status_code} | Encoding: {response.encoding}")
    print("--- Successfully accessed Wikipedia ---")

    # Save raw HTML for offline reference
    with open("wikipedia_asia.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    
    # --- 3. PARSING DATA ---
    soup = BeautifulSoup(response.text, 'lxml')
    right_table = soup.find("table", class_="wikitable")
    all_rows = right_table.find_all('tr')

    country = []
    list_area = []

    for row in all_rows:
        col = row.find_all('td')
        if len(col) > 2:
            a_tag = col[1].find('a')
            if a_tag and a_tag.get('title'):
                title = a_tag.get('title')
                country.append(title)
                
                # Cleaning the percentage text
                area_text = col[2].text.strip().replace('%', '')
                list_area.append(area_text)

    # --- 4. DATA ANALYSIS WITH PANDAS ---
    min_length = min(len(country), len(list_area))
    data = {
        "Country": country[:min_length],
        "Area": list_area[:min_length]
    }
    
    df = pd.DataFrame(data)
    
    # Ensure 'Area' is a float for calculations
    df['Area'] = df['Area'].astype(str).str.replace('%', '').astype(float)
    
    print("\n--- Pandas DataFrame (Top 5) ---")
    print(df.head())

    # Exporting results
    df.to_csv("asia_area_analysis.csv", index=False)
    df.to_excel("asia_area_analysis.xlsx", index=False)

    # --- 5. VISUALIZATION ---
    df_sorted = df.sort_values(by='Area', ascending=True).tail(15)

    plt.figure(figsize=(10, 8))
    plt.barh(df_sorted['Country'], df_sorted['Area'], color='skyblue')
    plt.xlabel('Percentage of Total Asian Area (%)')
    plt.ylabel('Country')
    plt.title('Top 15 Asian Countries by Area Percentage')
    
    plt.tight_layout()
    plt.savefig('asia_area_chart.png') # Save before showing
    plt.show()

else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")