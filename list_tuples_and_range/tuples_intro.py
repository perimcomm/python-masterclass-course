albums  =   [("Welcome to my nightmare", "Alice Cooper", 1975),
            ("Bad company", "bad company", 1974),
            ("nighflight", "bugdie", 1981),
            ("More mayhem", "emailda may", 2011),
            ("ride the lightning", "metallica", 1984)
            ]

print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))
