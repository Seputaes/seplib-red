from typing import Callable, NamedTuple, Optional


class Result(NamedTuple):
    success: bool
    error: Optional[str]

    @staticmethod
    def get_result(check: Callable[[], bool], error: str) -> "Result":
        """
        Build an appropriate Result object using the supplied Callable method and error message.

        The callable should return a type bool. If the result evaluates to false,
        the message Result's error will be set to the supplied error. If it evaluates to true,
        error will be set to none.

        :param check: Callable which returns type bool.
        :param error: Error message to be set to the result error if success is false.
        :return: Built Result object.
        """
        if check():
            return Result(success=True, error=None)
        return Result(success=False, error=error)
