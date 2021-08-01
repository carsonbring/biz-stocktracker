#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utility functions."""

import re

# HTML parser was renamed in python 3.x
import sys
if sys.version_info[0] >= 3:
    import html
else:
    from six.moves import html_parser
    html = html_parser.HTMLParser()
_parser = html


def clean_comment_body(body):
    """Returns given comment HTML as plaintext.

    Converts all HTML tags and entities within 4chan comments
    into human-readable text equivalents.
    """
    body = _parser.unescape(body)
    body = re.sub(r'<a [^>]+>(.+?)</a>', r'\1', body)
    body = body.replace('<br>', '\n')
    body = re.sub(r'<.+?>', '', body)
    return body
