from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (task_api_view, TaskAPIView, TaskGenericAPIView, 
                    TaskListAPIView, TaskRetrieveAPIView, TaskCreateAPIView,
                    TaskUpdateAPIView, TaskDestroyAPIView, TaskModelViewSet)

router = DefaultRouter()
router.register(r'TaskModelViewSet', TaskModelViewSet, basename='TaskModelViewSet')

urlpatterns = [
    path('api_view/', task_api_view, name="task_api_view"),

    path('APIView/', TaskAPIView.as_view(), name='APIView'),

    path('TaskGenericAPIView/', TaskGenericAPIView.as_view(), name='TaskGenericAPIView'),

    path('TaskListAPIView/', TaskListAPIView.as_view(), name='TaskListAPIView'),

    path('TaskRetrieveAPIView/<int:id>/', TaskRetrieveAPIView.as_view(), name='TaskRetrieveAPIView'),

    path('TaskCreateAPIView/', TaskCreateAPIView.as_view(), name='TaskCreateAPIView'),

    path('TaskUpdateAPIView/<int:id>/', TaskUpdateAPIView.as_view(), name='TaskUpdateAPIView'),

    path('TaskDestroyAPIView/<int:id>/', TaskDestroyAPIView.as_view(), name='TaskDestroyAPIView'),

    path('', include(router.urls)),
]