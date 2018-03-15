# -*- coding: utf-8 -*-
"""加算に関するユーティリティーが入っているモジュールです."""


class Adder:
    """加算器."""

    def __init__(self) -> None:
        """初期化."""
        self.result = 0

    def add(self, x: int, y: int) -> int:
        """加算を実行するメソッド.

        :param x: 整数x
        :param y: 整数y
        :return: x と y の演算結果
        """
        self.result = x + y
        return self.result
