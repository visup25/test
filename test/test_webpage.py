from bs4 import BeautifulSoup
import pytest
import pickle
import requests

class TestWebpage:
    @pytest.fixture(autouse=True)
    def get_soup(self):
        index_page = requests.get("http://localhost:8000/index.html")
        soup_index = BeautifulSoup(index_page.content, 'html.parser')
        self._index = soup_index
        
    # testing index.html
    def test_indexpage(self):
        assert self._index.find_all('header')
        site4= self._index.header.string=='WELCOME TO MY PAGE'
      