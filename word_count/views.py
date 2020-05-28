import os
import re
import string
from collections import Counter
from pathlib import Path

from django.conf import settings
from django.shortcuts import render
from django.views import View
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from .models import Word


class Words(View):
    def remove_stop_words(self, words):
        # Remove punctuation
        punct_free_text = ''.join(text for text in words if text not in string.punctuation)

        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(punct_free_text)

        return [word for word in word_tokens if words not in stop_words]

    def process_files(self, file_path=None, file_type='txt'):
        # Fallback
        if not file_path:
            file_path = os.path.join(settings.BASE_DIR, 'word_count/default_docs')

        pathlist = Path(file_path).glob(f'**/*.{file_type}')

        for path in pathlist:
            with open(path, 'r') as doc:
                filtered_text = self.remove_stop_words(doc.read())
                for text in filtered_text:

                

    def get(self, request):
        pass
