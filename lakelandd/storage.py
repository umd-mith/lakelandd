import dropbox


class Folder:

    def __init__(self, path, dropbox_key):
        self.path = path
        self.dropbox_key = dropbox_key
        self.dropbox = dropbox.Dropbox(dropbox_key)

    def __len__(self):
        count = 0
        for f in self.files():
            count += 1
        return count

    def files(self):
        finished = False
        results  = self.dropbox.files_list_folder(self.path, recursive=True)
        while not finished:
            for f in results.entries:
                # only return files, not folders
                if type(f) != dropbox.files.FolderMetadata:
                    yield File(path=f.path_display, size=f.size)
            if results.has_more:
                results = self.dropbox.files_list_folder_continue(results.cursor)
            else:
                finished = True


class File:

    def __init__(self, path, size):
        self.path = path
        self.size = size

    def __repr__(self):
        return self.path
