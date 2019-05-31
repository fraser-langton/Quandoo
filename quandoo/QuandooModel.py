import json
from datetime import datetime


class PrettyClass:
    useless_attrs = ["api_response", "agent"]

    def __str__(self):
        useful_attrs = ["{}: {}".format(key, val) for key, val in self.__dict__.items() if
                        key not in self.useless_attrs]

        return "{}(\n\t{}\n)".format(
            self.__class__.__name__,
            ",\n\t".join(useful_attrs)
        )

    def __repr__(self):
        return "\n" + indent(str(self))

    def to_tuple(self):
        return tuple([val for key, val in self.__dict__.items() if key not in self.useless_attrs])


class QuandooModel(PrettyClass):

    def __init__(self, data):
        self.api_response = data

    def get_api_response(self):
        return json.dumps(self.api_response, indent=2)


def get_datetime(data):
    return datetime.strptime(data, "%Y-%m-%dT%H:%M:%S%z")


def get_q_datetime(data):
    return datetime.strftime(data, "%Y-%m-%dT%H:%M:%S%z") + "+10:00"


def urljoin(*argv):
    return "/".join([str(arg) for arg in argv])


def indent(string, indent_amount=1):
    return "\n".join(["\t" * indent_amount + line for line in string.split("\n")])


