from __future__ import annotations

from typing import Optional


class IdGenerator:
    __signature = object()
    __instance: Optional[IdGenerator] = None

    def __init__(self, signature: object):
        assert signature is IdGenerator.__signature
        self.__counter = -1

    @staticmethod
    def instance() -> IdGenerator:
        if IdGenerator.__instance is None:
            IdGenerator.__instance = IdGenerator(IdGenerator.__signature)
        return IdGenerator.__instance

    def __next__(self) -> int:
        self.__counter += 1
        return self.__counter
