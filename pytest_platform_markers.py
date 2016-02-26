# -*- coding: utf-8 -*-

import os
import sys

import pytest


MARKERS = [
    ('posix', "os.name != 'posix'", "Requires a POSIX os"),
    ('windows', "os.name != 'nt'", "Requires Windows"),
    ('linux', "not sys.platform.startswith('linux')", "Requires Linux"),
    ('osx', "sys.platform != 'darwin'", "Requires OS X"),
    ('not_osx', "sys.platform == 'darwin'", "Skipped on OS X"),
    ('not_frozen', "getattr(sys, 'frozen', False)",
        "Can't be run when frozen"),
    ('frozen', "not getattr(sys, 'frozen', False)",
        "Can only run when frozen"),
    ('ci', "'CI' not in os.environ", "Only runs on CI"),
    ('not_ci', "'CI' in os.environ", "Skipped on CI"),
]


def pytest_configure(config):
    for marker, _, reason in MARKERS:
        config.addinivalue_line("markers", "{}: {}".format(marker, reason))


def pytest_collection_modifyitems(items):
    for item in items:
        for searched_marker, condition, default_reason in MARKERS:
            marker = item.get_marker(searched_marker)
            if not marker:
                continue

            if 'reason' in marker.kwargs:
                reason = '{}: {}'.format(default_reason,
                                         marker.kwargs['reason'])
            else:
                reason = default_reason + '.'
            skipif_marker = pytest.mark.skipif(condition, reason=reason)
            item.add_marker(skipif_marker)
