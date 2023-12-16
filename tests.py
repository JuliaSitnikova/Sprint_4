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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        assert len(collector.get_books_raiting()) == 1

    def test_set_book_genre(collector):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        collector.set_book_genre('Крик', 'Ужасы')
        assert collector.get_book_genre('Крик') == 'Ужасы'

    def test_get_book_genre(collector):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        collector.set_book_genre('Крик', 'Ужасы')
        assert collector.get_book_genre('Крик') not in 'Комедии'

    def test_get_books_with_specific_genre(collector):
        collector = BooksCollector()
        collector.add_new_book('Отель')
        collector.add_new_book('Аэропорт')
        collector.add_new_book('Черновик')
        collector.set_book_genre('Отель', 'Детективы')
        collector.set_book_genre('Аэропорт', 'Детективы')
        collector.set_book_genre('Черновик', 'Фантастика')
        assert collector.get_books_with_specific_genre('Детективы') == ['Отель', 'Аэропорт']

    def test_get_books_genre(collector):
        collector = BooksCollector()
        collector.add_new_book('Приключения Буратино')
        collector.set_book_genre('Приключения Буратино', 'Мультфильмы')
        assert collector.get_books_genre() == {'Приключения Буратино': 'Мультфильмы'}

    def test_get_books_for_children(collector):
        collector = BooksCollector()
        collector.add_new_book('Черновик')
        collector.add_new_book('Добро пожаловать')
        collector.add_new_book('Анна Каренина')
        collector.set_book_genre('Черновик', 'Фантастика')
        collector.set_book_genre('Добро пожаловать', 'Комедии')
        collector.set_book_genre('Анна Каренина', 'Роман')
        assert collector.get_books_for_children() == ['Добро пожаловать']

    def test_add_book_in_favorites(collector, book, expected_favorites):
        collector = BooksCollector()
        collector.add_new_book('Отель')
        collector.add_new_book('Аэропорт')
        collector.set_book_genre('Отель', 'Детективы')
        collector.set_book_genre('Аэропорт', 'Детективы')
        collector.add_book_in_favorites(book)

        assert collector.get_list_of_favorites_books() == expected_favorites

    def test_delete_book_from_favorites(collector, book, expected_favorites):
        collector = BooksCollector()
        collector.add_new_book('Отель')
        collector.add_new_book('Аэропорт')
        collector.set_book_genre('Отель', 'Детективы')
        collector.set_book_genre('Аэропорт', 'Детективы')
        collector.add_book_in_favorites('Отель')
        collector.add_book_in_favorites('Аэропорт')
        collector.delete_book_from_favorites(book)

        assert collector.get_list_of_favorites_books() == expected_favorites

    def test_get_list_of_favorites_books(collector, book, expected_favorites):
        collector = BooksCollector()
        collector.add_new_book('Крик')
        collector.add_book_in_favorites('Крик')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert (favorites[0] == 'Крик')
