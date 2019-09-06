# -*- coding: utf-8 -*-

import sys
import os

import pytest


pytest_plugins = 'pytester'


@pytest.mark.parametrize('marker, runs', [
    ('posix', os.name == 'posix'),
    ('windows', os.name == 'nt'),
    ('linux', sys.platform.startswith('linux')),
    ('osx', sys.platform == 'darwin'),
    ('not_osx', sys.platform != 'darwin'),
])
def test_os_markers(testdir, marker, runs):
    testdir.makepyfile("""
        import pytest

        @pytest.mark.{marker}
        def test_foo():
            pass
    """.format(marker=marker))

    result = testdir.runpytest()
    if runs:
        result.assert_outcomes(passed=1, skipped=0)
    else:
        result.assert_outcomes(skipped=1)


@pytest.mark.parametrize('frozen', [True, False])
def test_frozen_marker(monkeypatch, testdir, frozen):
    if frozen:
        monkeypatch.setattr(sys, 'frozen', True, raising=False)
    else:
        monkeypatch.delattr(sys, 'frozen', raising=False)

    testdir.makepyfile("""
        import pytest

        @pytest.mark.frozen
        def test_foo():
            pass
    """)

    result = testdir.runpytest()
    if frozen:
        result.assert_outcomes(passed=1, skipped=0)
    else:
        result.assert_outcomes(skipped=1)


@pytest.mark.parametrize('ci, marker, skipped', [
    (True, 'ci', False),
    (False, 'ci', True),
    (True, 'not_ci', True),
    (False, 'not_ci', False),
])
def test_ci_marker(monkeypatch, testdir, ci, marker, skipped):
    if ci:
        monkeypatch.setenv('CI', '1')
    else:
        monkeypatch.delenv('CI', raising=False)

    testdir.makepyfile("""
        import pytest

        @pytest.mark.{marker}
        def test_foo():
            pass
    """.format(marker=marker))

    result = testdir.runpytest()
    if skipped:
        result.assert_outcomes(skipped=1)
    else:
        result.assert_outcomes(passed=1, skipped=0)


def test_parametrize(monkeypatch, testdir):
    monkeypatch.delenv('CI', raising=False)
    testdir.makepyfile("""
        import pytest

        mark = pytest.mark.ci()

        @pytest.mark.parametrize('x', [pytest.param('a', marks=mark), 'b'])
        def test_foo(x):
            pass
    """)

    result = testdir.runpytest()
    result.assert_outcomes(passed=1, skipped=1)


@pytest.mark.parametrize('arg', ['', '(reason="Hello World")'])
def test_reason(monkeypatch, testdir, arg):
    monkeypatch.delenv('CI', raising=False)

    testdir.makepyfile("""
        import pytest

        @pytest.mark.ci{arg}
        def test_foo():
            pass
    """.format(arg=arg))

    result = testdir.runpytest('-rs')
    if arg:
        msg = 'SKIPPED [1] test_reason.py:3: Only runs on CI: Hello World'
    else:
        msg = 'SKIPPED [1] test_reason.py:3: Only runs on CI.'
    result.stdout.fnmatch_lines([msg])


def test_strict(monkeypatch, testdir):
    testdir.makepyfile("""
        import pytest

        @pytest.mark.ci
        def test_foo():
            pass
    """)

    result = testdir.runpytest('--strict')
    assert result.ret == 0
