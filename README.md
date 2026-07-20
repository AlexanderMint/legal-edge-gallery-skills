# Legal AI Edge Gallery Skills

Набор русскоязычных автономных Agent Skills для Google AI Edge Gallery.

## Навыки

| Каталог | Назначение | Интернет |
|---|---|---|
| `legal-contract-auditor` | Аудит предоставленного договора | Не нужен |
| `legal-template-adapter` | Адаптация предоставленного шаблона | Не нужен |
| `legal-case-brief` | Конспект материалов дела | Не нужен |
| `legal-position-red-team` | Проверка слабых мест позиции | Не нужен |
| `legal-document-drafter` | Подготовка проектов документов | Не нужен |
| `legal-law-version-comparator` | Сравнение двух редакций | Не нужен |
| `legal-calculator` | Детерминированные расчёты через JavaScript | Не нужен |

## Что исправлено в версии 2

- YAML-frontmatter записан с отдельными строками `---`.
- Все строковые значения YAML заключены в кавычки.
- Все текстовые файлы имеют UTF-8 без BOM и переводы строк LF.
- Добавлены `.gitattributes` и `.editorconfig`.
- Добавлен валидатор структуры и YAML.
- Добавлен GitHub Actions workflow.
- В `metadata.homepage` указаны реальные страницы репозитория.
- Описания навыков уточнены для более корректного автоматического выбора.
- Калькулятор использует десятичные строки и `BigInt`, а не неточные денежные вычисления через обычный `Number`.

## Публикация

Загрузите **содержимое** этой папки в корень репозитория:

```text
AlexanderMint/legal-edge-gallery-skills
```

В GitHub откройте:

```text
Settings → Pages → Deploy from a branch
```

Выберите:

```text
Branch: main
Folder: / (root)
```

Файл `.nojekyll` уже добавлен.

После публикации проверьте в браузере:

```text
https://alexandermint.github.io/legal-edge-gallery-skills/legal-contract-auditor/SKILL.md
```

Файл должен открываться как исходный многострочный Markdown.

В AI Edge Gallery указывайте URL папки:

```text
https://alexandermint.github.io/legal-edge-gallery-skills/legal-contract-auditor/
```

Не указывайте:

```text
https://alexandermint.github.io/legal-edge-gallery-skills/legal-contract-auditor/SKILL.md
```

и не используйте `raw.githubusercontent.com` для JavaScript-навыков.

## Локальная проверка

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python tools/validate_skills.py
```

Ожидаемый результат:

```text
Validation passed: 7 skills
```

## Рекомендации по включению навыков

Не включайте все навыки одновременно на небольшой мобильной модели.

- Проверка договора: `legal-contract-auditor`
- Адаптация: `legal-template-adapter`, затем `legal-contract-auditor`
- Материалы дела: `legal-case-brief`
- Проверка позиции: `legal-position-red-team`
- Подготовка проекта: `legal-document-drafter`
- Сравнение редакций: `legal-law-version-comparator`
- Расчёты: `legal-calculator`

## Ограничения

Навыки не содержат актуальную базу законодательства и судебной практики. Они не должны самостоятельно подтверждать действующую редакцию нормы, существование судебного акта или актуальные сведения о контрагенте.

Результат требует проверки квалифицированным юристом перед использованием.
