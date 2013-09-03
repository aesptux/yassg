#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_yassg
----------------------------------

Tests for `yassg` module.
"""

import unittest
import os
from yassg.utils import common
from yassg.core.settings import CONFIG


class TestYassg(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_site_folder_default(self):
        common.init_site_folder(CONFIG)
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['CONTENT_FOLDER'])))
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['PAGES_FOLDER'])))
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['THEMES_FOLDER'])))
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['OUTPUT_FOLDER'])))

    def test_create_site_folder_custom(self):
        CONFIG['PATH'] = 'sample'
        common.init_site_folder(CONFIG)
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['CONTENT_FOLDER'])))
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['PAGES_FOLDER'])))
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['THEMES_FOLDER'])))
        self.assertTrue(os.path.isdir(os.path.join(CONFIG['PATH'],
                                                   CONFIG['OUTPUT_FOLDER'])))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()