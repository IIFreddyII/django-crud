from rest_framework.routers import SimpleRouter

from tasks.api.views import ApiTaskViewSet

TASKS_ROUTER = SimpleRouter()
TASKS_ROUTER.register("tasks", ApiTaskViewSet, basename="tasks")
