import requests as re
from bs4 import BeautifulSoup as bs
import pandas as pd

data = {
    'Laptop Model': [],
    'Processor Type': [],
    'Generation': [],
    'RAM': [],
    'Storage': [],
    'Graphics': [],
    'Display Size(Inch)': [],
    'Price': []
}

for j in range(1, 20):
    url = f'https://www.ryans.com/category/laptop-all-laptop?page={j}'
    response = re.get(url)
    soup = bs(response.text, 'html.parser')
    box = soup.find_all('div', class_='card-body text-center')

    for i in range(len(box)):
        laptop_model = box[i].find('a', rel='noreferrer').text.strip()
        category_des = box[i].find('div', class_ = 'short-desc-attr')
        description = category_des.find_all('li')
        processor_type = description[0].text.strip().split('-')[1].strip()
        generation = description[1].text.strip().split('-')[1].strip()
        ram = description[2].text.strip().split('-')[1].strip()
        storage = description[3].text.strip().split('-')[1].strip()
        graphics = description[4].text.strip().split('-')[1].strip()
        try:
            display_size = description[5].text.strip().split('-')[1].strip()
        except:
            display_size = 'N/A'
        price = box[i].find('a', class_ = 'pr-text cat-sp-text pb-1 text-dark text-decoration-none').text.strip()
        data['Laptop Model'].append(laptop_model)
        data['Processor Type'].append(processor_type)
        data['Generation'].append(generation)
        data['RAM'].append(ram)
        data['Storage'].append(storage)
        data['Graphics'].append(graphics)
        data['Display Size(Inch)'].append(display_size)
        data['Price'].append(price)
    print(f'Page {j} done')

df = pd.DataFrame(data)
df.to_csv('updatedlaptop.csv', index=False)

