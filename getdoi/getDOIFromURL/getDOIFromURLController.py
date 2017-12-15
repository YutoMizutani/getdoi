#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ============================================================================================================

"""
 getDOIFromURLController.py

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
"""
http://a-clinical-psychologist.blogspot.jp/2014/11/doi.html
http://current.ndl.go.jp/node/18820
https://www.crossref.org/display-guidelines/
https://ja.wikipedia.org/wiki/%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E8%AD%98%E5%88%A5%E5%AD%90
"""
# --- notes ---
# --- Information ---
# --- Circumstances ---

# === import ===========================================================================================================

""" Standard library """
from enum import Enum
""" Third party library """
""" Local library """
from .gettableDOI import GettableDOI
from .sciencedirect import ScienceDirect
from .wiley import Wiley
from .springer import Springer
from .psycnet import PsycNET
from .plos import PLOS
from .pmc import PMC

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================

# === variables ========================================================================================================

# ======================================================================================================================


class JournalType(Enum):
    SCIENCEDIRECT = ScienceDirect
    WILEY = Wiley
    SPRINGER = Springer
    APA = PsycNET
    PLOS = PLOS
    PMC = PMC


class GetDOIFromURLControllerImpl(GettableDOI):
    # -- variables --
    journal_impl = GettableDOI

    # -- controller --
    def get(self, *, url: str)->str or None:
        journal_type = self.get_journal_type(url=url)
        if journal_type is None:
            return None
        self.journal_impl = journal_type.value()
        if self.journal_impl is not None:
            doi = self.journal_impl.get(url=url)
            return doi
        else:
            return None

    def get_url(self, *, url: str)->str or None:
        """return a full URL link"""
        journal_type = self.get_journal_type(url=url)
        if journal_type is None:
            return None
        self.journal_impl = journal_type.value()
        if self.journal_impl is not None:
            doi = self.journal_impl.get_url(url=url)
            return doi
        else:
            return None

    def get_prev_format(self, *, url: str)->str or None:
        """doi：[space] [doinumber]"""
        journal_type = self.get_journal_type(url=url)
        if journal_type is None:
            return None
        self.journal_impl = journal_type.value()
        if self.journal_impl is not None:
            doi = self.journal_impl.get_prev_format(url=url)
            return doi
        else:
            return None

    def get_journal_type(self, *, url: str):
        for type in JournalType:
            base_url = self.__get_url_from_url_type(type)
            # __get_url_from_url_type()がNoneなら次に進む。
            if base_url is None:
                continue
            if self.__decision_include_keyword(keyword=base_url, text=url):
                print('Journal site: {0}'.format(self.__get_type_str(type)))
                return type
        print('getMatchJournalURL(): no match journal')
        return None

    def __get_url_from_url_type(self, url_type=JournalType)->str or None:
        if url_type in {JournalType.SCIENCEDIRECT}:
            return "/www.sciencedirect.com/"
        elif url_type in {JournalType.WILEY}:
            return "/onlinelibrary.wiley.com/"
        elif url_type in {JournalType.SPRINGER}:
            return "/link.springer.com/"
        elif url_type in {JournalType.APA}:
            return "/psycnet.apa.org/"
        elif url_type in {JournalType.PLOS}:
            return "/journals.plos.org/"
        elif url_type in {JournalType.PMC}:
            return '/www.ncbi.nlm.nih.gov/pmc/'
        else:
            return None

    def __get_type_str(self, url_type=JournalType)->str:
        if url_type in {JournalType.SCIENCEDIRECT}:
            return "ScienceDirect"
        elif url_type in {JournalType.WILEY}:
            return "Wiley"
        elif url_type in {JournalType.SPRINGER}:
            return "Springer"
        elif url_type in {JournalType.APA}:
            return "APA"
        elif url_type in {JournalType.PLOS}:
            return "PLOS"
        elif url_type in {JournalType.PMC}:
            return 'PMC'
        else:
            return ''

    def __decision_include_keyword(self, *, keyword: str, text: str)->bool:
        """[text]から[keywordを検索] -> Bool """
        if keyword == '':
            return False
        # print(searchWord in text)
        return keyword in text

# ======================================================================================================================
