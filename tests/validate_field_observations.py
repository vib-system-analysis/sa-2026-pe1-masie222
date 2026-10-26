from pathlib import Path

REQUIRED_FACT_MARKERS = (
    'Полевая доказательная база отсутствует',
    'Реальный эпизод должен иметь дату, время, место, систему, конкретного участника',
    'записанное наблюдение',
    'поле «что удивило»',
)

FORBIDDEN_EVIDENCE_SHAPES = (
    '| OBS-001 |',
    '| OBS-002 |',
    '| OBS-003 |',
    'Статус: шаблон.',
)


def main() -> None:
    path = Path('docs/field-observations.md')
    text = path.read_text(encoding='utf-8')

    missing_markers = [marker for marker in REQUIRED_FACT_MARKERS if marker not in text]
    assert not missing_markers, f'missing field evidence markers: {missing_markers}'

    forbidden = [shape for shape in FORBIDDEN_EVIDENCE_SHAPES if shape in text]
    assert not forbidden, f'empty observation template must not be presented as evidence: {forbidden}'

    print('field evidence guard passed: no fabricated observations')


if __name__ == '__main__':
    main()
