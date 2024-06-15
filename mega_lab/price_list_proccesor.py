from get_data_from_website import GetData
import datetime
import glob
import os
import csv
import re

PRICE_LIST_SOURCE = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'
FINAL_FILE_NAME = 'cnic_price.csv'

def download_price_list(url):
    filename = 'cnic_price' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.xml'
    GetData(url).download_file('data', filename)

def get_latest_price(files: list) -> dict:
    latest_price = max(files, key=os.path.getctime)
    file = {
        'latest_price': latest_price,
        'index': files.index(latest_price)
    }
    return file

def read_xml_file(file_path: str):
    CsvHandler()  # Вызываем функцию для инициализации записи в CSV файл
    with open(file_path, "r") as f:
        currency = []
        rate = []
        for text in f:
            match = re.findall(r"<Cube\s+[^>]*?currency=([\'\'])(\w+)\1\s+[^>]*rate=([\'\'])([0-9.,]+)\1", text)
            #print(match)
            if len(match) > 0 :
                currency = match[0][1]
                rate = match[0][3]
                payload = {
                    'currency': currency,
                    'rate': rate,
                }
                write_to_csv(payload)


def CsvHandler():
    with open(FINAL_FILE_NAME, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['currency', 'rate']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def write_to_csv(data: dict):
    with open(FINAL_FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['currency', 'rate']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Проверяем, пустой ли файл
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(data)
def main():
    download_price_list(PRICE_LIST_SOURCE)
    list_of_files = glob.glob('data/*.xml')
    latest_price = get_latest_price(list_of_files)
    read_xml_file(latest_price.get('latest_price'))

if __name__ == '__main__':
    main()
