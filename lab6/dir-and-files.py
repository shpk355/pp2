import os
def ex1(path):
    items = os.listdir(path)
    dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]