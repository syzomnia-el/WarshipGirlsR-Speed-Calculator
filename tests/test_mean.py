#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import contextlib
import io
import sys
from unittest import TestCase
from unittest.mock import patch

from mean import main


# noinspection PyUnresolvedReferences
class TestMain(TestCase):
    @patch.object(sys, 'argv', ['mean.py'])
    def test_no_arg(self):
        # noinspection GrazieInspection
        prompt = """Calculate the `Combat Speed` of the fleet.

Provide one or two groups of speeds, separate groups with spaces ` ` and numbers with commas `,`.
For example,
    >>> mean 34,39,36 35,36
    35

In this case, `34,39,36` is the first group, and `35,36` is the second. \n"""
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            main()
            output = buf.getvalue()
        self.assertEqual(prompt, output, msg='If no argument, print the prompt.')

    @patch.object(sys, 'argv', ['mean.py', '34,39,36'])
    def test_one_group(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            main()
            output = buf.getvalue()
        self.assertEqual('36.33\n', output, msg='If one group, calculate the mean of the group.')

    @patch.object(sys, 'argv', ['mean.py', '34,39,36', '35,36'])
    def test_two_groups(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            main()
            output = buf.getvalue()
        self.assertEqual('35\n', output, msg='If two groups, calculate the minimum mean of the two groups.')

    @patch.object(sys, 'argv', ['mean.py', '34,', '39,', '36'])
    def test_too_many_args(self):
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            with self.assertRaisesRegex(SystemExit, '2', msg='If too many arguments, exit with code 2.'):
                main()
            output = buf.getvalue()
        self.assertEqual("TypeError: too many arguments, required 0, 1 or 2 but got 3: ['34,', '39,', '36']\n",
                         output,
                         msg='If more than two groups, raise a TypeError')

    @patch.object(sys, 'argv', ['mean.py', 'sss'])
    def test_not_numeric(self) -> None:
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            with self.assertRaisesRegex(SystemExit, '5', msg='If the input is not numeric, exit with code 5.'):
                main()
            output = buf.getvalue()
        self.assertEqual("ValueError: could not convert string to float: 'sss'\n", output,
                         msg='If the input is not numeric, raise a ValueError')
