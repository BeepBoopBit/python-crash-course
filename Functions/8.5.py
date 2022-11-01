from pydoc import describe


def describe_city(name, country = "Philippines"):
    print(name + " is in " + country)

describe_city("Manila")
describe_city("Cebu")
describe_city("Tokyo", "Japan")