# utils.py

# built-in package
import json
import random
import string

from urllib.parse import urlparse
from urllib.parse import uses_relative, uses_netloc, uses_params

_VALID_URLS = set(uses_relative + uses_netloc + uses_params)

def is_valid_url(url: str) -> bool:
    """Check to see if a URL has a valid protocol.
    Parameters
    ----------
    url: str or unicode
    Returns
    -------
    is_valid_url: bool
        If url has a valid protocol return True otherwise False.
    """

    try:
        return urlparse(url).scheme in _VALID_URLS
    except Exception:
        return False

def read_json_data(json_file_path:str) -> dict:
    """
    Read the json file
    """
    
    try:
	    with open(json_file_path, 'r') as f:
		    json_data = json.load(f)
    except Exception:
        json_data = {}
    finally:
	    return json_data

def random_string(length:int) -> str:
    """Generate Random String
    Parameter
    ---------
    length: int
        Length of random string
    
    Return
    ------
    random_val: str
        Random alpha-numeric string
    """

    random_val = ""
    while length:
        random_val += random.choice(
            string.digits + string.ascii_lowercase + string.ascii_uppercase
        )
        length -= 1
    return random_val