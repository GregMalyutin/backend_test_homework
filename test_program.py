import os

import program

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]

files_list = ['program.py', 'readme.md']


def test_program():
    for filename in files_list:
        assert filename in dir_files, f'Файл `{filename}` не найден в корне репозитория'

    try:
        import program as _program  # noqa: F401
    except Exception as e:
        assert False, (
            'Не удалось запустить `program.py`. '
            'Исправьте в нем ошибки:\n'
            f'{e}'
        )


def test_stair_workout():
    text = program.recommend('1')
    assert 'лестница' in text.lower() or 'StairMaster' in text
    assert 'Интервалы' in text


def test_leg_day_workout():
    text = program.recommend('ноги')
    assert 'День ног' in text
    assert 'Приседания' in text
    assert 'Жим ногами' in text


def test_unknown_choice():
    text = program.recommend('йога')
    assert 'Неизвестный выбор' in text


def test_compare():
    text = program.compare()
    assert 'Лестница' in text
    assert 'День ног' in text
