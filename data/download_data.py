"""Script to download data files from the BitBucket repository"""
from __future__ import absolute_import, division, print_function, unicode_literals


import sys
import os.path
import zipfile
try:
    import wget
except ImportError as e:
    print("> missing wget, trying to install it: %s" % e)
    try:
        import pip
        pip.main(['install', 'wget'])
        import wget
    except Exception as e:
        print("  - unable to install wget: %s" % e)
        sys.exit(1)

# list of archives to download
data_files = [
    'data.asvp.zip',
    'data.castaway.zip',
    'data.digibar.zip',
    'data.elac.zip',
    'data.idronaut.zip',
    'data.saiv.zip',
    'data.seabird.zip',
    'data.sippican.zip',
    'data.sonardyne.zip',
    'data.turo.zip',
    'data.unb.zip',
    'data.valeport.zip',
]

# actually downloading the file with wget
for fid in data_files:
    uri = 'https://bitbucket.org/ccomjhc/hyo_base/downloads/' + fid
    print("> downloading %s" % uri)
    if os.path.isfile(fid):
        print("  - already downloaded: skipping!")
    else:
        wget.download(uri, bar=wget.bar_thermometer)
        print("  - OK")

# actually unzipping the archives
downloaded_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), "downloaded")
if not os.path.exists(downloaded_folder):
    os.makedirs(downloaded_folder)
    print(downloaded_folder)
for fid in data_files:
    with zipfile.ZipFile(fid) as zf:
        zf.extractall(downloaded_folder)
    os.remove(fid)

print("--- DONE")
