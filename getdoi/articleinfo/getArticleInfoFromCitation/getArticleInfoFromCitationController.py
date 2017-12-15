#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ======================================================================================================

"""
 __init__.py

Copyright © 2017 Yuto Mizutani.
This software is released under the MIT License.

Version: 1.0.0

TranslateAuthors: Yuto Mizutani
E-mail: yuto.mizutani.dev@gmail.com
Website: http://operantroom.com

Created: 2017/12/07
Device: MacBook Pro (Retina, 13-inch, Mid 2015)
OS: macOS Serria version 10.12.6
IDE: PyCharm Community Edition 2017.2.4
Python: 3.6.1
"""

# --- References ---
# --- notes ---
# --- Information ---
"""
"""
# --- Circumstances ---
"""
"""

# === import ========================================================================================================

""" Standard library """
from enum import Enum
""" Third party library """
""" Local library """
from .gettableArticleInfo import GettableArticleInfo
from getdoi.articleinfo.articleInfo import ArticleInfo
from .apa import APA


# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================

# === variables ========================================================================================================


# ======================================================================================================================


class CitationType(Enum):
    APA = APA


class GetArticleInfoFromCitationControllerImpl(GettableArticleInfo):
    # -- variables --
    citation_impl = GettableArticleInfo

    # -- controller --
    def get_all(self, *, citation: str) -> ArticleInfo or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            info = self.citation_impl.get_all(citation=citation)
            return info
        else:
            return None

    def get_authors(self, *, citation: str) -> [str] or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            authors = self.citation_impl.get_authors(citation=citation)
            return authors
        else:
            return None

    def get_first_author(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            first_author = self.citation_impl.get_first_author(citation=citation)
            return first_author
        else:
            return None

    def get_year(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            year = self.citation_impl.get_year(citation=citation)
            return year
        else:
            return None

    def get_article_title(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            article_title = self.citation_impl.get_article_title(citation=citation)
            return article_title
        else:
            return None

    def get_article_main_title(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            article_main_title = self.citation_impl.get_article_main_title(citation=citation)
            return article_main_title
        else:
            return None

    def get_article_sub_title(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            article_sub_title = self.citation_impl.get_article_sub_title(citation=citation)
            return article_sub_title
        else:
            return None

    def get_journal_title(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            journal_title = self.citation_impl.get_journal_title(citation=citation)
            return journal_title
        else:
            return None

    def get_volume(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            volume = self.citation_impl.get_volume(citation=citation)
            return volume
        else:
            return None

    def get_issue(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            issue = self.citation_impl.get_issue(citation=citation)
            return issue
        else:
            return None

    def get_pages(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            pages = self.citation_impl.get_pages(citation=citation)
            return pages
        else:
            return None

    def get_doi(self, *, citation: str) -> str or None:
        citation_type = self.get_citation_type(citation=citation)
        if citation_type is None:
            return None
        self.citation_impl = citation_type.value()
        if self.citation_impl is not None:
            doi = self.citation_impl.get_doi(citation=citation)
            return doi
        else:
            return None

    def get_citation_type(self, *, citation: str):
        for type in CitationType:
            # FIX: add
            if True:
                self.print_citation_type(type)
                return type
        print('getMatchJournalURL(): no match journal')
        return None

    def print_citation_type(self, type: CitationType):
        type_str = ''
        if type == CitationType.APA:
            type_str = 'APA'

        print('Citation format: {0}'.format(type_str))

    def __decision_include_keyword(self, *, keyword: str, text: str) -> bool:
        """[text]から[keywordを検索] -> Bool """
        if keyword == '':
            return False
        # print(searchWord in text)
        return keyword in text

# ======================================================================================================================

