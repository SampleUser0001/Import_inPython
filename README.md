# import in Python

## 概要

- Pythonで「モジュール」はファイルを指す。
- 「from」はモジュールの指定。
- 「import」はクラスの指定。
- ```sys.path.append('./util')```は、```python```コマンド実行ディレクトリからの相対パスを指定する。

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
import sys
sys.path.append('./util')
from SampleUtil import SampleUtil

# hello_worldはクラスメソッド。
SampleUtil.hello_world()
```



## 参考

- [Qiita:Docker を使う（python のイメージで色々確認してみる）](https://qiita.com/landwarrior/items/fd918da9ebae20486b81)
- [Future Tech Blog:仕事でPythonコンテナをデプロイする人向けのDockerfile (1): オールマイティ編](https://future-architect.github.io/articles/20200513/)