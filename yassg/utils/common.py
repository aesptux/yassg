#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import logging
from collections import OrderedDict
import shutil
import distutils.core
from yassg.core.exceptions import ThemeNotFound


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_theme(path, themes_folder, active_theme):
    logger.info('Setting theme')
    # print os.path.dirname(os.path.join(os.path.abspath(__file__), os.pardir))
    content_path = os.path.dirname(os.path.abspath(os.path.join(__file__,
                                                         os.pardir)))
    destination_path = os.path.abspath(os.path.join(path, themes_folder))
    if active_theme not in os.listdir(os.path.join(content_path, 'themes')):
        raise ThemeNotFound("Theme was not found on the folder, "
                            "please check your settings.")
    else:
        # shutil.copytree(os.path.join(content_path, 'themes', active_theme),
        #                 destination_path)
        distutils.dir_util.copy_tree(os.path.join(content_path, 'themes',
                                                  active_theme, 'assets'),
                                     destination_path)


def init_site_folder(config):
    logger.info('Creating structure')
    logger.info('Path is {0}'.format(config['PATH']))
    if config['PATH'] != '.':
        if not os.path.isdir(config['PATH']):
            logger.info('Creating path')
            os.mkdir(config['PATH'])
    try:
        os.mkdir(os.path.join(config['PATH'], config['CONTENT_FOLDER']))
        os.mkdir(os.path.join(config['PATH'], config['PAGES_FOLDER']))
        os.mkdir(os.path.join(config['PATH'], config['THEMES_FOLDER']))
        os.mkdir(os.path.join(config['PATH'], config['OUTPUT_FOLDER']))
    except OSError:
        logger.error("Folders already exist, please use an empty folder.")
    config_file = open(os.path.join(config['PATH'], config['CONFIG_NAME']),
                       'w')
    config_file.write(json.dumps(OrderedDict(sorted(config.items())),
                                 indent=2))
    config_file.close()



# def slugify(value):
#     """
#     Converts to lowercase, removes non-word characters (alphanumerics and
#     underscores) and converts spaces to hyphens. Also strips leading and
#     trailing whitespace.
#     """
#     value = unicodedata.normalize('NFKD', value). \
#         encode('ascii', 'ignore').decode('ascii')
#     value = re.sub('[^\w\s-]', '', value).strip().lower()
#     return re.sub('[-\s]+', '-', value)