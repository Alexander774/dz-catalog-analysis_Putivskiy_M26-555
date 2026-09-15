import math as m


movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    """Computes average rating across movies."""
    ratings = [movie["rating"] for movie in movies]
    return round(sum(ratings) / 10)


def catalog_age_stats(movies, current_year=2026):
    """Finds the oldest and the newest movies; computes average age across movies."""
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = m.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    """Computes the duration in hours from duration in minutes."""
    hours = minutes // 60
    minutes_left = minutes % 60
    return f"{hours}ч {minutes_left}м"


def rating_tier(rating):
    """Reurns label for a given rating."""
    if rating >= 9.0:
        return "шедевр"
    elif rating >= 5.0:
        return "хорошо" if rating >= 7.0 else "средне"
    else:
        return "слабо"


def decade_label(year):
    """Returns label for a given year of production."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ :
            return "старые"


for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(movies[i]["title"])
        break
    i += 1
else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Counts movies longer than a certain threshold."""
    counter = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            counter += 1
    return counter


def normalize_title(title):
    """Normalizes title to Title Case."""
    title_words = title.split(" ")
    cap_title_words = list()

    for word in title_words:
        word = word[0].upper() + word[1:]
        cap_title_words.append(word)

    return " ".join(cap_title_words)


def make_slug(title):
    """Makes a slug from the title."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Formats a report line for a movie."""
    genres = ", ".join(movie["genres"])

    report_line = f'\"{movie["title"]}\" '
    report_line += f'({movie["year"]}) — '
    report_line += f'{movie["rating"]}/10, '
    report_line += f'{duration_in_hours(movie["duration_min"])}, '
    report_line += f'жанры: {genres}'

    return report_line


def titles_sorted_by_rating(movies):
    movies_sorted = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in movies_sorted]


def top_n_by_rating(movies, n=3):
    movies_sorted = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in movies_sorted[:n]]


def count_by_genre(movies):
    genre_counter = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counter[genre] = genre_counter.get(genre, 0) + 1

    return genre_counter


def actor_filmography(movies):
    actors_filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            actors_filmography[actor] = actors_filmography.get(actor, [])
            actors_filmography[actor].append(movie["title"])

    return actors_filmography


above_average = {movie["title"]: movie["rating"]
                 for movie in movies
                 if movie["rating"] > average_rating(movies)}
