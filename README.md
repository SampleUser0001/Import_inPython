# import in Python

## 概要

- Pythonで「モジュール」はファイルを指す。
- 「from」はモジュールの指定。
- 「import」はクラスの指定。

## ディレクトリ構成

``` txt
.
├── src
│   ├── app.py
│   └── util
│       ├── __pycache__
│       └── SampleUtil.py
└── start.sh
```

### app.pyからutil/SampleUtil.pyを参照する

``` python app.py
# import sys
# sys.pathからモジュールを探す。
# pythonコマンド実行ディレクトリは最初から含まれているので、この環境では./src/utilを探しに行く。
from util.SampleUtil import SampleUtil

# hello_worldはクラスメソッド。
SampleUtil.hello_world()
```

### 備考

#### 循環importはできない

この実装パターンはNG。

common.py

``` python

from sub01 import Sub01

class Common():
  # superクラスの定義

class Factory():
  # サブクラスのインスタンスを生成するクラス
```

sub01.py

``` python

from common import Common

class Sub01(Common):
  # superクラスの定義
  
```

こういう時はFactoryを別のモジュールにする等の対応を行う。

## 参考

- [Qiita:Docker を使う（python のイメージで色々確認してみる）](https://qiita.com/landwarrior/items/fd918da9ebae20486b81)
- [Future Tech Blog:仕事でPythonコンテナをデプロイする人向けのDockerfile (1): オールマイティ編](https://future-architect.github.io/articles/20200513/)
- [Python3 自作モジュールのインポートにハマる:かもメモ](https://chaika.hatenablog.com/entry/2018/08/24/090000)