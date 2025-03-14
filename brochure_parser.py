import requests
from bs4 import BeautifulSoup
import json
from brochure import Brochure


def fetch_brochure_data():
    try:
        response = requests.get('https://www.prospektmaschine.de/hypermarkte/', timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    html_data = BeautifulSoup(response.text, 'html.parser')
    return html_data.find_all('div', attrs={'class': 'brochure-thumb'})

def write_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    brochure_data = fetch_brochure_data()

    brochures = [Brochure(b).to_dict() for b in brochure_data]

    write_to_file(brochures, 'brochures.json')