#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ============================================================================================================

"""
 getArticleInfoFromCitationControllerStandAlone.py

Copyright © 2017 Yuto Mizutani.
This software is released under the MIT License.

Version: 1.0.0

TranslateAuthors: Yuto Mizutani
E-mail: yuto.mizutani.dev@gmail.com
Website: http://operantroom.com

Created: 2017/12/09
Device: MacBook Pro (Retina, 13-inch, Mid 2015)
OS: macOS Serria version 10.12.6
IDE: PyCharm Community Edition 2017.2.4
Python: 3.6.1
"""

# --- References ---
# --- notes ---
# --- Information ---
# --- Circumstances ---

# === import ===========================================================================================================

""" Standard library """
""" Third party library """
""" Local library """
from getdoi.articleinfo.getArticleInfoFromCitation.getArticleInfoFromCitationController import GetArticleInfoFromCitationControllerImpl

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================

# === variables ========================================================================================================

# ======================================================================================================================


class ReadEnteredTextStandAloneImpl:
    """ If user display_input, drop filesPath then return files, exit then return None """
    # -- variables --
    __display_input_text = '> '
    __display_output_text = '>> Read: '

    # reader = ReadEnteredTextStandAloneImpl()
    # while True:
    #     print()
    #     print('Enter the characters...')
    #     text = reader.read()
    #     if text is None:
    #         # exit
    #         break

    def read(self) -> str or None:
        entered_str = input(self.__display_input_text)
        if self.__decision_exit(entered_str):
            # if user display_inputs exit meaning then exit
            return None
        else:
            print('{0}{1}'.format(self.__display_output_text, entered_str))
            return entered_str

    def __decision_exit(self, text) -> bool:
        # -- constants --
        EXIT_TEXTS = ['e', '-e', 'exit', 'exit()', 'Exit', 'Exit()']
        # decision match strings argument and EXIT_TEXTS
        for exit_text in EXIT_TEXTS:
            if text == exit_text:
                return True
        return False

# ======================================================================================================================


class GetArticleInfoFromCitationControllerStandAloneImpl:
    # citation = 'Fleshler, M., & Hoffman, H. S. (1962). A progression for generating variable-interval schedules. Journal of the experimental analysis of behavior, 5(4), 529.'
    # -- variables --
    is_help = True
    controller = GetArticleInfoFromCitationControllerImpl
    reader = ReadEnteredTextStandAloneImpl

    # -- init --
    def __init__(self):
        print('-STAND ALONE MODE- getArticleInfoFromCitationController.py')
        print('Display the article info for your entered citation.')
        self.controller = GetArticleInfoFromCitationControllerImpl()
        self.reader = ReadEnteredTextStandAloneImpl()
        self.loop()

    def loop(self):
        while True:
            print()
            print('Enter the citation...')
            if self.is_help:
                print('... (citation)   : Article info')
                print('... -a (citation): Authors')
                print('... -f (citation): 1st author')
                print('... -y (citation): Year')
                print('... -t (citation): Article title')
                print('... -m (citation): Article Main title')
                print('... -s (citation): Article Sub title')
                print('... -j (citation): Journal')
                print('... -v (citation): Volume')
                print('... -i (citation): Issue')
                print('... -p (citation): Pages')
                print('... -d (citation): DOI')
                print('... -h           : Hide help')
            text = self.reader.read()
            if text is None:
                # exit
                break
            else:
                if text == '':
                    print('Entered text is null or empty!')
                    continue
                while text[0] == ' ':
                    text = text[1:]
                while text[-1] == ' ':
                    text = text[:-1]

                if text == 'h' or text[0:2] == '-h':
                    print('Hide help!')
                    self.is_help = not self.is_help
                    continue

                elif text[0:3] == '-a ':
                    citation = text[3:]
                    authors = self.controller.get_authors(citation=citation)
                    print('Authors: {0}'.format(authors))
                    continue

                elif text[0:3] == '-f ':
                    citation = text[3:]
                    first_author = self.controller.get_first_author(citation=citation)
                    print('1st author: {0}'.format(first_author))
                    continue

                elif text[0:3] == '-y ':
                    citation = text[3:]
                    year = self.controller.get_year(citation=citation)
                    print('Year: {0}'.format(year))
                    continue

                elif text[0:3] == '-t ':
                    citation = text[3:]
                    article_title = self.controller.get_article_title(citation=citation)
                    print('Title: {0}'.format(article_title))
                    continue

                elif text[0:3] == '-m ':
                    citation = text[3:]
                    article_main_title = self.controller.get_article_main_title(citation=citation)
                    print('Main Title: {0}'.format(article_main_title))
                    continue

                elif text[0:3] == '-s ':
                    citation = text[3:]
                    article_sub_title = self.controller.get_article_sub_title(citation=citation)
                    print('Sub title: {0}'.format(article_sub_title))
                    continue

                elif text[0:3] == '-j ':
                    citation = text[3:]
                    journal_title = self.controller.get_journal_title(citation=citation)
                    print('Journal: {0}'.format(journal_title))
                    continue

                elif text[0:3] == '-v ':
                    citation = text[3:]
                    volume = self.controller.get_volume(citation=citation)
                    print('Volume: {0}'.format(volume))
                    continue

                elif text[0:3] == '-i ':
                    citation = text[3:]
                    issue = self.controller.get_issue(citation=citation)
                    print('Issue: {0}'.format(issue))
                    continue

                elif text[0:3] == '-p ':
                    citation = text[3:]
                    pages = self.controller.get_pages(citation=citation)
                    print('Pages: {0}'.format(pages))
                    continue

                elif text[0:3] == '-d ':
                    citation = text[3:]
                    doi = self.controller.get_doi(citation=citation)
                    print('DOI: {0}'.format(doi))
                    continue

                else:
                    article_info = self.controller.get_all(citation=text)
                    article_info.print()
                    continue


# ======================================================================================================================


if __name__ == '__main__':
    main = GetArticleInfoFromCitationControllerStandAloneImpl()
