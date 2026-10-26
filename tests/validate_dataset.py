import json
from pathlib import Path

REQUIRED = {
    "id", "source", "version", "resume_text", "target", "quality_labels", "owner"
}


def main() -> None:
    path = Path("docs/quality/golden-dataset.jsonl")
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    assert len(records) >= 10, "golden dataset must contain at least 10 examples"
    ids = [record["id"] for record in records]
    assert len(ids) == len(set(ids)), "record ids must be unique"

    for record in records:
        assert REQUIRED <= record.keys(), f"missing fields: {record.get('id', 'unknown')}"
        assert isinstance(record["target"]["overall_score"], int)
        assert 0 <= record["target"]["overall_score"] <= 100

    print(f"validated {len(records)} golden dataset examples")


if __name__ == "__main__":
    main()
