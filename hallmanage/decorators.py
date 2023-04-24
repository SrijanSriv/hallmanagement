import functools
from rest_framework.response import Response
import jwt

key = "hallmanagementSystemProject"
def check_authentication():
    def decorator(views_func):
        @functools.wraps(views_func)
        def wrapper(request, *args, **kwargs):
            try:
                if not request.META.get('HTTP_AUTHORIZATION'):
                    raise Exception("please provide the token")
                bearer_token_array = request.META.get('HTTP_AUTHORIZATION').split(" ")
                token = bearer_token_array[1]
                if not token:
                    raise Exception("authentication failed")
                payload = jwt.decode(token, key, algorithms=["HS256"])
                kwargs['hallId'] = payload['hallId']
                return views_func(request, *args, **kwargs)
            except jwt.ExpiredSignatureError as err:
                return Response({"message": f"{err}"})
            except Exception as err:
                return Response(err)
        return wrapper
    return decorator
