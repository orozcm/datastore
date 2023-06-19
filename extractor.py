"""
Extract data from CSV into raw storage
"""
import os
import gzip
from config import DATA_SOURCE_FOLDER, ROOT_FOLDER
from transform import get_filename


def extract():
    for root, dirs, files in os.walk(os.path.join(ROOT_FOLDER, DATA_SOURCE_FOLDER)):
        for file in files:
            with gzip.open(os.path.join(root, file), 'rb') as gzf:
                _content = gzf.read().decode("utf-8")
                with open(os.path.join(ROOT_FOLDER, "csv", get_filename(file)), 'w') as f:
                    f.write(_content)
                    print(f"Extracted {file}")


if __name__ == "__main__":
    extract()
