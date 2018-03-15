# -*- coding: utf-8 -*-
"""Adder のユニットテストが格納されたモジュール."""

from unittest import TestCase

from nose.tools import eq_

from my_tools.adder import Adder


class AdderTestCase(TestCase):
    """Adder クラスのユニットテスト."""

    def setUp(self) -> None:
        """各テスト毎の初期化."""
        pass

    def tearDown(self) -> None:
        """各テスト毎の後処理."""
        pass

    def test_add(self) -> None:
        """加算メソッドのテスト."""
        adder = Adder()
        eq_(3, adder.add(1, 2))
