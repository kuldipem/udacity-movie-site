import webbrowser


class Movie():
    """
    This class represent Movie entity in the real world
    To create object of this class you need to pass 4 basic details
    about a movie.
    """

    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """
        This will open browser window to show the movie trailer
        """
        webbrowser.open(self.trailer_youtube_url)
