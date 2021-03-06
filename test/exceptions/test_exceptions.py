import unittest
import traceback
from coursera_python.exceptions.ManagingFailure import *


class ManagingFailureTests(unittest.TestCase):

    def test_00_basic_try_except_finally_none_failing(self):
        try:
            print('test_00_basic_try_except_finally_none_failing TRY')
            n = int('0')
            print(n)
        except:
            print('test_00_basic_try_except_finally_none_failing EXCEPT')
        finally:
            print('test_00_basic_try_except_finally_none_failing FINALLY')

        print('test_00_basic_try_except_finally_none_failing SUCCESS')


    def test_01_basic_try_except_finally_none_failing_else(self):
        try:
            print('test_01_basic_try_except_finally_none_failing_else TRY')
        except:
            print('test_01_basic_try_except_finally_none_failing_else EXCEPT')
        else:
            print('test_01_basic_try_except_finally_none_failing_else ELSE')
            n = int('0')
            print(n)
        finally:
            print('test_01_basic_try_except_finally_none_failing_else FINALLY')

        print('test_01_basic_try_except_finally_none_failing_else SUCCESS')


    def test_02_basic_try_except_finally(self):
        try:
            print('test_02_basic_try_except_finally TRY')
            AlwaysRaisesException(0)
        except:
            print('test_02_basic_try_except_finally EXCEPT')
        finally:
            print('test_2_basic_try_except_finally FINALLY')


    def test_03_basic_try_except_multi(self):
        try:
            print('test_03_basic_try_except_multi TRY')
            MultiCatch(AlwaysRaisesException, '0')
        except:
            print('test_03_basic_try_except_multi EXCEPT')
        finally:
            print('test_03_basic_try_except_multi FINALLY')


    def test_04_basic_try_except_multi_bbbexception(self):
        try:
            print('test_04_basic_try_except_multi TRY')
            MultiCatch(AlwaysRaiseBbbException, '0')
        except:
            print('test_04_basic_try_except_multi EXCEPT')
        finally:
            print('test_04_basic_try_except_multi FINALLY')


    def test_05_basic_try_except_inline(self):
        try:
            print('test_05_basic_try_except_inline TRY')
            MultiCatchInline(AlwaysRaisesException, '0')
        except:
            print('test_05_basic_try_except_inline EXCEPT')
        finally:
            print('test_05_basic_try_except_inline FINALLY')


    def test_06_basic_try_except_inline_bbbexception(self):
        try:
            print('test_06_basic_try_except_inline TRY')
            MultiCatchInline(AlwaysRaiseBbbException, '0')
        except:
            print('test_06_basic_try_except_inline EXCEPT')
        finally:
            print('test_06_basic_try_except_inline FINALLY')


    def test_07_swallowing_an_exception(self):
        try:
            AlwaysRaisesException(0)
        except:
            pass


    def test_08_printing_an_exception(self):
        try:
            AlwaysRaisesException(0)
        except:
            print('test_08_printing_an_exception EXCEPT')
            traceback.print_exc()


    def test_09_printing_a_reraised_exception(self):
        try:
            CatchAndRaise(AlwaysRaisesException,0)
        except:
            print('test_09_printing_a_reraised_exception EXCEPT')
            traceback.print_exc()


    def test_10_printing_a_new_exception(self):
        try:
            CatchAndRaiseNew(AlwaysRaisesException,0)
        except:
            print('test_10_printing_a_new_exception EXCEPT')
            traceback.print_exc()

    def test_11_printing_a_bad_int_exception(self):
        try:
            RaiseExceptionOnBadInt('This is not an int')
        except:
            print('test_11_printing_a_bad_int_exception EXCEPT')
            traceback.print_exc()


if __name__ == '__main__':
    unittest.main()
