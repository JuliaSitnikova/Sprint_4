import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('genre',
                             [
                                 'Фантастика',
                                 'Ужасы',
                                 'Детективы',
                                 'Мультфильмы',
                                 'Комедии'
                             ]
                             )
    def test_get_genres_true(self, genre):
        books_genre = BooksCollector()
        assert genre in books_genre.genre


    def test_add_new_book(collector):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(collector):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        collector.set_book_genre('Крик', 'Ужасы')
        assert collector.get_book_genre('Крик') == 'Ужасы'

    def test_get_book_genre(collector):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        collector.set_book_genre('Крик', 'Ужасы')
        assert collector.get_book_genre('Крик') != 'Комедии'

    def test_get_books_with_specific_genre(collector):
        collector = BooksCollector()
        collector.add_new_book('Отель')
        collector.add_new_book('Аэропорт')
        collector.set_book_genre('Отель', 'Детективы')
        collector.set_book_genre('Аэропорт', 'Детективы')
        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_genre(collector):
        collector = BooksCollector()
        collector.add_new_book('Приключения Буратино')
        collector.set_book_genre('Приключения Буратино', 'Мультфильмы')
        assert collector.get_books_genre() == {'Приключения Буратино': 'Мультфильмы'}

    def test_get_books_for_children(collector):
        collector = BooksCollector()
        collector.add_new_book('Добро пожаловать')

        collector.set_book_genre('Добро пожаловать', 'Комедии')
        assert collector.get_books_for_children() == ['Добро пожаловать']

    def test_add_book_in_favorites(collector):
        collector = BooksCollector()
        collector.add_new_book('Отель')
        collector.add_book_in_favorites('Отель')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(collector):
        collector = BooksCollector()
        collector.add_new_book('Отель')
        collector.add_new_book('Аэропорт')
        collector.add_book_in_favorites('Отель')
        collector.add_book_in_favorites('Аэропорт')
        collector.delete_book_from_favorites('Отель')

        assert collector.get_list_of_favorites_books() == ['Аэропорт']

    def test_get_list_of_favorites_books(collector):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        collector.add_book_in_favorites('Крик')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert (favorites[0] == 'Крик')
