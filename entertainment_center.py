#!/usr/bin/env python
# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

kung_fu_panda = media.Movie(
    'Kung Fu Panda',
    'The Dragon Warrior has to clash against the savage Tai Lung as China\'s'
    ' fate hangs in the balance: However, the Dragon Warrior mantle is'
    ' supposedly mistaken to be bestowed upon an obese panda who is a tyro in'
    ' martial arts.',
    'https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg',
    'https://www.youtube.com/watch?v=PXi3Mv6KMzY',
)

dr_strange = media.Movie(
    'Doctor Strange',
    'A former neurosurgeon embarks on a journey of healing only to be drawn'
    ' into the world of the mystic arts.',
    'https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg',
    'https://www.youtube.com/watch?v=HSzx-zryEgM',
)

forrest_gump = media.Movie(
    'Forrest Gump',
    'Forrest Gump, while not intelligent, has accidentally been present at many'
    ' historic moments, but his true love, Jenny Curran, eludes him.',
    'https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg',
    'https://www.youtube.com/watch?v=uPIEn0M8su0',
)

if __name__ == "__main__":
    movies = [kung_fu_panda, dr_strange, forrest_gump]

    fresh_tomatoes.open_movies_page(movies)
