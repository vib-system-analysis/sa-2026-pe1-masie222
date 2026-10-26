# Деплой hello-world

## Production-заглушка

Статическая заглушка находится в `public/index.html`. Production-пайплайн готовится как GitHub Pages и не содержит модели, секретов или реальных резюме.

## Настройка GitHub Pages

1. В репозитории открыть `Settings → Pages`.
2. В разделе **Build and deployment** выбрать **GitHub Actions**.
3. Смерджить ветку лабы в `main`.
4. Открыть публичный URL из отчёта Actions или поля Pages.

## Workflow

В репозитории отсутствует workflow Pages до фактического включения GitHub Pages: это намеренно, чтобы не публиковать заглушку до настройки разрешений. После включения нужно добавить `.github/workflows/pages.yml` с deployment permissions и загрузкой каталога `public`.

## Локальная проверка

```bash
cp .env.example .env
docker compose -f compose.dev.yml up --detach
curl --fail http://127.0.0.1:8080/
curl --fail http://127.0.0.1:8081/status.json
docker compose -f compose.dev.yml down
```

Остановка должна завершиться одной командой; поднятие не требует ручной генерации файлов. Реальный provider отключён до отдельного review по обработке данных.

## Критерий готовности прод-

- URL открывается у любого участника команды без VPN или авторизации.
- Страница загружается без пустого экрана и не запрашивает секреты.
- `status.json` показывает `mode: synthetic-stub`.
- В репозитории нет ключей API и реальных резюме.
