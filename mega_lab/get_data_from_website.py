import bs4 
import requests
import os

UserAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0'

class GetData:
    Response = requests.models.Response

    def __init__(self, url: str):
        self.url = url

    def get_html(self) -> Response:
        user = self.__get_headers_proxy()
        if user:
            headers = {'user-agent': UserAgent}#}
            response = requests.get(self.url, headers=headers, proxies = user['proxy_dict'], timeout = 5)
        else:
            headers = {'user-agent': UserAgent}#}
            response = requests.get(self.url, headers=headers, timeout = 5)

        return response
    
    def __get_headers_proxy(self) -> dict:
        http_proxy  = "http://10.10.1.10:3128"
        https_proxy = "https://10.10.1.11:1080"
        ftp_proxy   = "ftp://10.10.1.10:3128"

        proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

    def download_file(self, directory_path: str, file_name: str) -> None:
        file_bytes = self.get_html().content

        if not os.path.isdir(directory_path):
            os.mkdir(directory_path)

        with open(f'{directory_path}/{file_name}', 'wb') as f:
            f.write(file_bytes)