# -*- coding: utf-8 -*-

from islex.load import stream_from_fh
from pkg_resources import resource_stream

__author__ = 'Jeremy G. Kahn'
__email__ = 'jeremy@trochee.net'
__version__ = '0.1.1'

def entries_stream():
    """Get an iterator over the entries. Useful for building a dictionary.

    :returns: iterator over `islex.token.Word` objects.
    """
    return stream_from_fh(resource_stream(__name__, 'entries.txt'))
