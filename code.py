import pygame
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        mixer.init()

    def play_song(self, song_path):
        mixer.music.load(song_path)
        mixer.music.play()

    def stop_song(self):
        mixer.music.stop()

    def pause_song(self):
        mixer.music.pause()

    def unpause_song(self):
        mixer.music.unpause()

if __name__ == "__main__":
    player = MusicPlayer()
    player.play_song('path_to_your_song.mp3')
