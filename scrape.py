#import the library used to query a website
import requests
import re
from bs4 import BeautifulSoup
import json
#specify the url
# webpage = "http://127.0.0.1:8000/insta/"
#Query the website and return the html to the variable 'page'
#Parse the html in the 'page' variable, and store it in Beautiful Soup

# page = requests.get(webpage)

from socket import error as socket_error
from lxml import html
import requests
from requests.exceptions import ConnectionError, HTTPError
import json
import logging

SCRIPT_JSON_PREFIX = 18
SCRIPT_JSON_DATA_INDEX = 21


def instagram_scrap_profile(username):
    """
    Scrap an instagram profile page
    :param username:
    :return:
    """
    try:
        url = "https://www.instagram.com/{}/".format(username)
        page = requests.get(url)
        # Raise error for 404 cause by a bad profile name
        page.raise_for_status()
        return html.fromstring(page.content)
    except HTTPError:
        logging.exception('user profile "{}" not found'.format(username))
    except (ConnectionError, socket_error) as e:
        logging.exception("instagram.com unreachable")


def instagram_profile_js(username):
    """
    Retrieve the script tags from the parsed page.
    :param username:
    :return:
    """
    try:
        tree = instagram_scrap_profile(username)
        return tree.xpath('//script')
    except AttributeError:
        logging.exception("scripts not found")
        return None


def instagram_profile_json(username):
    """
    Get the JSON data string from the scripts.
    :param username:
    :return:
    """
    scripts = instagram_profile_js(username)
    source = None

    if scripts:
        for script in scripts:
            if script.text:
                if script.text[0:SCRIPT_JSON_PREFIX] == "window._sharedData":
                    source = script.text[SCRIPT_JSON_DATA_INDEX:-1]

    return source


def instagram_profile_obj(username):
    """
    Retrieve the JSON from the page and parse it to a python dict.
    :param username:
    :return:
    """
    json_data = instagram_profile_json(username)
    return json.loads(json_data) if json_data else None


def scrape_data(username): 
# soup = BeautifulSoup(instagram_profile_obj('oneplus').read(), "lxml")
# print (soup.prettify())
# s = soup.get_text()
    s = json.dumps(instagram_profile_obj(username))
    hash_array = re.findall("#(\w+)", s)
    final_hash_list = list(set(hash_array))
    print(final_hash_list)
    return final_hash_list



