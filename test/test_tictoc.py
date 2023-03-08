import time
import io
import sys
from unittest import TestCase
import unittest.mock
import tictoc as tt


class TestTicToc(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, tic, expected_output, mock_stdout):
        tic.toc()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_toc(self):
        # Testing with short time. Todo: add test for longer times to make sure output is correct
        tic = tt.TicToc()
        time.sleep(2)
        self.assert_stdout(tic, "Execution time: 00:00:02\n")
