from dataclasses import dataclass, field, asdict, fields, is_dataclass
import json
from pathlib import Path


@dataclass
class InstancesSettings:
    pass

@dataclass
class AccountsSettings:
    select_account: int = 0
    accounts_list: dict = field(default_factory=lambda: [{"uuid": "5627dd98-e6be-3c21-b8a8-e92344183641", 
                                                          "name": "Steve", 
                                                          "type": "offline"}])

@dataclass
class Settings:
    instances: InstancesSettings = field(default_factory=InstancesSettings)
    accounts: AccountsSettings = field(default_factory=AccountsSettings)


class SettingsManager:
    def __init__(self):
        self.file_path = Path("settings.json")
        self.settings = self._load()

    def _load(self) -> Settings:
        defaults = Settings()

        if not self.file_path.is_file():
            self._write(defaults)
            return defaults

        try:
            data = json.loads(
                self.file_path.read_text(encoding="utf-8")
            )
        except (json.JSONDecodeError, TypeError, ValueError):
            self._write(defaults)
            return defaults

        settings = self._from_dict(Settings, data)

        self._write(settings)

        return settings

    def _from_dict(self, cls, data):
        if not is_dataclass(cls):
            return data

        values = {}

        for field_info in fields(cls):
            if field_info.name not in data:
                continue

            value = data[field_info.name]
            field_type = field_info.type

            if is_dataclass(field_type) and isinstance(value, dict):
                value = self._from_dict(field_type, value)

            values[field_info.name] = value

        return cls(**values)

    def _write(self, settings: Settings) -> None:
        self.file_path.write_text(
            json.dumps(
                asdict(settings),
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

    def save(self) -> None:
        self._write(self.settings)