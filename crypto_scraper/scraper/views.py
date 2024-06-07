from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import ScrapingTask
from.serializer import ScrapingTaskSerializer
from.tasks import scrape_coin_data

class ScrapingTaskViewSet(viewsets.ModelViewSet):
    queryset = ScrapingTask.objects.all()
    serializer_class = ScrapingTaskSerializer

class StartScrapingAPIView(APIView):
    def post(self, request):
        coin_names = request.data.get("coin_names")
        if coin_names:
            for coin_name in coin_names:
                scraping_task = ScrapingTask.objects.create(coin=coin_name)
                scrape_coin_data.delay(scraping_task.id)
            serializer = ScrapingTaskSerializer(scraping_task, many=True)
            return Response({"job_id": scraping_task.id, "tasks": serializer.data})
        else:
            return Response({"error": "Please provide a list of coin names."}, status=400)

class ScrapingStatusAPIView(APIView):
    def get(self, request, job_id):
        scraping_task = ScrapingTask.objects.get(id=job_id)
        if scraping_task.completed:
            serializer = ScrapingTaskSerializer(scraping_task)
            return Response(serializer.data)
        else:
            return Response({"status": "Scraping in progress."}, status=202)



