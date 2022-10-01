"""Дополнительный модуль: вспомогательные функции."""

# импорт из стандартной библиотеки
from pathlib import Path
from sys import path
from shutil import get_terminal_size as gts
from math import ceil, floor
from configparser import ConfigParser
from itertools import zip_longest
from pprint import pprint


# импорт дополнительных модулей
import data