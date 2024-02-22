class SafeDict(dict):
    def __init__(self, default=None, *args, **kwargs):
        self.default = default
        super().__init__(*args, **kwargs)
        self._convert_nested_dicts()

    def _convert_nested_dicts(self):
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = SafeDict(default=self.default, **value)
            elif isinstance(value, list):
                self[key] = [SafeDict(default=self.default, **item) for item in value]

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.default
