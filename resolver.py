#!/usr/bin/env python3
import requests

def get_html(url):
    html = requests.get(url)
    print(html.content)
