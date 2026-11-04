import json, pathlib
EXPECTED = {
    "Lumen-Stream-Code": "CC0-1.0",
    "Lumen-Stream-Syn": "MIT",
    "Lumen-Stream-Mix": "Apache-2.0",
}
def score(path):
    got = json.loads(pathlib.Path(path).read_text())
    return sum(got.get(k) == v for k, v in EXPECTED.items())
