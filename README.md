# vocabulary
mem vocabulary in terminal

### 介绍

- 在终端terminal中背单词。

- 目前只有 TOFEL 词库。可以自行导入其他词库，稍作配置即可。

- `default_num` 表示每次默认返回几个单词。当前默认每次返回5个单词。

- 每次随机出单词。


### 使用方法

```
python3 main.py
```

`default_num` 表示每次默认返回几个单词。

例如，在 `.zprofile` 中配置alias
```
alias abc='python3 ~/coding/py-proj/vocabulary/main.py'
```
即可用 `abc` 直接调用。