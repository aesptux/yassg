#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yassg.core.settings import CONFIG
from yassg import __version__


def question(q, default=''):
    """
    Receives a question and a default value.
    Returns an answer

    :param q: question text
    :param default: default value
    """
    answer = raw_input("➜  {0} [{1}] ".format(q, default))

    if answer:
        return answer
    else:
        return default


def asker():
    """
    Asks several questions to configure the site.
    Returns a CONFIG dict.
    """
    print "Thanks for using yassg {version}.\n\n\n Please, " \
          "answer the following " \
          "questions"\
          "to configure your site.".format(version=__version__)
    CONFIG['AUTHOR_NAME'] = question('What is the author\'s name?',
                                    CONFIG['AUTHOR_NAME'])
    CONFIG['AUTHOR_EMAIL'] = question('Do you mind if I ask you for the '
                                      'author\'s email?',
                                      CONFIG['AUTHOR_EMAIL'])
    CONFIG['SITE_DESCRIPTION'] = question('What will be the site '
                                          'description?',
                                          CONFIG['SITE_DESCRIPTION'])
    CONFIG['SITE_NAME'] = question('What will be the site name?',
                                   CONFIG['SITE_NAME'])
    CONFIG['SITE_URL'] = question('What will be the site url?',
                                  CONFIG['SITE_URL'])
    CONFIG['PATH'] = question('Where do you want to store the site files?',
                              CONFIG['PATH'])

    return CONFIG


if __name__ == '__main__':
    asker()