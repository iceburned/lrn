from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__mtx_photos(self.pages)

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for s in range(len(self.photos)):
            if len(self.photos[s]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[s].append(label)
                return f"{label} photo added successfully on page {s + 1} " \
                       f"slot {len(self.photos[s])}"
        return "No more free slots"

    def display(self):
        asd = "-----------\n"
        for i in self.photos:
            asd = asd + ' '.join(['[]' for _ in i])
            asd = asd + "\n"
            asd = asd + "-----------\n"
        return asd.strip()

    def __mtx_photos(self, pages):
        return [[] for _ in range(pages)]


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
d = 3