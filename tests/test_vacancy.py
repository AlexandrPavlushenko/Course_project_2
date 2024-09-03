import unittest
from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def test_initialization(self):
        """Проверяет корректность создания объекта Vacancy."""
        vacancy = Vacancy(
            title="Разработчик Python",
            area="Москва",
            url="http://example.com/vacancy/1",
            salary_from="0",
            salary_to="120000",
            description="Заниматься разработкой на Python."
        )

        self.assertEqual(vacancy.title, "Разработчик Python")
        self.assertEqual(vacancy.area, "Москва")
        self.assertEqual(vacancy.url, "http://example.com/vacancy/1")
        self.assertEqual(vacancy.salary_from, "0")
        self.assertEqual(vacancy.salary_to, "120000")
        self.assertEqual(vacancy.description, "Заниматься разработкой на Python.")

    def test_str_method(self):
        """Проверяет работу метода __str__."""
        vacancy = Vacancy(
            title="Разработчик Python",
            area="Москва",
            url="http://example.com/vacancy/1",
            salary_from="0",
            salary_to="120000",
            description="Заниматься разработкой на Python."
        )

        expected_str = "Разработчик Python, Москва, Зарплата: от 0 до 120000, Ссылка: http://example.com/vacancy/1"
        self.assertEqual(str(vacancy), expected_str)

    def test_lt_method(self):
        """Проверяет правильность работы оператора <."""
        vacancy_1 = Vacancy(title="Junior", area="Москва", url="url_1", salary_from="0", salary_to="60000",
                            description="")
        vacancy_2 = Vacancy(title="Senior", area="Москва", url="url_2", salary_from="0", salary_to="120000",
                            description="")

        self.assertTrue(vacancy_1 < vacancy_2)
        self.assertFalse(vacancy_2 < vacancy_1)

    def test_validate_method(self):
        """Проверяет метод валидации."""
        valid_vacancy = Vacancy("Разработчик", "Санкт-Петербург", "http://example.com/vacancy/2",
                                "90000", "120000",
                                "Описание")
        self.assertIsNone(valid_vacancy.validate())

        invalid_vacancy_1 = Vacancy("", "Санкт-Петербург", "http://example.com/vacancy/2",
                                    "90000", "12000", "Описание")
        with self.assertRaises(ValueError) as context:
            invalid_vacancy_1.validate()
        self.assertEqual(str(context.exception), "Название и ссылка на вакансию обязательны.")

        invalid_vacancy_3 = Vacancy("Разработчик", "Санкт-Петербург", "",
                                    "90000", "12000", "Описание")
        with self.assertRaises(ValueError) as context:
            invalid_vacancy_3.validate()
        self.assertEqual(str(context.exception), "Название и ссылка на вакансию обязательны.")
