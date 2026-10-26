from pathlib import Path

REQUIRED_FIELD_MARKERS = (
    'Полевая доказательная база отсутствует',
    'Реальный эпизод должен иметь дату, время, место, систему, конкретного участника',
    'записанное наблюдение',
    'поле «что удивило»',
)

REQUIRED_CURRENT_STATE_MARKERS = (
    'Состояние реального процесса отбора резюме в репозитории не описано и не подтверждено',
    'Процесс сегодня: не собран',
    'система сейчас не описана',
)

FORBIDDEN_EVIDENCE_SHAPES = (
    'Рекрутер обрабатывает сотни резюме вручную и принимает решения',
    'К декабрю рекрутер малого HR-отдела открывает систему',
    '| OBS-001 |',
    '| OBS-002 |',
    '| OBS-003 |',
    'Статус: шаблон.',
)


def main() -> None:
    field_text = Path('docs/field-observations.md').read_text(encoding='utf-8')
    current_text = Path('docs/current-state.md').read_text(encoding='utf-8')

    missing_markers = [marker for marker in REQUIRED_FIELD_MARKERS if marker not in field_text]
    missing_markers += [marker for marker in REQUIRED_CURRENT_STATE_MARKERS if marker not in current_text]
    assert not missing_markers, f'missing field evidence markers: {missing_markers}'

    forbidden = [shape for shape in FORBIDDEN_EVIDENCE_SHAPES if shape in field_text + current_text]
    assert not forbidden, f'empty observation template must not be presented as evidence: {forbidden}'

    print('field evidence guard passed: no fabricated observations')


if __name__ == '__main__':
    main()
