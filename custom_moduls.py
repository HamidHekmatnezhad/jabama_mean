import requests
import re

class Jabama:
    def __init__(self):
        """define regex"""

        self.REGEX = r'<span class="text-md text-bold".*[\r\n]+([^\r\n]+)'

    def __del__(self):
        pass

    def __create_url(self, check_in, check_out, capacity=None):
        """create the url"""

        url_1 = 'https://www.jabama.com/city-ramsar?'
        # 1403-06-13 ye hamchin tarkibi bayad behesh ezafe beshe
        url_2 = 'checkIn=' + str(check_in)
        # 1403-06-15
        url_3 = '&checkOut=' + str(check_out)
        if capacity != None:
            url_4 = '&capacity=' + str(capacity)
        else:
            url_4 = ''
        # ye i ham behesh baraye search to page ha
        url_5 = '&page-number=' 

        url = url_1 + url_2 + url_3 + url_4 + url_5
        return url
    
    def get_data(self, check_in, check_out, capacity=None, PAGES=5):
        """get infos"""

        url = self.__create_url(check_in, check_out, capacity)
        i = 1
        prices = []

        while i <= PAGES:
            HTML = requests.get(url + str(i))
            
            data = re.findall(self.REGEX, HTML.text)

            for d in data:
                d = d.split()[0]
                d = d.replace(',', '')
                prices.append(int(d))
            
            i += 1

        return sum(prices) / len(prices),prices, url
