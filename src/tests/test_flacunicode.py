# -*- coding: utf-8 -*-
# Copyright 2011-2012 Michael Helmling
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation
#
from __future__ import absolute_import, unicode_literals
import unittest, taglib
from . import copyTestFile

class FLACUnicodeTest(unittest.TestCase):
    """A test for unicode tags in FLAC"""
    def test_unicode_value(self):
        with copyTestFile('testöü.flac') as copy_file:
            tfile = taglib.File(copy_file)
            tfile.tags["ARTIST"] = ["artøst 1", "artöst 2"]
            tfile.save()
            
            tfile = taglib.File(copy_file)
            self.assertEqual(len(tfile.tags["ARTIST"]), 2)
            self.assertEqual(tfile.tags["ARTIST"][0], "artøst 1")
            self.assertEqual(tfile.tags["ARTIST"][1], "artöst 2")
            
    def test_unicode_tag(self):
        """This failes ATM; need to rework PropertyMap stuff in taglib."""
        with copyTestFile('testöü.flac') as copy_file:
            tfile = taglib.File(copy_file)
            tfile.tags["HÄÜ"] = ["omg"]
            tfile.save()
            
            tfile = taglib.File(copy_file)
            self.assertEqual(tfile.tags["HÄÜ"], ["omg"])
        
        
if __name__ == '__main__':
    unittest.main()