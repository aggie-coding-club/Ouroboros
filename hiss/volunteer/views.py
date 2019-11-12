from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, response, permissions, authentication
from rest_framework.authtoken import views
from rest_framework.request import Request

from application.models import Application, STATUS_CHECKED_IN
from volunteer.models import FoodEvent, WorkshopEvent
from volunteer.permissions import IsVolunteer
from volunteer.serializers import EmailAuthTokenSerializer

USER_NOT_CHECKED_IN_MSG = (
    "This hacker has not been checked in. Please find an organizer immediately."
)


class EmailObtainAuthToken(views.ObtainAuthToken):
    """
    Given a request containing a user's "email" and "password", this view responds with the user's Token (which can
    be used to authenticate consequent requests).

    More information on how `TokenAuthentication` works can be seen at the DRF documentation site:
    https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
    """

    serializer_class = EmailAuthTokenSerializer


class CheckinHackerView(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated & (IsVolunteer | permissions.IsAdminUser)
    ]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request: Request, format: str = None):
        """
        Sets a specific user's Application status as STATUS_CHECKED_IN (indicating that a user has successfully
        checked into the event). If the request is malformed (i.e. missing the user's email), returns a Django Rest
        Framework Response with a 400 status code. if successful, returns a response with status 200.
        """
        user_email = request.data.get("email", None)
        if not user_email:
            # The hacker's email was not provided in the request body, we can't do anything.
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        # Return 404 if no application exists for the provided user.
        application: Application = get_object_or_404(
            Application, user__email=user_email
        )
        application.status = STATUS_CHECKED_IN
        application.save()
        return response.Response(status=status.HTTP_200_OK)

    def get(self, request: Request, format: str = None):
        user_email = request.GET.get("email")
        if not user_email:
            # The hacker's email was not provided as a query parameter, we can't do anything.
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        # Return 404 if no application exists for the provided user.
        application: Application = get_object_or_404(
            Application, user__email=user_email
        )
        return JsonResponse(
            {"checked_in": True if application.status == STATUS_CHECKED_IN else False}
        )


class CreateFoodEventView(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated & (IsVolunteer | permissions.IsAdminUser)
    ]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request: Request, format: str = None):
        """
        Creates a new FoodEvent (indicating that a user has taken food for this meal). If the request is malformed (
        i.e. missing the user's email), returns a Django Rest Framework Response with a 400 status code. if
        successful, returns a response with status 200.
        """
        user_email = request.data.get("email", None)
        meal = request.data.get("meal", None)
        restrictions = request.data.get("restrictions", None)

        # Ensure that all required parameters are present
        if not (user_email and meal and restrictions):
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        application: Application = get_object_or_404(
            Application, user__email=user_email
        )

        # Ensure that user has checked in
        if not application.status == STATUS_CHECKED_IN:
            return response.Response(
                data={"error": USER_NOT_CHECKED_IN_MSG},
                status=status.HTTP_412_PRECONDITION_FAILED,
            )

        FoodEvent.objects.create(
            user=application.user, meal=meal, restrictions=restrictions
        )
        return response.Response(status=status.HTTP_200_OK)


class CreateWorkshopEventView(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated & (IsVolunteer | permissions.IsAdminUser)
    ]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request: Request, format: str = None):
        user_email = request.data.get("email", None)
        if not user_email:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        application: Application = get_object_or_404(
            Application, user__email=user_email
        )
        if not application.status == STATUS_CHECKED_IN:
            return response.Response(
                data={"error": USER_NOT_CHECKED_IN_MSG},
                status=status.HTTP_412_PRECONDITION_FAILED,
            )
        WorkshopEvent.objects.create(user=application.user)
        return response.Response(status=status.HTTP_200_OK)
