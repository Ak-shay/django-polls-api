from django.urls import path, include
from . import apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', apiviews.PollViewSet, base_name='polls')

urlpatterns = [
	path("polls/<int:pk>/choices/", apiviews.ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", apiviews.CreateVote.as_view(), name="create_vote"),
	
]
urlpatterns += router.urls