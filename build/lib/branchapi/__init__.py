# __init__.py

# built-in package
from importlib import resources
from configparser import ConfigParser

# branchapi modules
from branchapi._version import __version__

# Read URL from config file
_cfg = ConfigParser()

with resources.path('branchapi', 'config.cfg') as _path:
    _cfg.read(str(_path))

URL = _cfg.get('api', 'url')
APP_ID = _cfg.get('params', 'app_id')
ACCESS_TOKEN = _cfg.get('secretKey', 'access_token')


