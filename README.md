# my_tools
## 概要
Qiita の記事で使用している架空のプロジェクト `my_tools` のサンプルコードです。
- [Style guide に即していない Python コードを自動で弾く](https://qiita.com/tshimura/items/4827e1d0a8463944008c)

Python 3.6 を使用しています。

## 使用するモジュールのインストール

pip によりインストールします。
```
pip install -r requirements.txt
```

## テストの実行
nose によりテストを実行します。
```
nosetests
```
通常のテストの他にStyle guideのチェックが実行されます。

## ドキュメントの生成
Sphinx によりドキュメントが生成されます。
このプロジェクトのルートディレクトリから
```
sphinx-build -a ./docs/ ./docs/html/
```
または docs ディレクトリから
```
make html
```

## GitHub/Circle CI
GitHub にリポジトリをプッシュするとテストが実行されます。
テストの後にドキュメントのビルドが行われます。

## S3へのアップロード
GitHub にマスターブランチがプッシュされた場合、S3 にドキュメントを転送します。
転送には AWS CLI が使用されます。
