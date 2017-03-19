# File name: test_blockinfo.py
# Author: Nupur Garg
# Date created: 3/16/2017
# Python Version: 3.5


import unittest

from src.globals import *
from src.models.blockinfo import *


# Test ReachingDefinitions class.
class TestReachingDefinitions(unittest.TestCase):

    def test_is_dict_equal(self):
        reachingdef = ReachingDefinitions()

        dictA = {'a': 'test'}
        dictB = {'b': 'test'}
        self.assertFalse(reachingdef._is_dict_equal(dictA, dictB))

        dictA = {'a': 'test'}
        dictB = {'a': 'test2'}
        self.assertFalse(reachingdef._is_dict_equal(dictA, dictB))

        dictA = {'a': 'test'}
        dictB = {'a': 'test'}
        self.assertTrue(reachingdef._is_dict_equal(dictA, dictB))

    def test_equality(self):
        reachingdef1 = ReachingDefinitions()
        reachingdef2 = ReachingDefinitions()
        self.assertFalse(reachingdef1 == None)
        self.assertFalse(reachingdef1 == 1)

        # Checks gen sets equality.
        reachingdef1.gen['a'] = set([('L2', 6)])
        self.assertFalse(reachingdef1 == reachingdef2)
        reachingdef2.gen['a'] = set([('L2', 6)])
        self.assertEqual(reachingdef1, reachingdef1)

        # Checks kill sets equality.
        reachingdef1.kill['a'] = set([('L2', 6)])
        self.assertFalse(reachingdef1 == reachingdef2)
        reachingdef2.kill['a'] = set([('L2', 6)])
        self.assertEqual(reachingdef1, reachingdef1)

        # Checks in_node sets equality.
        reachingdef1.in_node['a'] = set([('L2', 6)])
        self.assertFalse(reachingdef1 == reachingdef2)
        reachingdef2.in_node['a'] = set([('L2', 6)])
        self.assertEqual(reachingdef1, reachingdef1)

        # Checks out_node sets equality.
        reachingdef1.out_node['a'] = set([('L2', 6)])
        self.assertFalse(reachingdef1 == reachingdef2)
        reachingdef2.out_node['a'] = set([('L2', 6)])
        self.assertEqual(reachingdef1, reachingdef1)


# Test LiveVariables class.
class TestLiveVariables(unittest.TestCase):

    def test_equality(self):
        livevar1 = LiveVariables()
        livevar2 = LiveVariables()
        self.assertFalse(livevar1 == None)
        self.assertFalse(livevar1 == 1)

        # Checks defined set equality.
        livevar1.defined = set(['a'])
        self.assertFalse(livevar1 == livevar2)
        livevar2.defined = set(['a'])
        self.assertEqual(livevar1, livevar2)

        # Checks referenced set equality.
        livevar1.referenced = set(['a'])
        self.assertFalse(livevar1 == livevar2)
        livevar2.referenced = set(['a'])
        self.assertEqual(livevar1, livevar2)

        # Checks in_node set equality.
        livevar1.in_node = set(['a'])
        self.assertFalse(livevar1 == livevar2)
        livevar2.in_node = set(['a'])
        self.assertEqual(livevar1, livevar2)

        # Checks out_node set equality.
        livevar1.out_node = set(['a'])
        self.assertFalse(livevar1 == livevar2)
        livevar2.out_node = set(['a'])
        self.assertEqual(livevar1, livevar2)


# Test FunctionBlockInformation class.
class TestFunctionBlockInformation(unittest.TestCase):

    def test_equality(self):
        info1 = FunctionBlockInformation()
        info2 = FunctionBlockInformation()
        self.assertFalse(info1 == None)
        self.assertFalse(info1 == 1)

        self.skipTest('TODO: Implement')
        # TODO: Checks block info class equality.

        # TODO: Checks blocks equality.

        # TODO: Checks block info keys equality.

        # TODO: Checks block info values equality.

        # TODO: Checks instruction info values equality.

    def test_init(self):
        self.skipTest('TODO: Implement')
        # TODO: Checks block_info has correct keys

        # TODO: Checks instructions, instruction_info has correct keys

    def test_blocks(self):
        self.skipTest('TODO: Implement')

    def test_instructions(self):
        self.skipTest('TODO: Implement')

    def test_get_block_info(self):
        self.skipTest('TODO: Implement')

    def test_get_instruction(self):
        self.skipTest('TODO: Implement')

    def test_get_instruction_info(self):
        self.skipTest('TODO: Implement')


if __name__ == '__main__':
    unittest.main()
