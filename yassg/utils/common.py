#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import logging
from collections import OrderedDict

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_theme(themes_folder, active_theme):
    pass


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