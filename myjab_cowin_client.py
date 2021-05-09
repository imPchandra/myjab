"""
This is the client module which has wrapper functions for all possible GET, POST etc REST API requests
Also, there are possible list of exceptions that may occur while making the REST API calls.
"""
import json
from myjab_cowin_core import Core

class APIException(Exception):
    """This is the base class for all exceptions raised by JAMAClient"""
    pass


class UnauthorizedException(APIException):
    """This ecxeption is thrown whenever the api returns a 401 unauthorized response."""
    pass


class TooManyRequestsException(APIException):
    """This exception is thrown whenever the api returns a 429 too many requests response."""
    pass


class ResourceNotFoundException(APIException):
    """This exception is raised whenever the api returns a 404 not found response."""
    pass


class AlreadyExistsException(APIException):
    """This exception is thrown when the API returns a 400 response with a message that the resource already exists."""
    pass


class APIClientException(APIException):
    """This exception is thrown whenever a unknown 400 error is encountered."""
    pass


class APIServerException(APIException):
    """This exception is thrown whenever an unknown 500 response is encountered."""
    pass

class CowinClient:
    """
    Class to abstract communication with Cowin Server APIs
    """
    def __init__(self, host_domain="https://cdn-api.co-vin.in/",
                 credentials=('username|clientID', 'password|clientSecret'),
                 api_version='api/v2/',
                 oauth=False):
        """Cowin Client initializer
        :rtype: CowinClient
        :param host_domain: String The domain associated with the Cowin host
        :param credentials: the user name and password as a tuple or client id and client secret if using Oauth.
                            not required at the time of development
        :param api_version: api version '/v2/' """
        self.__credentials = credentials
        self.__core = Core(host_domain, credentials, api_version=api_version, oauth=oauth)

    def generate_otp(self, mobile):
        resource_path = "auth/public/generateOTP"
    
    def confirm_otp(self):
        resource_path = "auth/public/confirmOTP"

    def get_states(self):
        resource_path = "admin/location/states"
        response = self.__get(resource_path, params=None)
        CowinClient.__handle_response_status(response)
        return response.json()['states']

    def get_districts_list(self, state_id):
        resource_path = "admin/location/districts/"+state_id

    def get_vaccination_sessions_by_pin(self, pin):
        resource_path = "appointment/sessions/public/findByPin"

    def get_vaccination_sessions_by_district(self, district_id):
        resource_path = "appointment/sessions/public/findByDistrict"

    def get_vaccination_sessions_by_pin_for_seven_days(self, pin):
        resource_path = "appointment/sessions/public/calendarByPin"

    def get_vaccination_sessions_by_district_for_seven_days(self, district_id):
        resource_path = "appointment/sessions/public/calendarByDistrict"

    def get_certificate_as_pdf(self, beneficiary_id):
        resource_path = "registration/certificate/public/download"

    def __get(self, resource, params=None, **kwargs):
        parameters = {}
        if params:
            for key, value in params.items():
                parameters[key] = value
        response = self.__core.get(resource, params=parameters, **kwargs)
        CowinClient.__handle_response_status(response)
        return response

    @staticmethod
    def __handle_response_status(response):
        """ Utility method for checking http status codes.
        If the response code is not in the 200 range, An exception will be thrown."""

        status = response.status_code

        if status in range(200, 300):
            return status

        if status in range(400, 500):
            """These are client errors. It is likely that something is wrong with the request."""

            try:
                response_json = json.loads(response.text)
                response_message = response_json.get('meta').get('message')

            except json.JSONDecodeError:
                pass

            raise APIClientException("{} Client Error ".format(status) + response.reason)

        if status in range(500, 600):
            """These are server errors and network errors."""
            raise APIServerException("{} Server Error.".format(status))