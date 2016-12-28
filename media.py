# -*- coding: utf-8 -*-

import json
import webbrowser
from urllib import urlopen

class Movie(object):
    """
    Movie class contains information such as movie title, storyline,
    poster image url and trailer youtube url.
    """
    OMDB_URL = "http://www.omdbapi.com/?t=%s&y=&plot=short&r=json"

    def __init__(self, movie_title, trailer_youtube):
        self.title = movie_title
        self.omdb_info = self._get_omdb_info(movie_title)
        self.storyline, self.poster_image_url = self._parse_omdb_info()
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def _get_omdb_info(self, movie_title):
        omdb_info_json = urlopen(Movie.OMDB_URL % movie_title)
        return json.load(omdb_info_json)

    def _parse_omdb_info(self):
        return self.omdb_info.get("Plot"), self.omdb_info.get("Poster")

    def __str__(self):
        return "Movie %s" % (self.title)
