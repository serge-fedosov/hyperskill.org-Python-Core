def tracklist(**artists):
    for artist in artists:
        print(artist)
        for album, song in artists[artist].items():
            print(f"ALBUM: {album} TRACK: {song}")
