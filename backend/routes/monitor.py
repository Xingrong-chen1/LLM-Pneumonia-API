from fastapi import APIRouter
from prometheus_client import Counter, generate_latest

router = APIRouter()

request_count = Counter("prediction_requests_total", "Total prediction requests")

@router.get("/metrics")
def get_metrics():
    """ return Prometheus paramets """
    request_count.inc()  
    return generate_latest()
