# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module autoread_dotenv.autoread."""
import os


def test_env_path() -> None:
    from autoread_dotenv.autoread import get_dotenv_path

    env_path = get_dotenv_path()
    assert env_path


def test_autoread_dotenv() -> None:
    from autoread_dotenv.autoread import autoread_dotenv

    # initially already set via sitecustomize
    foo = os.getenv("FOO")
    if foo:
        del os.environ["FOO"]

    # test cleared environment
    foo = os.getenv("FOO")
    assert foo is None

    autoread_dotenv()
    foo = os.getenv("FOO")
    assert foo == "foo"
