# Import third-party modules
from notifiers import get_notifier


def test_get_provider():
    wecom = get_notifier("wecom")
    assert wecom.name == "wecom"
