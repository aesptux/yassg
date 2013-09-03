#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Create the site

Usage:
  yassg startsite|build
  yassg (-h | --help)

Arguments
  <startsite> Command to create the new site
  <build> Build your site

Options:
  -h --help     Show this screen.

"""

import logging
from docopt import docopt
from ..utils import asker, common
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main(arguments):
    if arguments['startsite']:
        config = asker.asker()
        common.init_site_folder(config)
        logger.info('Please review the config file for more information.')
    elif arguments['build']:
        pass  # build site



if __name__ == '__main__':
    arguments = docopt(__doc__, version='yassg')
    main(arguments)


