#!/usr/bin/env python
# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

# initialize movies
kung_fu_panda = media.Movie(
    'Kung Fu Panda',
    'https://www.youtube.com/watch?v=PXi3Mv6KMzY',
)

dr_strange = media.Movie(
    'Doctor Strange',
    'https://www.youtube.com/watch?v=HSzx-zryEgM',
)

forrest_gump = media.Movie(
    'Forrest Gump',
    'https://www.youtube.com/watch?v=uPIEn0M8su0',
)

if __name__ == "__main__":
    movies = [kung_fu_panda, dr_strange, forrest_gump]

    # serve static HTML page
    fresh_tomatoes.open_movies_page(movies)
