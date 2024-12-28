from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Worker
from .serializers import WorkerSerializer


class WorkerListView(ListAPIView):
    """Список работников по номеру бригады."""

    serializer_class = WorkerSerializer

    def get_queryset(self):
        brigade_id = self.kwargs["brigade_id"]
        return Worker.objects.filter(brigade_number=brigade_id)


class WorkerDetailView(RetrieveAPIView):
    """Просмотр конкретного работника."""

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    lookup_field = "id"
