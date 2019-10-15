import uasyncio


class AsyncTestRunner:
    def __init__(self):
        self.return_value = None

    async def _runner(self, coro):
        self.return_value = await coro

    def run(self, coro):
        uasyncio.get_event_loop().run_until_complete(self._runner(coro))
        return self.return_value


class Mock:
    def __init__(self):
        self.calls = []
        self.return_value = None

    def __call__(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        if self.return_value:
            return self.return_value

    @property
    def call_args_list(self):
        return self.calls


class AsyncMock(Mock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


class MonkeyPatch:
    """Monkeypatch some object.

    Example:
        You can use it like this::

            from tools import MonkeyPatch
            from tools import Mock

            mock_zack = Mock()
            mock_zack.return_value = "bumm"

            with MonkeyPatch(foo, "zack", mock_foo):
                print(foo.zack())


    Args:
        object (callable): Object to patch.
        name (str): Name of attribute to set.
        patch (callable): Object that gets set to the attribute.

    """

    def __init__(self, object, name, patch):
        self.object = object
        self.name = name
        self.patch = patch
        self.pre_patch_value = None

    def __enter__(self):
        self.pre_patch_value = getattr(self.object, self.name)
        setattr(self.object, self.name, self.patch)

    def __exit__(self, exc_type, exc_value, traceback):
        setattr(self.object, self.name, self.pre_patch_value)
