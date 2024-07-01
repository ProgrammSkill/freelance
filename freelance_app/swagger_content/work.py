from drf_spectacular.utils import extend_schema, extend_schema_view


service = extend_schema_view(
    list=extend_schema(
        summary="Просмотр списка услуг",
        tags=['Service']
    ),
    retrieve=extend_schema(
        summary="Просмотр услуги",
        tags=['Service']
    ),
    create=extend_schema(
        summary="Создание услуги",
        tags=['Service']
    ),
    update=extend_schema(
        summary="Изменение данных в услуге",
        tags=['Service']
    ),
    partial_update=extend_schema(
        summary="Изменение данных в услуге",
        tags=['Service']
    ),
    destroy=extend_schema(
        summary="Удаление услуги",
        tags=['Service']
    )
)


order = extend_schema_view(
    list=extend_schema(
        summary="Просмотр списка заказов",
        tags=['Order']
    ),
    retrieve=extend_schema(
        summary="Просмотр заказа",
        tags=['Order']
    ),
    create=extend_schema(
        summary="Создание заказа",
        tags=['Order']
    ),
    update=extend_schema(
        summary="Изменение данных в заказе",
        tags=['Order']
    ),
    partial_update=extend_schema(
        summary="Изменение данных в заказе",
        tags=['Order']
    ),
    destroy=extend_schema(
        summary="Удаление заказа",
        tags=['Order']
    )
)