import urllib3
from bs4 import BeautifulSoup


def get_html(url):
    resp = urllib3.request("GET", url)
    if resp.status != 200:
        print(resp.status)
        print("Incorrect website connection.")
        return None
    return resp.data


def find_meta(html):
    soup = BeautifulSoup(html, "html.parser")
    meta_tags = soup.find_all('meta')
    meta_dict = {}
    for single_meta in meta_tags:
        property_atr = single_meta.get("property", single_meta.get("name", ""))
        property_content = single_meta.get("content", "")
        if property_atr[:3] == "og:":
            meta_dict[property_atr[3:]] = property_content

    return meta_dict
