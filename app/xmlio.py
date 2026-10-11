import defusedxml.ElementTree as ET


def parse(data):
    return ET.fromstring(data)
