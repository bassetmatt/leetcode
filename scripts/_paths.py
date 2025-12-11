from pathlib import Path

__DATA = Path("data")
CSV_FILE = __DATA / "problems.csv"
DEF_RUST_FILE = __DATA / "rust_src_template.rs"
DEF_CPP_FILE = __DATA / "cpp_src_template.cpp"
DEF_PY_FILE = __DATA / "python_src_template.py"
DEF_JAVA_FILE = __DATA / "java_src_template.java"

README_FILE = Path("README.md")

__paths = [
    __DATA,
    README_FILE,
    DEF_RUST_FILE,
    DEF_CPP_FILE,
    DEF_PY_FILE,
    DEF_JAVA_FILE,
]

for p in __paths:
    if not p.exists():
        raise FileNotFoundError(f"Required path {p} does not exist")
