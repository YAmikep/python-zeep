from collections import OrderedDict

from lxml import etree

from zeep.xsd.valueobjects import CompoundValue


def serialize_object(obj, dict_type=OrderedDict):
    """Serialize zeep objects to native python data structures"""
    if obj is None:
        return obj

    if isinstance(obj, etree._Element):
        return obj

    if isinstance(obj, list):
        return [serialize_object(sub) for sub in obj]

    if isinstance(obj, dict):
        result = dict_type()
        for key in obj:
            value = obj[key]
            if isinstance(value, (list, CompoundValue)):
                value = serialize_object(value)
            result[key] = value
        return result
        
    return obj
