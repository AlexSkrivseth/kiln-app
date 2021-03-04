from django.core.exceptions import ValidationError
from rest_framework import exceptions, permissions, authentication

from api.models import APIClient



# custom authentication
# not useing this right now
def validate_authkey(value):
    """Raises a ValidationError if value has not length 32"""
    if not len(value) == 32:
        raise ValidationError(
            'Value must be a string containing 32 alphanumeric characters')

# custom authentication class
class APIClientAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        # Get the accesskey from the query parameters, and the secretkey from
        # the request headers.
        accesskey = request.query_params.get('accesskey')
        secretkey = request.META.get('secretkey')
