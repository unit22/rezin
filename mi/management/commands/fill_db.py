from django.core.management.base import BaseCommand
from mi.models import Category1, Category2, Category3, Item
from datetime import date


class Command(BaseCommand):
    help = 'Fill DB new data'
    def handle(self, *args, **options):
        categories1 = [
            {'name': 'Одежда для женщин'},
            {'name': 'Одежда для мужчин'},
            {'name': 'Все для детей'},
            {'name': 'Телефоны и планшеты'},
            {'name': 'Компьютерная техника'},
            {'name': 'Автотовары'},
            {'name': 'Бижутерия и часы'},
            {'name': 'Сумки и обувь'},
            {'name': 'Для дома и сада'},
            {'name': 'Электроника'},
            {'name': 'Красота и здоровье'},
            {'name': 'Спорт и развлечения'},
            {'name': 'Техника и инструменты'}
        ]
        categories2 = [
            {'cat1': 'Одежда для женщин', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Одежда для женщин', 'click': 0, 'name': 'Верх'},
            {'cat1': 'Одежда для женщин', 'click': 0, 'name': 'Низ'},
            {'cat1': 'Одежда для женщин', 'click': 0, 'name': 'Куртки и пальто'},
            {'cat1': 'Одежда для женщин', 'click': 0, 'name': 'Нижнее белье'},

            {'cat1': 'Одежда для мужчин', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Одежда для мужчин', 'click': 0, 'name': 'Верх'},
            {'cat1': 'Одежда для мужчин', 'click': 0, 'name': 'Низ'},
            {'cat1': 'Одежда для мужчин', 'click': 0, 'name': 'Одежда и аксессуары'},
            {'cat1': 'Одежда для мужчин', 'click': 0, 'name': 'Аксессуары'},

            {'cat1': 'Все для детей', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Все для детей', 'click': 0, 'name': 'Одежда для девочек'},
            {'cat1': 'Все для детей', 'click': 0, 'name': 'Одежда для мальчиков'},
            {'cat1': 'Все для детей', 'click': 0, 'name': 'Игрушки и хобби'},
            {'cat1': 'Все для детей', 'click': 0, 'name': 'Сумки и обувь'},

            {'cat1': 'Телефоны и планшеты', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Телефоны и планшеты', 'click': 0, 'name': 'Мобильные телефоны'},
            {'cat1': 'Телефоны и планшеты', 'click': 0, 'name': 'Планшеты'},
            {'cat1': 'Телефоны и планшеты', 'click': 0, 'name': 'Запчасти'},
            {'cat1': 'Телефоны и планшеты', 'click': 0, 'name': 'Сумки и чехлы'},
            {'cat1': 'Телефоны и планшеты', 'click': 0, 'name': 'Аксессуары'},

            {'cat1': 'Компьютерная техника', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Компьютерная техника', 'click': 0, 'name': 'Ноутбуки'},
            {'cat1': 'Компьютерная техника', 'click': 0, 'name': 'Офисная электроника'},
            {'cat1': 'Компьютерная техника', 'click': 0, 'name': 'Устройства хранения'},
            {'cat1': 'Компьютерная техника', 'click': 0, 'name': 'Сеть'},

            {'cat1': 'Автотовары', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Автотовары', 'click': 0, 'name': 'Автомобили'},
            {'cat1': 'Автотовары', 'click': 0, 'name': 'Электроника'},
            {'cat1': 'Автотовары', 'click': 0, 'name': 'Аксессуары'},
            {'cat1': 'Автотовары', 'click': 0, 'name': 'Инструменты'},

            {'cat1': 'Бижутерия и часы', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Бижутерия и часы', 'click': 0, 'name': 'Часы'},
            {'cat1': 'Бижутерия и часы', 'click': 0, 'name': 'Бижутерия'},
            {'cat1': 'Бижутерия и часы', 'click': 0, 'name': 'Ювелирные украшения'},

            {'cat1': 'Сумки и обувь', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Сумки и обувь', 'click': 0, 'name': 'Женские сумки'},
            {'cat1': 'Сумки и обувь', 'click': 0, 'name': 'Мужские сумки'},
            {'cat1': 'Сумки и обувь', 'click': 0, 'name': 'Женская обувь'},
            {'cat1': 'Сумки и обувь', 'click': 0, 'name': 'Мужская обувь'},
            {'cat1': 'Сумки и обувь', 'click': 0, 'name': 'Средства по уходу'},

            {'cat1': 'Для дома и сада', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Для дома и сада', 'click': 0, 'name': 'Домашний декор'},
            {'cat1': 'Для дома и сада', 'click': 0, 'name': 'Рукоделие и вышивка'},
            {'cat1': 'Для дома и сада', 'click': 0, 'name': 'Текстиль для дома'},
            {'cat1': 'Для дома и сада', 'click': 0, 'name': 'Освещение'},
            {'cat1': 'Для дома и сада', 'click': 0, 'name': 'Кухня, столовая, бар'},

            {'cat1': 'Электроника', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Электроника', 'click': 0, 'name': 'Аудио и видео'},
            {'cat1': 'Электроника', 'click': 0, 'name': 'Фототовары'},
            {'cat1': 'Электроника', 'click': 0, 'name': 'Умная электроника'},

            {'cat1': 'Красота и здоровье', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Красота и здоровье', 'click': 0, 'name': 'Макияж'},
            {'cat1': 'Красота и здоровье', 'click': 0, 'name': 'Маникюр'},
            {'cat1': 'Красота и здоровье', 'click': 0, 'name': 'Уход за кожей'},
            {'cat1': 'Красота и здоровье', 'click': 0, 'name': 'Уход за волосами'},
            {'cat1': 'Красота и здоровье', 'click': 0, 'name': 'Здоровье и гигиена'},

            {'cat1': 'Спорт и развлечения', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Спорт и развлечения', 'click': 0, 'name': 'Кемпинг и туризм'},
            {'cat1': 'Спорт и развлечения', 'click': 0, 'name': 'Игры с мячом'},
            {'cat1': 'Спорт и развлечения', 'click': 0, 'name': 'Обувь'},

            {'cat1': 'Техника и инструменты', 'click': 0, 'name': 'Самые популярные'},
            {'cat1': 'Техника и инструменты', 'click': 0, 'name': 'Инструменты'},
            {'cat1': 'Техника и инструменты', 'click': 0, 'name': 'Бытовая техника'},
            {'cat1': 'Техника и инструменты', 'click': 0, 'name': 'Безопасность и защита'},
            {'cat1': 'Техника и инструменты', 'click': 0, 'name': 'Материалы для ремонта'},
        ]
        categories3 = [
            {'cat1': 'Одежда для женщин', 'cat2': 'Верх', 'click': 0, 'name': 'Майки и футболки'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Верх', 'click': 0, 'name': 'Рубашки'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Верх', 'click': 0, 'name': 'Толстовки и кофты'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Верх', 'click': 0, 'name': 'Кардиганы'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Верх', 'click': 0, 'name': 'Пуловеры'},

            {'cat1': 'Одежда для женщин', 'cat2': 'Низ', 'click': 0, 'name': 'Юбки'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Низ', 'click': 0, 'name': 'Шорты'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Низ', 'click': 0, 'name': 'Джинсы'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Низ', 'click': 0, 'name': 'Брюки'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Низ', 'click': 0, 'name': 'Леггинсы'},

            {'cat1': 'Одежда для женщин', 'cat2': 'Куртки и пальто', 'click': 0, 'name': 'Спортивные куртки'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Куртки и пальто', 'click': 0, 'name': 'Стандартные куртки'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Куртки и пальто', 'click': 0, 'name': 'Тренчи'},

            {'cat1': 'Одежда для женщин', 'cat2': 'Нижнее белье', 'click': 0, 'name': 'Бюстгалтеры'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Нижнее белье', 'click': 0, 'name': 'Трусы'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Нижнее белье', 'click': 0, 'name': 'Коплекты белья'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Нижнее белье', 'click': 0, 'name': 'Ночные сорочки и рубашки'},
            {'cat1': 'Одежда для женщин', 'cat2': 'Нижнее белье', 'click': 0, 'name': 'Пижамные комплекты'},

            {'cat1': 'Одежда для мужчин', 'cat2': 'Верх', 'click': 0, 'name': 'Майки и футболки'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Верх', 'click': 0, 'name': 'Рубашки'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Верх', 'click': 0, 'name': 'Костюмы и пиджаки'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Верх', 'click': 0, 'name': 'Толстовки и кофты'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Верх', 'click': 0, 'name': 'Куртки и пальто'},

            {'cat1': 'Одежда для мужчин', 'cat2': 'Низ', 'click': 0, 'name': 'Повседневные штаны'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Низ', 'click': 0, 'name': 'Шорты'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Низ', 'click': 0, 'name': 'Джинсы'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Низ', 'click': 0, 'name': 'Нижнее белье'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Низ', 'click': 0, 'name': 'Носки'},

            {'cat1': 'Одежда для мужчин', 'cat2': 'Одежда и аксессуары', 'click': 0, 'name': 'Бейсболки'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Одежда и аксессуары', 'click': 0, 'name': 'Пояса и ремни'},
            {'cat1': 'Одежда для мужчин', 'cat2': 'Одежда и аксессуары', 'click': 0, 'name': 'Очки и аксессуары'},

            {'cat1': 'Все для детей', 'cat2': 'Одежда для девочек', 'click': 0, 'name': 'Платья'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для девочек', 'click': 0, 'name': 'Комплекты одежды'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для девочек', 'click': 0, 'name': 'Топы и футболки'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для девочек', 'click': 0, 'name': 'Купальники'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для девочек', 'click': 0, 'name': 'Аксессуары'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для девочек', 'click': 0, 'name': 'Семейные комплекты'},

            {'cat1': 'Все для детей', 'cat2': 'Одежда для мальчиков', 'click': 0, 'name': 'Комплекты одежды'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для мальчиков', 'click': 0, 'name': 'Футболки'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для мальчиков', 'click': 0, 'name': 'Толстовки и кофты'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для мальчиков', 'click': 0, 'name': 'Верхняя одежда и пальто'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для мальчиков', 'click': 0, 'name': 'Джинсы'},
            {'cat1': 'Все для детей', 'cat2': 'Одежда для мальчиков', 'click': 0, 'name': 'Аксессуары'},

            {'cat1': 'Все для детей', 'cat2': 'Игрушки и хобби', 'click': 0, 'name': 'Радиоуправляемые модели'},
            {'cat1': 'Все для детей', 'cat2': 'Игрушки и хобби', 'click': 0, 'name': 'Мякгие игрушки'},
            {'cat1': 'Все для детей', 'cat2': 'Игрушки и хобби', 'click': 0, 'name': 'Игрушечные фигурки'},
            {'cat1': 'Все для детей', 'cat2': 'Игрушки и хобби', 'click': 0, 'name': 'Лего'},
            {'cat1': 'Все для детей', 'cat2': 'Игрушки и хобби', 'click': 0, 'name': 'Конструкторы'},
            {'cat1': 'Все для детей', 'cat2': 'Игрушки и хобби', 'click': 0, 'name': 'Спорт и игры на природе'},

            {'cat1': 'Все для детей', 'cat2': 'Сумки и обувь', 'click': 0, 'name': 'Первая обувь для малышей'},
            {'cat1': 'Все для детей', 'cat2': 'Сумки и обувь', 'click': 0, 'name': 'Обувь для девочек'},
            {'cat1': 'Все для детей', 'cat2': 'Сумки и обувь', 'click': 0, 'name': 'Обувь для мальчиков'},
            {'cat1': 'Все для детей', 'cat2': 'Сумки и обувь', 'click': 0, 'name': 'Школьные ранцы'},
            {'cat1': 'Все для детей', 'cat2': 'Сумки и обувь', 'click': 0, 'name': 'Сумки через плечо'},

            {'cat1': 'Телефоны и планшеты', 'cat2': 'Мобильные телефоны', 'click': 0, 'name': 'Восьмиядерные'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Мобильные телефоны', 'click': 0, 'name': 'Четырехядерные'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Мобильные телефоны', 'click': 0, 'name': 'С одной SIM-картой'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Мобильные телефоны', 'click': 0, 'name': 'С двумы SIM-картами'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Мобильные телефоны', 'click': 0, 'name': 'iPhone'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Мобильные телефоны', 'click': 0, 'name': 'Samsung'},

            {'cat1': 'Телефоны и планшеты', 'cat2': 'Планшеты', 'click': 0, 'name': 'Восьмиядерные'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Планшеты', 'click': 0, 'name': 'Четырехядерные'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Планшеты', 'click': 0, 'name': 'С одной SIM-картой'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Планшеты', 'click': 0, 'name': 'С двумы SIM-картами'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Планшеты', 'click': 0, 'name': 'iPhone'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Планшеты', 'click': 0, 'name': 'Samsung'},

            {'cat1': 'Телефоны и планшеты', 'cat2': 'Запчасти', 'click': 0, 'name': 'Дисплеи'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Запчасти', 'click': 0, 'name': 'Батареи'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Запчасти', 'click': 0, 'name': 'Корпуса'},

            {'cat1': 'Телефоны и планшеты', 'cat2': 'Сумки и чехлы', 'click': 0, 'name': 'Бамперы'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Сумки и чехлы', 'click': 0, 'name': 'Водонепроницаемые чехлы'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Сумки и чехлы', 'click': 0, 'name': 'Кожанные чехлы'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Сумки и чехлы', 'click': 0, 'name': 'Алюминиевые чехлы'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Сумки и чехлы', 'click': 0, 'name': 'Чехлы со стразами'},

            {'cat1': 'Телефоны и планшеты', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Резервное питание'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Защитные пленки'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Зарядные устройства'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Антенны для связи'},
            {'cat1': 'Телефоны и планшеты', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Беспроводные терминалы'},

            {'cat1': 'Компьютерная техника', 'cat2': 'Ноутбуки', 'click': 0, 'name': 'Ноутбуки'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Ноутбуки', 'click': 0, 'name': 'Сумки и чехлы'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Ноутбуки', 'click': 0, 'name': 'Сумки и чехлы'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Ноутбуки', 'click': 0, 'name': 'Сумки и чехлы'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Ноутбуки', 'click': 0, 'name': 'Клавиатуры'},

            {'cat1': 'Компьютерная техника', 'cat2': 'Офисная электроника', 'click': 0, 'name': 'Принтеры'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Офисная электроника', 'click': 0, 'name': '3d принтеры'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Офисная электроника', 'click': 0, 'name': 'лазерные ручки'},

            {'cat1': 'Компьютерная техника', 'cat2': 'Устройства хранения', 'click': 0, 'name': 'USB флэшки'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Устройства хранения', 'click': 0, 'name': 'Карты памяти'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Устройства хранения', 'click': 0, 'name': 'Внешние жесткие диски'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Устройства хранения', 'click': 0, 'name': 'Корпуса для жестких дисков'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Устройства хранения', 'click': 0, 'name': 'SSD'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Сеть', 'click': 0, 'name': 'Роутеры'},
            {'cat1': 'Компьютерная техника', 'cat2': 'Сеть', 'click': 0, 'name': '3G модемы'},

            {'cat1': 'Автотовары', 'cat2': 'Автомобили', 'click': 0, 'name': 'Автомобили'},
            {'cat1': 'Автотовары', 'cat2': 'Электроника', 'click': 0, 'name': 'Видеорегистраторы'},
            {'cat1': 'Автотовары', 'cat2': 'Электроника', 'click': 0, 'name': 'GPS-навигаторы'},
            {'cat1': 'Автотовары', 'cat2': 'Электроника', 'click': 0, 'name': 'Видеоплееры'},
            {'cat1': 'Автотовары', 'cat2': 'Электроника', 'click': 0, 'name': 'Аудиоплееры'},
            {'cat1': 'Автотовары', 'cat2': 'Электроника', 'click': 0, 'name': 'Радио'},
            {'cat1': 'Автотовары', 'cat2': 'Электроника', 'click': 0, 'name': 'Системы безопасности'},
            {'cat1': 'Автотовары', 'cat2': 'Электроника', 'click': 0, 'name': 'Детекторы для авто'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Стайлинг автомобиля'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Коврики'},

            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Чехлы на руль'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Хранение и организация'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Прикуриватели'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Внешнее освещение'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Освежители воздуха'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Освежители воздуха'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Чехлы для автомобиля'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Зарядные устройства'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Наклейки на авто'},
            {'cat1': 'Автотовары', 'cat2': 'Аксессуары', 'click': 0, 'name': 'Наклейки на авто'},

            {'cat1': 'Автотовары', 'cat2': 'Инструменты', 'click': 0, 'name': 'Губки, салфетки, кисти'},
            {'cat1': 'Автотовары', 'cat2': 'Инструменты', 'click': 0, 'name': 'Диагностика'},
            {'cat1': 'Автотовары', 'cat2': 'Инструменты', 'click': 0, 'name': 'Уход за покрытием'},
            {'cat1': 'Автотовары', 'cat2': 'Инструменты', 'click': 0, 'name': 'Губки, полотенца, тряпки'},
            {'cat1': 'Автотовары', 'cat2': 'Инструменты', 'click': 0, 'name': 'Бортовая диагностика'},
            {'cat1': 'Автотовары', 'cat2': 'Инструменты', 'click': 0, 'name': 'Мытье автомобиля'},
            {'cat1': 'Автотовары', 'cat2': 'Инструменты', 'click': 0, 'name': 'Пылесосы'},
            {'cat1': 'Автотовары', 'cat2': 'Инструменты', 'click': 0, 'name': 'Насосы'},

            {'cat1': 'Бижутерия и часы', 'cat2': 'Бижутерия', 'click': 0, 'name': 'Ожерелья и подвески'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Бижутерия', 'click': 0, 'name': 'Серьги'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Бижутерия', 'click': 0, 'name': 'Браслеты'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Бижутерия', 'click': 0, 'name': 'Кольца'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Бижутерия', 'click': 0, 'name': 'Ювелирные комплекты'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Бижутерия', 'click': 0, 'name': 'Бриллианты'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Бижутерия', 'click': 0, 'name': 'Серебро'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Бижутерия', 'click': 0, 'name': 'Жемчуг'},

            {'cat1': 'Бижутерия и часы', 'cat2': 'Часы', 'click': 0, 'name': 'Мужские часы'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Часы', 'click': 0, 'name': 'Женские часы'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Часы', 'click': 0, 'name': 'Механические часы'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Часы', 'click': 0, 'name': 'Кварцевые часы'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Часы', 'click': 0, 'name': 'Спортивные часы'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Часы', 'click': 0, 'name': 'Часы-браслеты'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Часы', 'click': 0, 'name': 'Дизайнерские часы'},

            {'cat1': 'Бижутерия и часы', 'cat2': 'Ювелирные украшения', 'click': 0, 'name': 'Ожерелья и подвески'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Ювелирные украшения', 'click': 0, 'name': 'Серьги'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Ювелирные украшения', 'click': 0, 'name': 'Браслеты'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Ювелирные украшения', 'click': 0, 'name': 'Кольца'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Ювелирные украшения', 'click': 0, 'name': 'Ювелирные комплекты'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Ювелирные украшения', 'click': 0, 'name': 'Бриллианты'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Ювелирные украшения', 'click': 0, 'name': 'Серебро'},
            {'cat1': 'Бижутерия и часы', 'cat2': 'Ювелирные украшения', 'click': 0, 'name': 'Жемчуг'},

            {'cat1': 'Сумки и обувь', 'cat2': 'Женские сумки', 'click': 0, 'name': 'Наплечные сумки'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женские сумки', 'click': 0, 'name': 'Сумки с короткими ручками'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женские сумки', 'click': 0, 'name': 'Сумки через плечо'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женские сумки', 'click': 0, 'name': 'Кошельки'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женские сумки', 'click': 0, 'name': 'Рюкзаки'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женские сумки', 'click': 0, 'name': 'Клатчи'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женские сумки', 'click': 0, 'name': 'Каошельки и портмоне'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужские сумки', 'click': 0, 'name': 'Сумки через плечо'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужские сумки', 'click': 0, 'name': 'Рюкзаки'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужские сумки', 'click': 0, 'name': 'Кошельки'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужские сумки', 'click': 0, 'name': 'Багаж и дорожные сумки'},

            {'cat1': 'Сумки и обувь', 'cat2': 'Женская обувь', 'click': 0, 'name': 'Сапоги и ботинки'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женская обувь', 'click': 0, 'name': 'Туфли'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женская обувь', 'click': 0, 'name': 'На плоской подошве'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женская обувь', 'click': 0, 'name': 'Оксфорды'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женская обувь', 'click': 0, 'name': 'Лоферы'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женская обувь', 'click': 0, 'name': 'Сандалии'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женская обувь', 'click': 0, 'name': 'Тапочки'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женская обувь', 'click': 0, 'name': 'Ботильоны'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Женская обувь', 'click': 0, 'name': 'Сапоги выше колен'},

            {'cat1': 'Сумки и обувь', 'cat2': 'Мужская обувь', 'click': 0, 'name': 'Сапоги'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужская обувь', 'click': 0, 'name': 'Лоферы'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужская обувь', 'click': 0, 'name': 'Кроссовки'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужская обувь', 'click': 0, 'name': 'Сандалии'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужская обувь', 'click': 0, 'name': 'Тапочки'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужская обувь', 'click': 0, 'name': 'Деловая обувь'},
            {'cat1': 'Сумки и обувь', 'cat2': 'Мужская обувь', 'click': 0, 'name': 'Шлепанцы'},

            {'cat1': 'Для дома и сада', 'cat2': 'Домашний декор', 'click': 0, 'name': 'Декор своими руками'},
            {'cat1': 'Для дома и сада', 'cat2': 'Домашний декор', 'click': 0, 'name': 'Наклейки на стену'},
            {'cat1': 'Для дома и сада', 'cat2': 'Домашний декор', 'click': 0, 'name': 'Рисование и каллиграфия'},
            {'cat1': 'Для дома и сада', 'cat2': 'Домашний декор', 'click': 0, 'name': 'Часы-браслеты'},
            {'cat1': 'Для дома и сада', 'cat2': 'Домашний декор', 'click': 0, 'name': 'Фотоальбомы'},
            {'cat1': 'Для дома и сада', 'cat2': 'Домашний декор', 'click': 0, 'name': 'Праздничный декор'},

            {'cat1': 'Для дома и сада', 'cat2': 'Рукоделие и вышивка', 'click': 0, 'name': 'Вышивка'},
            {'cat1': 'Для дома и сада', 'cat2': 'Рукоделие и вышивка', 'click': 0, 'name': 'Ткань'},
            {'cat1': 'Для дома и сада', 'cat2': 'Рукоделие и вышивка', 'click': 0, 'name': 'Кружево'},
            {'cat1': 'Для дома и сада', 'cat2': 'Рукоделие и вышивка', 'click': 0, 'name': 'Стразы'},

            {'cat1': 'Для дома и сада', 'cat2': 'Текстиль для дома', 'click': 0, 'name': 'Постельное белье'},
            {'cat1': 'Для дома и сада', 'cat2': 'Текстиль для дома', 'click': 0, 'name': 'Шторы'},
            {'cat1': 'Для дома и сада', 'cat2': 'Текстиль для дома', 'click': 0, 'name': 'Ковры'},
            {'cat1': 'Для дома и сада', 'cat2': 'Текстиль для дома', 'click': 0, 'name': 'Полотенца'},
            {'cat1': 'Для дома и сада', 'cat2': 'Текстиль для дома', 'click': 0, 'name': 'Подушки'},

            {'cat1': 'Для дома и сада', 'cat2': 'Освещение', 'click': 0, 'name': 'Люстры'},
            {'cat1': 'Для дома и сада', 'cat2': 'Освещение', 'click': 0, 'name': 'Светильники'},
            {'cat1': 'Для дома и сада', 'cat2': 'Освещение', 'click': 0, 'name': 'Светодиодное освещение'},

            {'cat1': 'Для дома и сада', 'cat2': 'Кухня, столовая, бар', 'click': 0, 'name': 'Кухонная посуда'},
            {'cat1': 'Для дома и сада', 'cat2': 'Кухня, столовая, бар', 'click': 0, 'name': 'Кухонные ножи и аксессуары'},
            {'cat1': 'Для дома и сада', 'cat2': 'Кухня, столовая, бар', 'click': 0, 'name': 'Формы для выпечки'},

            {'cat1': 'Электроника', 'cat2': 'Аудио и видео', 'click': 0, 'name': 'Колонки'},
            {'cat1': 'Электроника', 'cat2': 'Аудио и видео', 'click': 0, 'name': 'ТВ-приемники'},
            {'cat1': 'Электроника', 'cat2': 'Аудио и видео', 'click': 0, 'name': 'Проекторы и аксессуары'},
            {'cat1': 'Электроника', 'cat2': 'Аудио и видео', 'click': 0, 'name': 'Видео и аудио аксессуары'},
            {'cat1': 'Электроника', 'cat2': 'Аудио и видео', 'click': 0, 'name': 'MP3-плееры'},
            {'cat1': 'Электроника', 'cat2': 'Аудио и видео', 'click': 0, 'name': 'MP4-плееры'},

            {'cat1': 'Электроника', 'cat2': 'Фототовары', 'click': 0, 'name': 'Штативы и аксессуары'},
            {'cat1': 'Электроника', 'cat2': 'Фототовары', 'click': 0, 'name': 'Мини-видеокамеры'},
            {'cat1': 'Электроника', 'cat2': 'Фототовары', 'click': 0, 'name': 'Камеры и фотоаксессуары'},
            {'cat1': 'Электроника', 'cat2': 'Фототовары', 'click': 0, 'name': 'Объективы и аксессуары'},
            {'cat1': 'Электроника', 'cat2': 'Фототовары', 'click': 0, 'name': 'Портативные видеокамеры'},

            {'cat1': 'Электроника', 'cat2': 'Умная электроника', 'click': 0, 'name': 'Носимая электроника'},
            {'cat1': 'Электроника', 'cat2': 'Умная электроника', 'click': 0, 'name': 'Для дома'},
            {'cat1': 'Электроника', 'cat2': 'Умная электроника', 'click': 0, 'name': 'Умные часы'},
            {'cat1': 'Электроника', 'cat2': 'Умная электроника', 'click': 0, 'name': 'Игровые приставки, консоли'},
            {'cat1': 'Электроника', 'cat2': 'Умная электроника', 'click': 0, 'name': 'PlayStation'},

            {'cat1': 'Красота и здоровье', 'cat2': 'Макияж', 'click': 0, 'name': 'Косметика'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Макияж', 'click': 0, 'name': 'Для глаз'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Макияж', 'click': 0, 'name': 'Инструменты и аксессуары'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Макияж', 'click': 0, 'name': 'Для лица'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Макияж', 'click': 0, 'name': 'Для губ'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Макияж', 'click': 0, 'name': 'Наборы для макияжа'},

            {'cat1': 'Красота и здоровье', 'cat2': 'Маникюр', 'click': 0, 'name': 'Дизайн ногтей'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Маникюр', 'click': 0, 'name': 'Лаки для ногтей'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Маникюр', 'click': 0, 'name': 'Инструменты для маникюра'},

            {'cat1': 'Красота и здоровье', 'cat2': 'Уход за кожей', 'click': 0, 'name': 'Питательные маски'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Уход за кожей', 'click': 0, 'name': 'Для лица'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Уход за кожей', 'click': 0, 'name': 'Кремы для похудения'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Уход за кожей', 'click': 0, 'name': 'Эфирные масла'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Уход за кожей', 'click': 0, 'name': 'Массаж и релаксация'},

            {'cat1': 'Красота и здоровье', 'cat2': 'Уход за волосами', 'click': 0, 'name': 'Выпрямляющие утюжки'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Уход за волосами', 'click': 0, 'name': 'Бигуди'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Уход за волосами', 'click': 0, 'name': 'Окрашивание волос'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Уход за волосами', 'click': 0, 'name': 'Средства от выпадения волос'},

            {'cat1': 'Красота и здоровье', 'cat2': 'Здоровье и гигиена', 'click': 0, 'name': 'Бритье и эпиляция'},
            {'cat1': 'Красота и здоровье', 'cat2': 'Здоровье и гигиена', 'click': 0, 'name': 'Интимные товары'},

            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Приманки'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Лески'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Удочки'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Катушки'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Фонари и фары'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Электроника'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Велосипеды'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Велоперчатки'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Спортивные очки'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Одежда велосипедиста'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Бег'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Кемпинг и туризм', 'click': 0, 'name': 'Охота'},

            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Футбольные майки'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Футбольная обувь'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Футбольные гетры'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Баскетбольная обувь'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Баскетбольные майки'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Американский футбол'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Баскетбол'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Регби'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Теннис'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Волейбол'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Спортивные игра с ракетками'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Бейсбол и софтбол'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Игры с мячом', 'click': 0, 'name': 'Хоккей'},

            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Танцы'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Бокс'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Туризм'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Фитнес и бодибилдинг'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Эспандеры и ленты'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Плавание и дайвинг'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Скейтборды и роликовые коньки'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Лыжи и сноуборд'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Игры для дома'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Спортивная защита'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Музыкальные инструменты'},
            {'cat1': 'Спорт и развлечения', 'cat2': 'Обувь', 'click': 0, 'name': 'Сувениры и брелоки'},

            {'cat1': 'Техника и инструменты', 'cat2': 'Бытовая техника', 'click': 0, 'name': 'Техника для кухни'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Бытовая техника', 'click': 0, 'name': 'Кофеварки'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Бытовая техника', 'click': 0, 'name': 'Соковыжималки'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Бытовая техника', 'click': 0, 'name': 'Техника для дома'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Бытовая техника', 'click': 0, 'name': 'Техника для уборки'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Бытовая техника', 'click': 0, 'name': 'Запчасти для бытовой техники'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Бытовая техника', 'click': 0, 'name': 'Прочая бытовая техника'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Бытовая техника', 'click': 0, 'name': 'Для личного пользования'},

            {'cat1': 'Техника и инструменты', 'cat2': 'Инструменты', 'click': 0, 'name': 'Ручные инструменты'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Инструменты', 'click': 0, 'name': 'Механические инструменты'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Инструменты', 'click': 0, 'name': 'Аксессуары'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Инструменты', 'click': 0, 'name': 'Измерительные инструменты'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Инструменты', 'click': 0, 'name': 'Наборы'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Инструменты', 'click': 0, 'name': 'Абразивные инструменты'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Инструменты', 'click': 0, 'name': 'Запчасти'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Материалы для ремонта', 'click': 0, 'name': 'Крепежи и крючки'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Материалы для ремонта', 'click': 0, 'name': 'Замки и запоры'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Материалы для ремонта', 'click': 0, 'name': 'Мебельная фурнитура'},
            {'cat1': 'Техника и инструменты', 'cat2': 'Материалы для ремонта', 'click': 0, 'name': 'Дверная фурнитура'},

        ]
        Category1.objects.all().delete()
        for category in categories1:
            category = Category1(**category)
            category.save()

        Category2.objects.all().delete()
        for category in categories2:
            parent_name = category['cat1']
            cat1 = Category1.objects.get(name=parent_name)
            category['cat1'] = cat1
            print(category, cat1)
            category = Category2(**category)
            category.save()

        Category3.objects.all().delete()
        for category in categories3:
            cat1 = Category1.objects.get(name=category['cat1'])#отобрать все совпадения
            cat2 = Category2.objects.filter(cat1_id=cat1.id).get(name=category['cat2'])
            cat3 = Category2.objects.filter(name=category['cat2'], cat1=cat1.id)
            print(cat1.id, cat2.id, cat1, cat3[0], category['name'], cat3)
            line = Category3.objects.create(
                name=category['name'],
                click=category['click'],
                cat1_id=cat1.id,
                cat2_id=cat2.id)