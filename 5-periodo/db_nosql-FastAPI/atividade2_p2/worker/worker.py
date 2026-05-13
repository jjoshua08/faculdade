import os
import time
import redis

redis_client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True)
QUEUE_NAME = "queue:jobs"

print("Worker iniciado. Aguardando novos jobs com BRPOP...", flush=True)

while True:
    result = redis_client.brpop(QUEUE_NAME, timeout=0) 
    
    if result:
        queue, job_id = result
        print(f"[*] Consumindo job: {job_id}")
        
        time.sleep(3) 
        
        print(f"[✓] Job {job_id} concluído com sucesso.")