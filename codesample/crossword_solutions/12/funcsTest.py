import unittest
from funcs import *



class TestCases1(unittest.TestCase):

    def setUp(self):
        self.puzzle = ['WAQHGTTWZE',
                       'CBNSZQQELS',
                       'AZXWKWIIML',
                       'LDWLFXXSAV',
                       'PONDTMVUXN',
                       'OEDSDYQPOB',
                       'LGQCKGMMIT',
                       'YCSLOACAZM',
                       'XVDMGSXCYZ',
                       'UUIUNIXFNU']
    
    def test_make_puzzle_1(self):
        text = ('WAQHGTTWZECBNSZQQELSAZXWKWIIMLLDWLFXXSAVPONDTMVUXN'
                'OEDSDYQPOBLGQCKGMMITYCSLOACAZMXVDMGSXCYZUUIUNIXFNU')
        self.assertEqual(make_puzzle(text), self.puzzle)
  
    def test_make_words_1(self):
        text = ('SLACK HIGH HIGHLAND CHORRO PEACH BROAD GRAND OSOS '
                'MORRO HIGUERA MARSH FOOTHILL NIPIMO MILL PALM')
        words = ['SLACK', 'HIGH', 'HIGHLAND', 'CHORRO', 'PEACH', 'BROAD',
                 'GRAND', 'OSOS', 'MORRO', 'HIGUERA', 'MARSH', 'FOOTHILL',
                 'NIPIMO', 'MILL', 'PALM']
        self.assertEqual(make_words(text), words)

    def test_make_words_2(self):
        text = 'CAT DOG MOUSE HOUSE FROG'
        words = ['CAT', 'DOG', 'MOUSE', 'HOUSE', 'FROG']
        self.assertEqual(make_words(text), words)

    def test_rows_1(self):
        self.assertEqual(check_rows(self.puzzle, 'SLO'), ['(FORWARD)', 7, 2])

    def test_rows_2(self):
        self.assertEqual(check_rows(self.puzzle, 'OLS'), ['(BACKWARD)', 7, 4])

    def test_rows_3(self):
        self.assertEqual(check_rows(self.puzzle, 'TIM'), ['(BACKWARD)', 6, 9])

    def test_rows_4(self):
        self.assertEqual(check_rows(self.puzzle, 'FROG'), None)

    def test_cols_1(self):
        self.assertEqual(check_cols(self.puzzle,'CALPOLY'), ['(DOWN)', 1, 0])

    def test_cols_2(self):
        self.assertEqual(check_cols(self.puzzle, 'CAMPUS'), ['(UP)', 8, 7])

    def test_cols_3(self):
        self.assertEqual(check_cols(self.puzzle, 'FROG'), None)


if __name__ == '__main__':
    unittest.main()
