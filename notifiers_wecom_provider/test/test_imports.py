"""Import Test."""
# Import future modules
# Import built-in modules
import importlib
import pkgutil

import notifiers_wecom_provider

# Import local modules


def test_imports():
    """Test import modules."""
    prefix = f"{notifiers_wecom_provider.__name__}."
    iter_packages = pkgutil.walk_packages(
        notifiers_wecom_provider.__path__,  # noqa: WPS609
        prefix,
    )
    for _, name, _ in iter_packages:
        module_name = name if name.startswith(prefix) else prefix + name
        importlib.import_module(module_name)
