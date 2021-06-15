## API для интернет-магазина

- Товар: `/api/v1/products/`
- Отзыв к товару: `/api/v1/product-reviews/`
- Заказы: `/api/v1/orders/`
- Подборки: `/api/v1/product-collections/`

## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Создать базу в postgres и прогнать миграции:

```base
./manage.py migrate
```

Тестовый данные можно загрузить командой:
```base
./manage.py loaddata app.json
```

Запуск тестов:
```base
pytest
```
