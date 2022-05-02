"""
Mypy plugin.

This is a simple plugin, that adds support for our custom attrs wrapper.

To use it, add `naff.ext.mypy` to the plugins list in your mypy config.

For mypy.ini:
```ini
[mypy]
plugins = naff.ext.mypy
```

For pyproject.toml:
```toml
[tool.mypy]
plugins = "naff.ext.mypy"
```
"""
from functools import partial
from typing import Callable, Optional
from mypy.plugin import Plugin, ClassDefContext
from mypy.plugins import attrs

__all__ = ("plugin",)


class NaffPlugin(Plugin):
    # This could be smarter, but it does the job.
    def get_class_decorator_hook(self, fullname: str) -> Optional[Callable[[ClassDefContext], None]]:
        if fullname == "naff.client.utils.attr_utils.define":
            return partial(
                attrs.attr_class_maker_callback,
                auto_attribs_default=None,
            )
        return None


def plugin(version: str) -> NaffPlugin:
    # ignore version argument if the plugin works with all mypy versions.
    return NaffPlugin
