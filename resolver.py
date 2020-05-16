#!/usr/bin/env python3
import requests

def get_html(url):
    try:
        html = requests.get(url)
        return html.content
    except:
        print("Invalid Url")
