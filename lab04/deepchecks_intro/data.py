import os
import urllib.request
import zipfile

url = "https://download.pytorch.org/tutorial/hymenoptera_data.zip"
urllib.request.urlretrieve(url, "./hymenoptera_data.zip")

with zipfile.ZipFile("./hymenoptera_data.zip", "r") as zip_ref:
    zip_ref.extractall(".")
