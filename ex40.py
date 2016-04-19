import time

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    def PlaySong(self):
        for verse in self.lyrics:
            print verse
            time.sleep(2)

song_lyrics = ("Let go and beg for freedom",
                "Another row jumping into the flame",
                "Loose lips are shifting leaders",
                "From here on out everyone is to blame",)
bulls_lyrics = ("I'm looking up to my company",
                "A full blown artillery",
                "Keep the sights on the enemy",
                "And bust the lid off anarchy)")

happy_bday = Song(song_lyrics)

bulls_on_parade = Song(bulls_lyrics)


happy_bday.PlaySong()
