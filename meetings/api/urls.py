from django.urls import path

from meetings.api.views import (  # ContactDeleteAPIView,; ContactDetailAPIView,; ContactListAPIView,; ContactUpdateAPIView,
    MeeetingsCreateAPIView,
    MeetingListApi,
)

app_name = "meeting-api"


urlpatterns = [
    path("create/", MeeetingsCreateAPIView.as_view(), name="create"),
    path("list/", MeetingListApi.as_view(), name="list"),

]
