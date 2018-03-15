# -*- coding: utf-8 -*-
"""PyLint のコードチェックを行うテストが格納されたモジュール."""

from subprocess import PIPE, Popen
from unittest import TestCase

from nose.tools import ok_
from pylint import epylint as lint


class PyLintTestCase(TestCase):
    """PyLintによるコードチェックを行うためのクラス."""

    def setUp(self) -> None:
        """Run setup function."""
        pass

    def tearDown(self) -> None:
        """Run tear down function."""
        pass

    def test_pylint_conformance(self) -> None:
        """PyLintによるコードチェックを行うテスト."""
        # 検査対象とするディレクトリ名
        dir_name = "my_tools"
        # 検査から除外するエラーや警告
        disables = [
            "R0801",    # Similar lines in 2 files.
            "C0326",    # bad-whitespace
            "C0103",    # invalid-name
            # "invalid-name",   # この書き方でも可
            "R0903",    # too-few-public-methods
        ]
        # 検査から除外するファイル
        ignore_files = [
            "__init__.py",
        ]
        # PyLintに渡すオプション
        options = [
            "--max-line-length=160",
            "--variable-rgx='[a-z_]([a-z0-9_])?'",  # 変数名: v, v1, val_hoge1, __val 等
            f"--disable={','.join(disables)}",
            f"--ignore-patterns={','.join(ignore_files)}",
        ]
        cmd = " ".join([dir_name, " ".join(options)])

        # PyLint を実行します.
        # 結果は pylint_stdout に格納されます.
        pylint_stdout, _ = lint.py_run(cmd, return_std=True)

        # pylint_stdout から区切りの行と前後の空白、改行を取り除いた文字列を
        # messages に格納します.
        messages = []
        for line in pylint_stdout.readlines():
            s = line.strip()
            if len(s) and not s.startswith(("*", "-")):
                messages.append(s)

        if len(messages) > 1:   # 最初の１行目は結果にかかわらず表示されるサマリー.
            # テスト失敗
            # messages に何か内容が入っていればテストは失敗とみなし.内容をコンソールに表示する.
            ok_(False, "\n".join(messages))
        else:
            # テスト成功
            # messages に警告やエラーが無ければテストは成功とみなす.
            ok_(True)
