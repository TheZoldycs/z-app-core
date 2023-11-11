from rest_framework_simplejwt.tokens import AccessToken
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User


@database_sync_to_async
def returnUser(token_string):
    access_token = AccessToken(token_string)  # Get the access token from the request
    try:
        user_id = access_token.payload['user_id']
        user = User.objects.get(id=user_id)
    except:
        user = AnonymousUser()
    return user


class TokenAuthMiddleWare:
	def __init__(self, app):
		self.app = app
	async def __call__(self, scope, receive, send):
		query_string = scope["query_string"]
		query_params = query_string.decode()
		query_dict = parse_qs(query_params)
		try:
			token = query_dict.get("token")[0]
		except :
			token=None
		if token:
			user = await returnUser(token)
			scope["user"] = user
		return await self.app(scope, receive, send)