---
name: legal-calculator
description: Выполняет автономные детерминированные расчёты простых процентов, неустойки, сумм по периодам, календарных дней и проверку арифметики. Правовые параметры расчёта должен предоставить пользователь или юрист.
metadata:
  homepage: https://github.com/USERNAME/legal-edge-gallery-skills
---

# Юридический калькулятор

## Важное ограничение

Этот навык считает, но не определяет по памяти применимую ставку, начало просрочки, мораторий, предел ответственности, правила рабочего календаря или юридическую формулу. Пользователь должен предоставить параметры или подтвердить их.

## Когда вызывать JavaScript

Для арифметического расчёта обязательно вызови инструмент `run_js`.

- script name: index.html
- data: JSON-строка.

Поддерживаемые операции:

### simple_interest
Поля:
- operation: "simple_interest"
- principal: Number, основная сумма
- annual_rate_percent: Number, годовая ставка в процентах
- days: Integer, число дней
- year_basis: 365 или 366
Формула: principal × rate / 100 × days / year_basis.

### penalty_percent_per_day
Поля:
- operation: "penalty_percent_per_day"
- principal: Number
- daily_rate_percent: Number
- days: Integer
- cap: Number или null
Формула: principal × daily rate / 100 × days, затем применяется cap.

### sum_items
Поля:
- operation: "sum_items"
- items: массив объектов {"label": String, "amount": Number}

### calendar_days
Поля:
- operation: "calendar_days"
- start_date: "YYYY-MM-DD"
- end_date: "YYYY-MM-DD"
- inclusion: "exclude_start" | "include_both" | "exclude_end"
Расчёт ведётся в календарных днях UTC.

### verify_expression
Поля:
- operation: "verify_expression"
- operands: массив чисел
- operator: "sum" | "subtract_sequence" | "multiply"

## После результата

1. Покажи исходные параметры.
2. Покажи формулу.
3. Покажи промежуточный результат без округления и итог с двумя знаками.
4. Укажи, какие правовые предпосылки не проверялись.
5. Не называй расчёт расчётом по конкретной статье закона, если формулу и применимость не подтвердил пользователь.
