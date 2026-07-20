# Установка на iPhone

## Через GitHub Pages

1. Убедитесь, что GitHub Pages опубликован.
2. Откройте в Safari:

```text
https://alexandermint.github.io/legal-edge-gallery-skills/legal-contract-auditor/SKILL.md
```

3. Проверьте, что первая строка — отдельное `---`, затем идут многострочные `name` и `description`, а закрывающее `---` также находится на отдельной строке.
4. В AI Edge Gallery откройте Agent Skills.
5. Откройте менеджер Skills.
6. Нажмите `+`.
7. Выберите загрузку из URL.
8. Вставьте URL папки:

```text
https://alexandermint.github.io/legal-edge-gallery-skills/legal-contract-auditor/
```

## Диагностика ошибки `Expected at least two '---' sections`

Проверьте:

- URL ведёт на папку, а не на `SKILL.md`;
- файл опубликован через GitHub Pages;
- `.nojekyll` находится в корне;
- первая и закрывающая строки frontmatter равны ровно `---`;
- файл не превратился в одну строку;
- файл сохранён в UTF-8 без BOM и с LF;
- GitHub Actions `Validate skills` завершился успешно.

Если корректный файл всё равно не импортируется на iPhone, проверьте актуальную версию приложения и статус iOS-проблемы загрузчика навыков в официальном репозитории Google.
