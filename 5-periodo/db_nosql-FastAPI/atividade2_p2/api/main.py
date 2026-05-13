import os
import time
from fastapi import FastAPI, Request, Response
import redis

app = FastAPI()

redis_client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    redis_client.incr("stats:total_requests")
    
    client_ip = request.client.host
    rate_key = f"rate_limit:{client_ip}"
    
    current_requests = redis_client.incr(rate_key)
    
    if current_requests == 1:
        redis_client.expire(rate_key, 60)
        
    if current_requests > 10:
        return Response(content="Rate limit exceeded. Tente novamente mais tarde.", status_code=429)
        
    response = await call_next(request)
    return response

@app.get("/stats")
def get_stats():
    total = redis_client.get("stats:total_requests")
    return {"total_requests_processed": total}

@app.get("/dados-pesados")
def get_data(response: Response):
    cache_key = "cache:dados_pesados"
    cached_data = redis_client.get(cache_key)
    
    if cached_data:
        response.headers["X-Cache"] = "HIT"
        return {"data": cached_data, "source": "redis_cache"}
        
    time.sleep(2) 
    fresh_data = "Dados processados e recém-gerados"
    
    redis_client.setex(cache_key, 30, fresh_data)
    
    response.headers["X-Cache"] = "MISS"
    return {"data": fresh_data, "source": "banco_de_dados"}

@app.post("/jobs")
def create_job(job_id: str):
    redis_client.lpush("queue:jobs", job_id)
    return {"status": "Job enviado para a fila", "job_id": job_id}