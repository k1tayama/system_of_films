from typing import List, Dict, Optional
from abc import ABC, abstractmethod
from enum import Enum
from collections import defaultdict
import statistics
from dataclasses import dataclass

class Genres(Enum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    COMEDY = "Comedy"
    SCI_FI = "Sci-Fi"
    DRAMA = "Drama"
    HORROR = "Horror"
    THRILLER = "Thriller"
    FANTASY = "Fantasy"
    ROMANCE = "Romance"
    MYSTERY = "Mystery"
    ANIMATION = "Animation"
    FAMILY = "Family"
    CRIME = "Crime"
    BIOGRAPHY = "Biography"
    HISTORY = "History"
    MUSICAL = "Musical"
    WESTERN = "Western"
    DOCUMENTARY = "Documentary"

class Film:
    def __init__(self, movie_id: int, title: str, genres: List[Genres], director: str, year: int, rating: float):
        self._id = movie_id
        self._title = title
        self._genres = genres
        self._director = director
        self._year = year
        self._rating = rating

    def __str__(self):
        return f"{self._title} ({self._year}) - рейтинг: {self._rating}"
    @property
    def movie_id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def genres(self):
        return self._genres

    @property
    def director(self):
        return self._director

    @property
    def year(self):
        return self._year

    @property
    def rating(self):
        return self._rating

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Поле не может быть пустым")
        value = value.strip()
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        self._title = value

    @genres.setter
    def genres(self, value):
        if not isinstance(value, list):
            raise TypeError("genres должен быть списком")
        if not all(isinstance(g, Genres) for g in value):
            raise TypeError("Каждый элемент genres должен быть элементом перечисления Genres")
        if not value:
            raise ValueError("Поле не может быть пустым")
        self._genres = value

    @director.setter
    def director(self, value):
        if not value:
            raise ValueError("Поле не может быть пустым")
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        self._director = value

    @year.setter
    def year(self, value):
        if not value:
            raise ValueError("Поле не может быть пустым")
        if not (1800 <= value <= 2100):
            raise ValueError("Год фильма должен быть в диапазоне 1800–2100")
        self._year = value

    @rating.setter
    def rating(self, value):
        if not (0 <= value <= 10):
            raise ValueError("Рейтинг должен быть от 0 до 10")
        self._rating = float(value)

class User:
    def __init__(self, user_id, user_name, watched_films=None, preferred_genres=None):
        self._id = user_id
        self._name = user_name
        if watched_films:
            self._watched_films = watched_films
        else:
            self._watched_films = {}
        if preferred_genres:
            self._preferred_genres = preferred_genres
        else:
            self._preferred_genres = []

    @property
    def user_id(self):
        return self._id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, int):
            raise TypeError("user_id должен быть числом")
        if value <= 0:
            raise ValueError("user_id должен быть положительным")
        self._id = value

    @property
    def user_name(self):
        return self._name

    @user_name.setter
    def user_name(self, value):
        if not isinstance(value, str):
            raise TypeError("user_name должен быть строкой")
        value = value.strip()
        if not value:
            raise ValueError("user_name не может быть пустым")
        self._name = value

    @property
    def watched_films(self):
        return self._watched_films

    @watched_films.setter
    def watched_films(self, value):
        if not isinstance(value, dict):
            raise TypeError("watched_films должен быть словарём")
        self._watched_films = value

    @property
    def preferred_genres(self):
        return self._preferred_genres

    @preferred_genres.setter
    def preferred_genres(self, value):
        if not isinstance(value, list):
            raise TypeError("preferred_genres должен быть списком")
        self._preferred_genres = value

    def add_watched_film(self, film: Film, rating: float):
        self._watched_films[film] = rating

    def get_rating(self, film: Film):
        return self._watched_films.get(film, None)




