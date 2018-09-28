class TolokaSearchResult:
    __slots__ = ['id', 'link', 'title', 'forum_name', 'forum_parent',
                 'comments', 'size', 'seeders', 'leechers', 'complete']

    def __init__(self, id, link, title, forum_name, forum_parent, comments, size, seeders, leechers, complete):
        self.id = id
        self.link = link
        self.title = title
        self.forum_name = forum_name
        self.forum_parent = forum_parent
        self.comments = comments
        self.size = size
        self.seeders = seeders
        self.leechers = leechers
        self.complete = complete

    def to_json(self):
        to_serialize = ['id', 'link', 'title', 'forum_name', 'forum_parent',
                        'comments', 'size', 'seeders', 'leechers', 'complete']
        d = {}
        for attr in to_serialize:
            d[attr] = getattr(self, attr)

        return d

    @classmethod
    def from_json(cls, d: dict) -> 'TolokaSearchResult':
        return cls(**d)
