from celery import shared_task
import time
import random
from .models import Job

@shared_task(bind=True, max_retries=3)
def process_job(self, job_id):
    job = Job.objects.get(id=job_id)

    try:
        job.status = 'processing'
        job.save()

        # Simulate random failure
        if random.choice([True, False]):
            raise Exception("Random failure occurred")

        time.sleep(5)

        job.status = 'completed'
        job.result = f"Processed job: {job.name}"
        job.save()

    except Exception as e:
        job.retry_count += 1
        job.save()

        if job.retry_count < job.max_retries:
            raise self.retry(exc=e, countdown=5)  # retry after 5 sec
        else:
            job.status = 'failed'
            job.result = str(e)
            job.save()