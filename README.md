# notifiers_wecom_provider

WeCom provider for [Notifiers](https://github.com/liiight/notifiers).

```python
from notifiers import get_notifier
notifier = get_notifier("wecom")
notifier.notify(msgtype="text", api_key='1234', message="test")
```
