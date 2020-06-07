import glob
import os
import re
from collections import OrderedDict

from gensim.summarization import keywords

from django.conf import settings
from django.shortcuts import render
from django.views import View


class Words(View):
    def extract_keywords(self, text):
        """
        Extracts keyword from given text based on gensim word scoring.
        Set ratio to 0.1 to return highest scoring keywords.

        return a list of keywords.
        """
        return keywords(text, split=True, ratio=0.1)

    def process_files(self, file_path=None, file_type='txt'):
        counter = {}
        # Fallback
        if not file_path:
            file_path = os.path.join(settings.BASE_DIR, 'word_count/default_docs')

        # Find all files in a given directory.
        documents = [doc for doc in glob.glob(file_path + f"**/*.{file_type}", recursive=True)]

        for doc in documents:
            with open(doc, 'r') as doc_file:
                # Remove newlines from text
                file_text = doc_file.read().replace('\n', '')
                file_keywords = self.extract_keywords(file_text)

                for word in file_keywords:
                    # TODO: Need to find out why gensim keyword extracts and adds suffixes to words. let and letting
                    word_count = file_text.lower().count(word.lower())
                    if word_count > 0:
                        if counter.get(word):
                            counter[word]['count'] += word_count
                            counter[word]['files'].append(doc)
                            counter[word]['sentence'] + re.findall(rf"([^.]*?{word}[^.]*\.)", file_text.lower())

                        else:
                            counter[word] = {
                                'count': word_count,
                                'files': [doc],
                                'sentence': re.findall(rf"([^. ]*?{word}[^.]*\.)", file_text.lower())
                            }
                    else:
                        continue

        return OrderedDict(sorted(counter.items()))

    def get(self, request):
        words = self.process_files()

        return render(request, 'index.html', {'words': words})