class DataManager:
    def __init__(self):
        self._films = {}
        self._users = {}

    def add_film(self, film: Film):
        if film._id in self._films:
            print(f"Фильм с ID {film._id} уже существует.")
        else:
            self._films[film._id] = film

    def add_user(self, user: User):
        if user._id in self._users:
            print(f"Пользователь с ID {user._id} уже существует")
        else:
            self._users[user._id] = user

    def load_sample_data(self):
        sample_films = [
            Film(1, "Inception", [Genres.ACTION, Genres.THRILLER], "Nolan", 2010, 8.8),
            Film(2, "Titanic", [Genres.DRAMA, Genres.ROMANCE], "Cameron", 1997, 7.8),
            Film(3, "The Lion King", [Genres.ANIMATION, Genres.FAMILY], "Allers", 1994, 8.5),
            Film(4, "Avengers: Endgame", [Genres.ACTION, Genres.ADVENTURE], "Russo", 2019, 8.4),
            Film(5, "Joker", [Genres.DRAMA, Genres.CRIME], "Phillips", 2019, 8.5),
            Film(6, "Frozen", [Genres.ANIMATION, Genres.FAMILY], "Buck", 2013, 7.5),
            Film(7, "Pulp Fiction", [Genres.CRIME, Genres.DRAMA], "Tarantino", 1994, 8.9),
            Film(8, "The Godfather", [Genres.CRIME, Genres.DRAMA], "Coppola", 1972, 9.2),
            Film(9, "The Dark Knight", [Genres.ACTION, Genres.THRILLER], "Nolan", 2008, 9.0),
            Film(10, "Forrest Gump", [Genres.DRAMA, Genres.ROMANCE], "Zemeckis", 1994, 8.8),
            Film(11, "The Matrix", [Genres.ACTION], "Wachowski", 1999, 8.7),
            Film(12, "Gladiator", [Genres.ACTION, Genres.DRAMA], "Scott", 2000, 8.5),
            Film(13, "La La Land", [Genres.DRAMA, Genres.MUSICAL], "Chazelle", 2016, 8.0),
            Film(14, "The Shawshank Redemption", [Genres.DRAMA, Genres.CRIME], "Darabont", 1994, 9.3),
            Film(15, "The Avengers", [Genres.ACTION, Genres.ADVENTURE], "Whedon", 2012, 8.0),
            Film(16, "Interstellar", [Genres.ADVENTURE, Genres.SCI_FI], "Nolan", 2014, 8.6),
            Film(17, "Parasite", [Genres.THRILLER, Genres.DRAMA], "Bong", 2019, 8.6),
            Film(18, "Spirited Away", [Genres.ANIMATION, Genres.FANTASY], "Miyazaki", 2001, 8.6),
            Film(19, "The Wolf of Wall Street", [Genres.COMEDY, Genres.DRAMA], "Scorsese", 2013, 8.2),
            Film(20, "Mad Max: Fury Road", [Genres.ACTION, Genres.ADVENTURE], "Miller", 2015, 8.1),
            Film(21, "Avatar", [Genres.ACTION, Genres.ADVENTURE, Genres.FANTASY], "Cameron", 2009, 7.8),
            Film(22, "The Social Network", [Genres.DRAMA, Genres.BIOGRAPHY], "Fincher", 2010, 7.7),
            Film(23, "Guardians of the Galaxy", [Genres.ACTION, Genres.ADVENTURE, Genres.COMEDY], "Gunn", 2014, 8.0),
            Film(24, "Coco", [Genres.ANIMATION, Genres.FAMILY, Genres.MUSICAL], "Unkrich", 2017, 8.4),
            Film(25, "Jumanji: Welcome to the Jungle", [Genres.ADVENTURE, Genres.COMEDY], "Johnson", 2017, 6.9),
            Film(26, "Black Panther", [Genres.ACTION, Genres.ADVENTURE], "Coogler", 2018, 7.3),
            Film(27, "Toy Story 3", [Genres.ANIMATION, Genres.FAMILY], "Lasseter", 2010, 8.3),
            Film(28, "Deadpool", [Genres.ACTION, Genres.COMEDY], "Reynolds", 2016, 8.0),
            Film(29, "Shrek", [Genres.ANIMATION, Genres.COMEDY, Genres.FAMILY], "Adamson", 2001, 7.9),
            Film(30, "Fight Club", [Genres.DRAMA, Genres.THRILLER], "Fincher", 1999, 8.8),
        ]
        for f in sample_films:
         self.add_film(f)

        user1 = User(1, "Alice", preferred_genres=[Genres.ACTION, Genres.ADVENTURE])
        user2 = User(2, "Walter", preferred_genres=[Genres.DRAMA, Genres.ROMANCE])
        user3 = User(3, "Jimmy", preferred_genres=[Genres.ANIMATION, Genres.FAMILY])

        self.add_user(user1)
        self.add_user(user2)
        self.add_user(user3)

        user1.add_watched_film(sample_films[3], 8.5)
        user2.add_watched_film(sample_films[1], 7.8)
        user2.add_watched_film(sample_films[9], 8.8)
        user3.add_watched_film(sample_films[2], 8.5)
        user3.add_watched_film(sample_films[5], 7.5)

# 2  


class RecommendationStrategy(ABC):  
    def __init__(self, name: str):
        self._name = name  
        self._recommendation_count = 5  
    @property
    def name(self):
        return self._name  
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Название стратегии должно быть строкой")
        self._name = value 
    @property
    def recommendation_count(self):
        return self._recommendation_count
    @recommendation_count.setter
    def recommendation_count(self, value: int):
        if value < 1:
            raise ValueError("Количество рекомендаций должно быть положительным")
        self._recommendation_count = value 
    @abstractmethod
    def __call__(self, data_manager, user):
        pass 
    def __str__(self):
        return f"Стратегия: {self._name}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self._name}')"
    @abstractmethod
    def get_description(self):
        pass

