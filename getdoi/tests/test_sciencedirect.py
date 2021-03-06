#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ============================================================================================================

"""
 test_sciencedirect.py

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
import unittest
""" Third party library """
""" Local library """
from getdoi.getDOIFromURL.sciencedirect import ScienceDirect

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================

# === variables ========================================================================================================

# ======================================================================================================================


class TestScienceDirect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('class TestScienceDirect(unittest.TestCase):')
        print('def setUpClass(cls):')

    @classmethod
    def tearDownClass(cls):
        print('def tearDownClass(cls):')

    def setUp(self):
        print('def setUp(self):')
        self.getter = ScienceDirect()

    def tearDown(self):
        print('def tearDown(self):')

    def test_get_url(self):
        print('def test_get_url(self):')
        url = 'http://www.sciencedirect.com/science/article/pii/104084289390007Q'
        doi = 'https://doi.org/10.1016/1040-8428(93)90007-Q'
        result = self.getter.get_url(url=url)
        print('URL: {0}'.format(url))
        print('DOI: {0}'.format(result))
        self.assertEqual(result, doi)

    def test_get_prev_format(self):
        print('def test_get_prev_format(self):')
        url = 'http://www.sciencedirect.com/science/article/pii/104084289390007Q'
        doi = 'doi: 10.1016/1040-8428(93)90007-Q'
        result = self.getter.get_prev_format(url=url)
        print('URL: {0}'.format(url))
        print('DOI: {0}'.format(result))
        self.assertEqual(result, doi)

# ======================================================================================================================


if __name__ == '__main__':
    unittest.main()
