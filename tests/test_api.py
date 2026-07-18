# -*- coding: utf-8 -*-

from shsk_lesson_smith import api


def test():
    _ = api


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.api",
        preview=False,
    )
