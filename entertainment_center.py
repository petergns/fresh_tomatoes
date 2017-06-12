import fresh_tomatoes
import media

# Movie Entries:
# (movie_title, description, movie_storyline,
# poster_image, trailer_youtube, movie_duration,
# movie_rating)

# Sound of Music movie:
sound_of_music = media.Movie(
    "The Sound of Music",
    "A nun in Austria finds a new home",
    "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",   # NOQA
    "https://www.youtube.com/watch?v=UY6uw3WpPzY",
    "174 minutes",
    "G"
    )
# Mr Beans Holiday movie:
mr_beans_holiday = media.Movie(
    "Mr. Bean's Holiday",
    "Mr Bean has an adventure in France",
    "https://upload.wikimedia.org/wikipedia/en/8/87/Mr_beans_holiday_ver7.jpg",  # NOQA
    "https://www.youtube.com/watch?v=dW1BIid8Osg",
    "85 minutes",
    "PG-13"
    )
# Wonder Woman movie:
wonder_woman = media.Movie(
    "Wonder Woman",
    "Story of the rise of a super heroine, "
    "and her fight to save the world",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=INLzqh7rZ-U",
    "141 minutes",
    "PG-13"
    )
# Guardians Galaxy Vol 2 movie:
guardians_galaxy_vol_2 = media.Movie(
    "Guardians of the Galaxy Vol. 2",
    "A group of heroes save the galaxy once again, "
    "and one finds his true origins",
    "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=dW1BIid8Osg",
    "136 minutes",
    "PG-13"
    )
# Life of Brian movie:
life_of_brian = media.Movie(
    "Monty Python's Life Of Brian",
    "A young Jewish man is mistaken as the messiah",
    "https://upload.wikimedia.org/wikipedia/en/1/18/Lifeofbrianfilmposter.jpg",  # NOQA
    "https://www.youtube.com/watch?v=HxIlg4m5fns",
    "93 minutes",
    "PG-13"
    )
# Chocolat movie:
chocolat = media.Movie(
    "Chocolat",
    "A romantic comedy set in a small french town",
    "https://upload.wikimedia.org/wikipedia/en/0/08/Chocolat_sheet.jpg",  # NOQA
    "https://www.youtube.com/watch?v=692hOJq1KJE",
    "121 minutes",
    "PG-13"
    )
# Into Darkness movie:
into_darkness = media.Movie(
    "Star Trek Into Darkness",
    "A captain in a sci-fi future must search"
    " for a fugitive",
    "https://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=QAEkuVgt6Aw",
    "133 minutes",
    "PG-13"
    )

# Movies to show on page
movies = [
    sound_of_music,
    mr_beans_holiday,
    wonder_woman,
    guardians_galaxy_vol_2,
    life_of_brian,
    chocolat,
    into_darkness
    ]
# Opens movie page
fresh_tomatoes.open_movies_page(movies)
