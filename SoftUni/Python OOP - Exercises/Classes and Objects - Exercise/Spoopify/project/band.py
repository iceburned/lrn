from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for obj in self.albums:
            if obj.name == album_name:
                if obj.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(obj)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        band_name = f"Band {self.name}"
        albums_count = [_.details() for _ in self.albums]
        return band_name + "\n" + ''.join(albums_count)
