#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ============================================================================================================

"""
 test_science.py

Copyright © 2017 Yuto Mizutani.
This software is released under the MIT License.

Version: 1.0.0

TranslateAuthors: Yuto Mizutani
E-mail: yuto.mizutani.dev@gmail.com
Website: http://operantroom.com

Created: 2017/12/21
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
from getdoi.getDOIFromURL.science import Science

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================

# === variables ========================================================================================================

# ======================================================================================================================


class TestScience(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('class TestScience(unittest.TestCase):')
        print('def setUpClass(cls):')

    @classmethod
    def tearDownClass(cls):
        print('def tearDownClass(cls):')

    def setUp(self):
        print('def setUp(self):')
        self.getter = Science()

    def tearDown(self):
        print('def tearDown(self):')

    def test_get_url(self):
        print('def test_get_url(self):')
        url = 'http://science.sciencemag.org/content/309/5732/310'
        doi = 'https://doi.org/10.1126/science.1114519'
        result = self.getter.get_url(url=url)
        print('URL: {0}'.format(url))
        print('DOI: {0}'.format(result))
        self.assertEqual(result, doi)

    def test_get_prev_format(self):
        print('def test_get_prev_format(self):')
        url = 'http://science.sciencemag.org/content/309/5732/310'
        doi = 'doi: 10.1126/science.1114519'
        result = self.getter.get_prev_format(url=url)
        print('URL: {0}'.format(url))
        print('DOI: {0}'.format(result))
        self.assertEqual(result, doi)

# ======================================================================================================================


if __name__ == '__main__':
    unittest.main()
