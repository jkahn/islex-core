#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_load_strings
----------------------------------

Tests for `islex.data.core` module.
"""

from six import next
import pytest

import islex.tokens
from islex.data.core import entries_stream

class TestIsleCore(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_get_one(self):
        entries = entries_stream()
        e = next(entries)
        assert isinstance(e, islex.tokens.Word)

    @classmethod
    def teardown_class(cls):
        pass
