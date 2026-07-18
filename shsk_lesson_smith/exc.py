# -*- coding: utf-8 -*-

"""Exception types for lesson-smith.

The lint layer is built out of many tiny check functions. Each one either
returns quietly (the rule holds) or raises :class:`LintError` carrying a
friendly, human-readable message that says exactly what is wrong.

The higher-level linter runs the checks one after another and catches
:class:`LintError` around each, so a single failing check is recorded as one
result and never aborts the whole run.
"""


class LessonSmithError(Exception):
    """Base class for every error this package raises on purpose."""


class LintError(LessonSmithError):
    """A single lint rule was violated.

    The string message is meant to be shown verbatim to a human (the course
    creator) in the lint result list, so write it as a complete, friendly
    sentence that explains the problem and, where useful, how to fix it.
    """
