# dict-envy

dict-like grouping of environment variables :sparkles:

---

Imagine you have this:

```
COUNTRIES_GB_NAME="United Kingdom"
COUNTRIES_GB_TLD=.uk
COUNTRIES_HK_NAME=China
COUNTRIES_HK_TLD=.cn
```

and with a simple call you can have all of this:

```python
>>> import os
>>> import dictenvy
>>> import pprint
>>> env = dictenvy.dictate(os.environ, depth=2)
>>> pprint.pprint(env)
{'countries': {'gb': {'name': 'United Kingdom', 'tld': '.uk'},
               'hk': {'name': 'China', 'tld': '.cn'}}}
```

`depth` is how you regulate the depth of the returned dictionary.

<details><summary>Couple gotchas</summary>

### #1

Sometimes you may encounter the following situation:

```
TERM_PROGRAM=Apple_Terminal
TERM=xterm-256color
```

In which case, the return value would still be a dict, but `TERM` value would have an empty key like so:

```python
>>> import dictenvy
>>> import pprint
>>> env = dictenvy.dictate({'TERM': 'xterm-256color', 'TERM_PROGRAM': 'Apple_Terminal'}, depth=1))
>>> pprint.pprint(env)
{'term': {'': 'xterm-256color', 'program': 'Apple_Terminal'}}
```

### #2

Variables that start with an underscore will be left alone.
</details>

## Installation

Use pip:

```shell
$ pip install dict-envy
```

## License

MIT
