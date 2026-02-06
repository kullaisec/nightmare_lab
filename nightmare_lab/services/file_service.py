import os

def read_file(path):
    base = "/var/data/"
    full = os.path.join(base, path)
    return open(full).read()