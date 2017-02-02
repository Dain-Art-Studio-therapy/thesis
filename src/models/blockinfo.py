# File name: blockinfo.py
# Author: Nupur Garg
# Date created: 2/1/2017
# Python Version: 3.5


from src.globals import *


class BlockInformation(ABC):
    """
    Abstract class containing BlockInformation.
    """

    def __init__(self):
        self.gen = {}
        self.kill = {}

    def __ne__(self, other):
        return not self == other

    @abstractmethod
    def __eq__(self, other):
        pass

    # Finds dictA DIFF dictB for the common keys.
    @staticmethod
    def diff_common_keys(dictA, dictB):
        result = {}
        for key, valueset in dictA.items():
            if key in dictB:
                result[key] = valueset.symmetric_difference(dictB[key])
        return result

    # Finds diffA - diffB.
    @staticmethod
    def sub(dictA, dictB):
        result = {}
        for key, valueset in dictA.items():
            result[key] = valueset
            if key in dictB:
                result[key] = valueset - dictB[key]
        return result

    # Finds dictA UNION dictB.
    @staticmethod
    def union(dictA, dictB):
        result = {}
        keys = set().union(*[dictA, dictB])
        for key in keys:
            result[key] = set()
            if key in dictA:
                result[key] = result[key].union(dictA[key])
            if key in dictB:
                result[key] = result[key].union(dictB[key])
        return result


class ReachingDefinitions(BlockInformation):
    """
    Reaching definitions for a block.
    """

    def __init__(self):
        super(self.__class__, self).__init__()
        self.in_block = {}
        self.out_block = {}

    def _is_dict_equal(self, dictA, dictB):
        if dictA.keys() != dictB.keys():
            return False

        for key in dictA.keys():
            if dictA[key] != dictB[key]:
                return False
        return True

    def __eq__(self, other):
        if other is None or type(other) != type(self):
            return False

        return (self._is_dict_equal(self.gen, other.gen) and
                self._is_dict_equal(self.kill, other.kill) and
                self._is_dict_equal(self.in_block, other.in_block) and
                self._is_dict_equal(self.out_block, other.out_block))


class FunctionBlockInformation(object):
    """
    Information for a function block.

    func_block: obj
        FunctionBlock object.
    block_info_class: obj
        BlockInformation class.
    """

    def __init__(self):
        self._blocks = None
        self._block_info = None
        self._block_info_class = None

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        if other is None or type(other) != type(self):
            return False

        if (type(other._block_info_class) != type(other._block_info_class) or
            len(other._blocks) != len(other._blocks) or
            other._block_info.keys() != other._block_info.keys()):
            return False

        for block, block_info in self.items():
            if block_info != other.get_block_info(block):
                return False

        return True

    # Initializes FunctionBlockInformation.
    def init(self, func_block, block_info_class):
        assert issubclass(type(block_info_class()), BlockInformation)

        self._blocks = []
        self._block_info = {}
        self._block_info_class = block_info_class

        for block in func_block.get_sorted_blocks():
            self._blocks.append(block)
            self._block_info[block.label] = block_info_class()

    # Returns ordered list of (Block, BlockInformation) tuples.
    def items(self):
        return [(block, self._block_info[block.label])
                for block in self._blocks]

    # Returns BlockInformation for a given Block.
    def get_block_info(self, block):
        return self._block_info[block.label]
