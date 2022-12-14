# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

from colors import green

import pathlib
import json
import random

import pkg_resources

from helloworld.translator.translator import LanguageTranslator


class Greeter:
    def __init__(self,
                 *,
                 translations: dict[str, dict[str, str]] | None = None
                 ) -> None:
        self._translations = (translations
                              if translations is not None else json.loads(
                                  pkg_resources.resource_string(
                                      __name__, "translations.json")))
        self._translator = LanguageTranslator(self._translations)

    def greet(self, name: str) -> str:
        random_greeting = random.choice(list(self._translations.keys()))
        greeting = self._translator.translate_to_random_language(
            random_greeting)
        return f"{greeting}, {name}!".capitalize()


def say_hello() -> None:
    greeting = Greeter().greet("Pantsbuild")
    secret_path = pathlib.Path(
        __file__).parent / 'helloworld/external/data/top_secret.txt'
    print(green(greeting))
    print(secret_path.read_text())


if __name__ == "__main__":
    say_hello()