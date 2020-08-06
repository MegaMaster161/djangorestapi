
from django.utils.text import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(word_for_translate):
    """
    Проводим транслитерацию кирилических обозначений.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in word_for_translate.lower()))


def change_value_in_dict(data, request_data):
    if len(data) > 0:
        for key, value in data.items():
            request_data[key] = data[key]
    else:
        raise NameError

            



