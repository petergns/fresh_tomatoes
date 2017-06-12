import webbrowser


class Movie:
    # Initializes:
    # the title, storyline, image, youtube trailer, movie duration,
    # and movie rating
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_duration, movie_rating):
        self.title = movie_title
        # Defines CSS styles & titles style for movies
        # Defines the span class
        a_css = '<span class="'
        b_css = '">'
        end_css = '</span>'
        # Defines CSS style & title for Movie Description
        desc_class = 'title_description'
        desc_text = 'Description: '
        description_css = a_css + desc_class + b_css + desc_text
        title_description = description_css + end_css
        self.storyline = title_description + movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # Defines CSS style & title for Movie Duration
        dur_class = 'title_duration'
        dur_text = 'Duration: '
        dur_css = a_css + dur_class + b_css + dur_text
        title_duration = dur_css + end_css
        self.duration = title_duration + movie_duration
        # Defines CSS style & title for Movie Rating
        rate_class = 'title_rating'
        rate_text = ' Rating: '
        title_css = a_css + rate_class + b_css + rate_text
        title_rating = title_css + end_css
        self.rating = title_rating + movie_rating

    # Opens the movie trailer link to youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
