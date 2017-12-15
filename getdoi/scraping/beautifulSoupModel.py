#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ============================================================================================================

"""
 readEnteredText.py

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
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
""" Local library """

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================

# === variables ========================================================================================================

# ======================================================================================================================


class BeautifulSoupModelImpl:
    #### Controller
    def get_html(self, url):
        try:
            request = self.__translate_disguised_request(url)
            response = urllib.request.urlopen(request)
            return response
        except urllib.error.URLError as e:
            print(e.reason)
            return None

    def get_anchors(self, url):
        html = self.get_html(url)
        if html is None:
            return None
        else:
            soup = self.__translate_beautiful_soup(html=html)
            return self.__find_anchor(soup=soup)

    def get_anchor_links(self, url):
        anchor = self.get_anchors(url)
        if anchor is None:
            return None
        else:
            return self.__find_href_link(anchor=anchor)
        
    def get_anchor_texts(self, url):
        anchor = self.get_anchors(url)
        if anchor is None:
            return None
        else:
            return self.__find_href_text(anchor=anchor)

    def get_anchor_texts_and_links(self, url):
        anchor = self.get_anchors(url)
        if anchor is None:
            return None
        else:
            return self.__find_href_texts_and_links(anchor=anchor)





    def find_loop_from_array(self, span, keyword):
        # print('start loop!')
        count = 1
        for tag in span:
            # print(count)
            # print(tag)
            count += 1
            raw_text = tag.string
            # print(f'raw: {raw_text}')
            if self.__decision_include_keyword(keyword=keyword, text=raw_text):
                print('指定された単語の存在を確認！')
                print(f'発見された単語({count}番目): {raw_text}')
                return raw_text
        return ''

    def sraiping_using_bautiful_soup_4(self, url, class_name, keyword):
        result = self.find_loop_from_array(
            self.__find_class(
                class_name,
                soup=self.__translate_beautiful_soup(html=self.get_html(url=url))
            ),
            keyword
        )
        if result != '':
            result_text = f'指定された単語の存在を確認しました！: {result}'
        else:
            result_text = '指定された単語の存在は認められませんでした。'
        print(result_text)
        return result

    #### Translator
    def __translate_beautiful_soup(self, *, html)->BeautifulSoup:
        # htmlをBeautifulSoupで扱う
        return BeautifulSoup(html, 'html.parser')

    #### Model
    def __translate_disguised_request(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
            # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        }
        request = urllib.request.Request(url=url, headers=headers)
        return request

    def __find_anchor(self, *, soup=BeautifulSoup):
        anchor = soup.find_all('a')
        return anchor

    def __find_href_text(self, *, anchor):
        links = []
        for link in anchor:
            if 'href' in link.attrs:
                # print(link.text, ':', link.attrs['href'])
                links.append(link.text)
        return links

    def __find_href_link(self, *, anchor):
        links = []
        for link in anchor:
            if 'href' in link.attrs:
                # print(link.text, ':', link.attrs['href'])
                links.append(link.attrs['href'])
        return links

    def __find_href_texts_and_links(self, *, anchor):
        links = []
        for link in anchor:
            if 'href' in link.attrs:
                # print(link.text, ':', link.attrs['href'])
                links.append([link.text, link.attrs['href']])
        return links

    def __find_class(self, class_name, *, soup):
        # span要素全てを摘出する→全てのspan要素が配列に入ってかえされます→[<span class="m-wficon triDown"></span>, <span class="l-h...
        span = soup.find_all(class_=class_name)  # soup.find_all('a')
        # print('get span!')
        # print(span)
        return span

    def __decision_include_keyword(self, *, keyword: str, text: str):
        """[text]から[keywordを検索] -> Bool """
        if keyword == '':
            return False
        # print(searchWord in text)
        return keyword in text

# =============================================================================================================


class ReadEnteredTextStandAloneImpl:
    """ If user display_input, drop filesPath then return files, exit then return None """
    # -- variables --
    __display_input_instructions = 'Enter the characters...'
    __display_input_text = '> '
    __display_output_text = '>> Read: '

    # reader = ReadEnteredTextStandAloneImpl()
    # while True:
    #     text = reader.read()
    #     if text is None:
    #         # exit
    #         break

    def read(self)->str or None:
        print(self.__display_input_instructions)
        entered_str = input(self.__display_input_text)
        if self.__decision_exit(entered_str):
            # if user display_inputs exit meaning then exit
            return None
        else:
            print('{0}{1}'.format(self.__display_output_text, entered_str))
            return entered_str

    def __decision_exit(self, text: str)->bool:
        # -- constants --
        EXIT_TEXTS = ['e', '-e', 'exit', 'exit()', 'Exit', 'Exit()']
        # decision match strings argument and EXIT_TEXTS
        for exit_text in EXIT_TEXTS:
            if text == exit_text:
                return True
        return False

# =============================================================================================================


if __name__ == '__main__':
    print('-STAND ALONE MODE- beautifulSoupModel.py')
    print('Display the anchor text for your entered link.')
    # get link text
    soup = BeautifulSoupModelImpl()
    reader = ReadEnteredTextStandAloneImpl()
    while True:
        print()
        text = reader.read()
        if text is None:
            # exit
            break
        else:
            url = text  # 'https://news.yahoo.co.jp/list/'
            anchors = soup.get_anchor_texts(url)
            print(anchors)
