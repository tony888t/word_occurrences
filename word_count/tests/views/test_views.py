import os
import pytest

from django.conf import settings
from word_count.views import Words


@pytest.fixture
def text_sample():
    return '''Challenges in natural language processing frequently involve
    speech recognition, natural language understanding, natural language
    generation (frequently from formal, machine-readable logical forms),
    connecting language and machine perception, dialog systems, or some
    combination thereof. Machine learning is cool.'''


@pytest.fixture
def sample_doc(text_sample):
    with open('test.txt', 'w') as test_doc:
        test_doc.write(text_sample)


@pytest.fixture
def expected_extracted_keywords():
    return ['machine', 'language']


def test_keyword_extactions(text_sample, expected_extracted_keywords):
    words = Words()
    result = words.extract_keywords(text_sample)

    assert result == expected_extracted_keywords


def test_word_count(sample_doc, expected_extracted_keywords):
    words = Words()
    result = words.process_files(file_path=settings.BASE_DIR)

    os.remove('test.txt')

    for keyword in expected_extracted_keywords:
        assert keyword in result.keys()

    assert result['language']['count'] == 4
    assert result['machine']['count'] == 3


def test_where_word_is_used(sample_doc, expected_extracted_keywords):
    words = Words()
    result = words.process_files(file_path=settings.BASE_DIR)

    os.remove('test.txt')

    assert len(result['machine']['sentence']) == 2
    assert result['machine']['sentence'][1] == 'machine learning is cool.'


def test_which_file_word_is_used(sample_doc, expected_extracted_keywords):
    words = Words()
    result = words.process_files(file_path=settings.BASE_DIR)

    os.remove('test.txt')

    assert result['machine']['files'][0] == os.path.join(settings.BASE_DIR, 'test.txt')
