import dropbox
import airtable

RESOURCE_LOCATIONS = 'Resource Locations'

class Database:

    def __init__(self, base, key):
        self.base = base
        self.key = key

    def sources(self):
        table = airtable.Airtable(self.base, RESOURCE_LOCATIONS, self.key)
        for row in table.get_all():
            yield Source(
                name=row['fields'].get('Name'),
                url=row['fields'].get('URL')
            )

class Source:

    def __init__(self, name, url):
        self.name = name
        self.url = url

