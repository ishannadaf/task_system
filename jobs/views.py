from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .tasks import process_job
from django.shortcuts import render


@api_view(['POST'])
def create_job(request):
    name = request.data.get('name')

    job = Job.objects.create(name=name)

    process_job.delay(job.id)

    return Response({"job_id": job.id})


@api_view(['GET'])
def job_status(request, job_id):
    job = Job.objects.get(id=job_id)

    return Response({
        "status": job.status,
        "result": job.result
    })
    
    

def dashboard(request):
    return render(request, 'dashboard.html')


@api_view(['GET'])
def all_jobs(request):
    jobs = Job.objects.all().order_by('-created_at')

    data = []
    for job in jobs:
        data.append({
            "id": job.id,
            "name": job.name,
            "status": job.status,
            "result": job.result,
            "retry_count": job.retry_count
        })

    return Response(data)