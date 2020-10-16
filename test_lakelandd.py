import os
import dotenv

from lakelandd.database import Database, Source
from lakelandd.storage import Folder

dotenv.load_dotenv()

AIRTABLE_BASE = os.environ.get('AIRTABLE_BASE')
AIRTABLE_KEY = os.environ.get('AIRTABLE_KEY')

DROPBOX_FOLDER = os.environ.get('DROPBOX_FOLDER')
DROPBOX_KEY = os.environ.get('DROPBOX_KEY')

def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_sources():
    db = Database(AIRTABLE_BASE, AIRTABLE_KEY)
    for source in db.sources():
        assert type(source) == Source
        assert source.name

def test_storage():
    s = Folder(DROPBOX_FOLDER, DROPBOX_KEY)
    assert len(s) > 0

