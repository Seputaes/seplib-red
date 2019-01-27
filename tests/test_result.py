from seplib.tests.utils.strings import random_string
from seplib.utils import Result


class TestResult(object):
    def test_get_result_true_check(self):
        def check():
            return True

        result = Result.get_result(check=check, error="")
        assert result.success is True

    def test_get_result_true_error_message(self):
        def check():
            return True

        result = Result.get_result(check=check, error="This should be None in the result.")
        assert result.error is None

    def test_get_result_false_check(self):
        def check():
            return False

        result = Result.get_result(check=check, error="")
        assert result.success is False

    def test_get_result_false_error_message(self):
        def check():
            return False

        error_msg = random_string()
        result = Result.get_result(check=check, error=error_msg)
        assert result.error == error_msg

    def test_get_result_does_not_catch_exception(self):
        class NewBaseException(BaseException):
            pass

        error_msg = random_string()

        def check():
            raise NewBaseException(error_msg)

        try:
            Result.get_result(check=check(), error=error_msg)
            assert False, "Exception was caught in Result"
        except BaseException as e:
            assert type(e) == NewBaseException
            assert e.args[0] == error_msg
