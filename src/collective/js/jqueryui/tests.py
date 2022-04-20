# -*- coding: utf-8 -*-
import doctest
import unittest


def test_suite():
    return unittest.TestSuite((doctest.DocTestSuite("collective.js.jqueryui.utils"),))
