import json
from pathlib import Path

REQUIRED_FIELDS = (
    'id',
    'evidence_type',
    'date',
    'start_time',
    'end_time',
    'timezone',
    'place',
    'system',
    'work_object',
    'participant_role',
    'participant_id',
    'source_access',
    'context',
    'observation',
    'surprised',
    'hypothesis',
    'verdict',
    'source',
)

FORBIDDEN_VALUES = (
    'evidence_status != real',
    'YYYY-MM-DD',
    'HH:MM',
    'не собранно',
    'не назначен',
    'шаблон',
)


def main() -> None:
    path = Path('docs/field-observations.jsonl')
    if not path.is_file():
        raise SystemExit(
            'BLOCKED: field observations are missing. '
            'Create docs/field-observations.jsonl with three real episodes.'
        )

    records = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line]
    if len(records) < 3:
        raise SystemExit('BLOCKED: at least three real field observations are required.')

    ids = set()
    for record in records:
        if record.get('evidence_type') != 'field-observation':
            raise SystemExit(f"BLOCKED: observation {record.get('id', '<unknown>')} is secondary, synthetic, or not field evidence")
        missing = [field for field in REQUIRED_FIELDS if not str(record.get(field, '')).strip()]
        if missing:
            raise SystemExit(f"BLOCKED: observation {record.get('id', '<unknown>')} missing fields: {missing}")
        if record['id'] in ids:
            raise SystemExit(f"BLOCKED: duplicate observation id: {record['id']}")
        ids.add(record['id'])

        serialized = json.dumps(record, ensure_ascii=False).lower()
        forbidden = [value for value in FORBIDDEN_VALUES if value in serialized]
        if forbidden:
            raise SystemExit(f"BLOCKED: observation {record['id']} contains template values: {forbidden}")

    print(f'field evidence guard passed: {len(records)} real observations')


if __name__ == '__main__':
    main()