@dataclass
class RecommendationResult:
    films: List['Film']
    strategy_name: str
    score: Optional[float] = None
    def __str__(self):
        titles = [f.title for f in self.films]
        return f"{self.strategy_name}: {', '.join(titles)}"
    def __len__(self):
        return len(self.films)

class GenreBasedStrategy(RecommendationStrategy):
    def __init__(self):
        super().__init__("По жанрам")
    def __call__(self, data_manager, user):
        preferred_genres = user.preferred_genres
        if not preferred_genres:
            return [] 
        matching_films = []
        for film in data_manager._films.values():
            if any(genre in preferred_genres for genre in film.genres):
                if film not in user.watched_films:
                    matching_films.append((film, len([g for g in film.genres if g in preferred_genres])))
        matching_films.sort(key=lambda x: (x[1], x[0].rating), reverse=True)
        return [film for film, _ in matching_films[:self.recommendation_count]]
    def get_description(self):
        return "Рекомендует фильмы любимых жанров пользователя"

class RatingBasedStrategy(RecommendationStrategy):
    def __init__(self):
        super().__init__("По популярности")
    def __call__(self, data_manager, user):
        unwatched_films = [
            film for film in data_manager._films.values() 
            if film not in user.watched_films
        ]
        unwatched_films.sort(key=lambda f: f.rating, reverse=True)
        return unwatched_films[:self.recommendation_count]
    def get_description(self):
        return "Рекомендует самые популярные непросмотренные фильмы"

class SimilarUsersStrategy(RecommendationStrategy):  
    def __init__(self):
        super().__init__("Похожие пользователи")
    def _calculate_similarity(self, user1: 'User', user2: 'User'):
        common_films = set(user1.watched_films.keys()) & set(user2.watched_films.keys())
        if not common_films:
            return 0.0  
        ratings_diff = [
            abs(user1.get_rating(film) or 0 - (user2.get_rating(film) or 0))
            for film in common_films
        ]
        return 1.0 / (1.0 + statistics.mean(ratings_diff))
    def __call__(self, data_manager, user):
        all_users = [u for u in data_manager._users.values() if u.user_id != user.user_id]
        if not all_users:
            return []
        similarities = [(other_user, self._calculate_similarity(user, other_user)) 
                       for other_user in all_users if self._calculate_similarity(user, other_user) > 0]
        if not similarities:
            return []
        similarities.sort(key=lambda x: x[1], reverse=True)
        most_similar_user, similarity_score = similarities[0]
        recommendations = [
            film for film, rating in most_similar_user.watched_films.items()
            if film not in user.watched_films and rating >= 8.0
        ]
        recommendations.sort(key=lambda f: most_similar_user.get_rating(f) or 0, reverse=True)
        return recommendations[:self.recommendation_count]
    def get_description(self):
        return "Рекомендует фильмы, которые понравились похожим пользователям"

class RecommendationService:
    def __init__(self):
        self._strategies: Dict[str, RecommendationStrategy] = {}
        self._register_strategies()
    def _register_strategies(self):
        self._strategies["genre"] = GenreBasedStrategy()
        self._strategies["rating"] = RatingBasedStrategy()
        self._strategies["similar"] = SimilarUsersStrategy()
    @property
    def available_strategies(self):
        return list(self._strategies.keys())
    def create_recommendation(self, strategy_name: str, data_manager, user):
        if strategy_name not in self._strategies:
            raise ValueError(f"Стратегия '{strategy_name}' не найдена. Доступны: {self.available_strategies}") 
        strategy = self._strategies[strategy_name]
        films = strategy(data_manager, user)
        return RecommendationResult(films, strategy.name)
    def get_all_recommendations(self, data_manager, user):
        return {
            name: self.create_recommendation(name, data_manager, user)
            for name in self.available_strategies
        }
    def __getitem__(self, strategy_name: str):
        return self._strategies[strategy_name]  
    def __str__(self):
        strategies = "\n".join([f"  - {s}" for s in self.available_strategies])
        return f"Сервис по рекомендациям со стратегиями:\n{strategies}"

# test
# dm = DataManager()
# dm.load_sample_data()

# service = RecommendationService()
# print(service)

# user1 = dm._users[1]

# print("\nРекомендации для User1:")
# genre_recs = service.create_recommendation("genre", dm, user1)
# print(f"1) {genre_recs}") 
# print(f"   Количество фильмов: {len(genre_recs)}")

# rating_recs = service.create_recommendation("rating", dm, user1)
# print(f"2) {rating_recs}")
# print(f"   Количество фильмов: {len(genre_recs)}")

# similar_recs = service.create_recommendation("similar", dm, user1)
# print(f"3) {similar_recs}")
# print(f"   Количество фильмов: {len(genre_recs)}")

# print(f"\nПрямая стратегия: {service['genre']}")
# print(repr(service['genre']))
