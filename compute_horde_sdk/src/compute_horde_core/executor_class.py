# Backward compatible StrEnum with Python 3.10
try:
    from enum import StrEnum
except ImportError:
    from enum import Enum as Enum

    class _StrEnum(str, Enum):
        def __str__(self) -> str:
            return str(self.value)

    StrEnum = _StrEnum


class ExecutorClass(StrEnum):
    spin_up_4min__gpu_24gb = "spin_up-4min.gpu-24gb"
    always_on__gpu_24gb = "always_on.gpu-24gb"
    always_on__llm__a6000 = "always_on.llm.a6000"
