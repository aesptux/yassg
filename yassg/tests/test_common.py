#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_yassg
----------------------------------

Tests for `yassg` module.
"""

import unittest
import os
import shutil
from yassg.utils import common
from yassg.core.settings import CONFIG
from yassg.core.exceptions import ThemeNotFound


class TestYassg(unittest.TestCase):

    def setUp(self):
        pass

    # def test_create_site_folder_default(self):
    #     common.init_site_folder(CONFIG)
    #     self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
    #                                                CONFIG['CONTENT_FOLDER'])))
    #     self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
    #                                                CONFIG['PAGES_FOLDER'])))
    #     self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
    #                                                CONFIG['THEME_FOLDER'])))
    #     self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
    #                                                CONFIG['OUTPUT_FOLDER'])))

    def test_create_site_folder_custom(self):
        CONFIG['PATH'] = 'sample'
        common.init_site_folder(CONFIG)
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['CONTENT_FOLDER'])))
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['PAGES_FOLDER'])))
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['THEME_FOLDER'])))
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['OUTPUT_FOLDER'])))

    def test_get_theme(self):
        CONFIG['PATH'] = 'sample'
        common.get_theme(CONFIG['PATH'], CONFIG['THEME_FOLDER'],
                         CONFIG['SITE_THEME'])

        path_to_theme = os.path.join(CONFIG['PATH'],
                                     CONFIG['THEME_FOLDER'])
        # self.assertTrue(os.path.isdir(path_to_theme))
        # self.assertGreater(len(os.listdir(path_to_theme)) > 0, msg=None)
        self.assertTrue(os.listdir(path_to_theme))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()