# coding:utf-8
from dateparser.date import DateDataParser
from w3lib.html import remove_tags
from itertools import chain

import re 
import six

_NUMERIC_ENTITIES = re.compile(r'&#([0-9]+)(?:;|\s)', re.U)
_PRICE_NUMBER_RE = re.compile(r'(?:^|[^a-zA-Z0-9])(\d+(?:\.\d+)?)'
                              r'(?:$|[^a-zA-Z0-9])')
_NUMBER_RE = re.compile(r'(-?\d+(?:\.\d+)?)')
_DECIMAL_RE = re.compile(r'(\d[\d\,]*(?:(?:\.\d+)|(?:)))', re.U | re.M)
_VALPARTS_RE = re.compile(r'([\.,]?\d+)')

class Text():
    def __call__(self, values):
        return [remove_tags(v).strip()
                if v and isinstance(v, six.string_types) else v
                for v in values]

class Date(Text):
    def __init__(self, format='%Y-%m-%dT%H:%M:%S'):
        self.format = format

    def __call__(self, values):
        values = super(Date, self).__call__(values)
        dates = []
        for text in values:
            if isinstance(text, (dict, list)):
                dates.append(text)
            try:
                date = DateDataParser().get_date_data(text)['date_obj']
                dates.append(date)
            except ValueError:
                pass
        return dates

class CleanText():
    def __call__(self, values):
        return [(lambda v: v.replace('\n', '').replace(' ', '').strip())(v) for v in values]

class Number():
    def __call__(self, values):
        numbers = []
        for value in values:
            if isinstance(value, (dict, list)):
                numbers.append(value)
            txt = _NUMERIC_ENTITIES.sub(lambda m: unichr(int(m.groups()[0])),value)
            numbers.append(_NUMBER_RE.findall(txt))
        return list(map(lambda v: float(v) , list(chain(*numbers))))

class Price():
    def __call__(self, values):
        prices = []
        for value in values:
            if isinstance(value, (dict, list)):
                prices.append(value)
            txt = _NUMERIC_ENTITIES.sub(lambda m: unichr(int(m.groups()[0])),value)
            m = _DECIMAL_RE.search(txt)
            if m:
                value = m.group(1)
                parts = _VALPARTS_RE.findall(value)
                decimalpart = parts.pop(-1)
                if decimalpart[0] == "," and len(decimalpart) <= 3:
                    decimalpart = decimalpart.replace(",", ".")
                value = "".join(parts + [decimalpart]).replace(",", "")
                prices.append(float(value))
        return prices