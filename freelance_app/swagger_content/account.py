from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view, inline_serializer
from rest_framework import serializers
from freelance_app.serializers.account import AccountCreateSerializer


auth = extend_schema_view(
    post=extend_schema(
        tags=['Sign in and sign up'],
        parameters=[OpenApiParameter(
            'login_params', str,
            enum=['email', 'username'],
            default='email'
        )],
        request=inline_serializer('auth_request', {
            'email': serializers.CharField(),
            'username': serializers.CharField(),
            'password': serializers.CharField()
        }),
        responses={
            '200': inline_serializer('auth_response2', {
                'access': serializers.CharField(),
                'refresh': serializers.CharField()
            })
        }
    )
)


create = extend_schema_view(
    post=extend_schema(
        tags=['Sign in and sign up'],
        responses={
            '200': inline_serializer('user_create_response', {
                'access': serializers.CharField(),
                'refresh': serializers.CharField(),
                'user': AccountCreateSerializer()
            })
        }
    )
)


password_and_phone_validation = extend_schema_view(
    post=extend_schema(
        tags=['Sign in and sign up']
    )
)

refresh = extend_schema_view(
    post=extend_schema(
        tags=['Sign in and sign up']
    )
)


account = extend_schema_view(
    get=extend_schema(
        tags=['Account']
    ),
    patch=extend_schema(
        tags=['Account']
    ),
    put=extend_schema(
        tags=['Account']
    ),
    delete=extend_schema(
        tags=['Account']
    )
)

change_password = extend_schema_view(
    post=extend_schema(
        tags=['Account'],
    )
)

email_check = extend_schema_view(
    post=extend_schema(
        tags=['Account'],
        parameters=[OpenApiParameter(
            'place', str,
            enum=['register', 'change_password'],
            default='change_password'
        )],
    )
)

