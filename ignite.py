import pkgutil
import os

if pkgutil.find_loader("langchain") is None:
    os.system("pip install langchain")

if pkgutil.find_loader("ctransformers") is None:
    os.system("pip install ctransformers")

if pkgutil.find_loader("openfabric_pysdk") is None:
    os.system("pip install openfabric_pysdk")

from openfabric_pysdk.starter import Starter


if __name__ == '__main__':
    Starter.ignite(debug=False, host="0.0.0.0", port=5500),
