import re
from pathlib import Path
from typing import Generator

import toml

BASE_TYPE = {"int": int, "str": str, "bool": bool, "float": float}


def type_parser(type_str: str) -> type:
    if (match := re.match(r"List[(?P<base>\w)]", type_str)) is not None:
        groups = match.groupdict()
        base = groups["base"]
        if base not in BASE_TYPE:
            raise TypeError(f"List of unknown type: '{base}'")
        return list[BASE_TYPE[base]]

    elif type_str in BASE_TYPE:
        return BASE_TYPE[type_str]

    raise TypeError(f"Unknown type {type_str}")


TypeDict = dict[str, type]


class CaseDef:
    def __init__(self, inputs_type: TypeDict, output_type: TypeDict) -> None:
        self.inputs = inputs_type
        self.output = output_type


class TestCase:
    def __init__(self, types: CaseDef, inputs: dict, output: dict) -> None:
        self.types = types
        self.input = inputs
        self.output = output
        assert types.inputs.keys() == inputs.keys()

    def to_param_in(self) -> str:
        def param_str() -> Generator[str]:
            for name, value in self.input.keys():
                ty = self.types.inputs[name]
                s = ""
                if isinstance(ty, str | int | float | bool):
                    s = f"{name}={value}"
                elif isinstance(ty, list):
                    s = f"{name}={value}"
                yield s

        param_list = ", ".join(param_str())
        return f"fn({param_list})"

    def expected_value(self) -> str:
        return ""


def load_file(folder: Path) -> list[TestCase]:
    TEST_FILES = folder / "testcases.toml"
    with open(TEST_FILES, "r") as f:
        tests_config = toml.load(f)
    assert tests_config.get("version", "") == 1.0, (
        f"Wrong testcase version in folder {folder}"
    )

    inputs: dict[str, type] = {}
    format = tests_config["format"]
    for name, ty in format["input"]["values"].items():
        inputs[name] = type_parser(ty)

    output: dict[str, type] = {}
    for name, ty in format["output"]:
        output[name] = type_parser(ty)

    defs = CaseDef(inputs, output)

    cases: list[TestCase] = []
    for case in tests_config["testcases"]:
        case_in = case["input"]
        case_out = case["output"]
        cases.append(TestCase(defs, case_in, case_out))

    return cases


# def to_python(folder: Path, testcases: list[TestCase]) -> None:
#     ident = " " * 4
#     test_file_txt = ""

#     for case in testcases:
#         pass
#     test_file_txt = f"fn()"
#     pass


"""
from typing import Callable
from solution import Solution


def test_sol() -> None:
    # Ensures that if there are multiple implementations they are all tested
    sol = Solution()
    funcs_to_test: list[Callable] = [
        attrib
        for (key, attrib) in sol.__dict__.items()
        if callable(attrib) and not key.startswith("_")
    ]

    for fn in funcs_to_test:
        per_fn(fn)


def per_fn(fn: Callable) -> None:
    # Code here
"""
