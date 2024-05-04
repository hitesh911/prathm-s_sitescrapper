from distutils.core import setup
import py2exe
setup(
    console=['main.py'],
    options={"py2exe": {
        "compressed": False,  # Compress the library archive
        "optimize": 2,  # Optimize bytecode slightly
        "dist_dir": "bigbite",  # Specify the output directory
    }},name="Scrapper",author="JUFFLER",fullname="Scrapping Master",version="0.1"
)


