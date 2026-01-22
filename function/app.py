from fastapi import FastAPI, Request
import logging
import json
from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/access.log",
    level=logging.INFO,
    format="%(message)s"
)

app = FastAPI()

@app.post("/vulnerable")
async def vulnerable(request: Request):
    body = await request.body()

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.client.host,
        "path": request.url.path,
        "payload_size": len(body)
    }

    logging.info(json.dumps(log_entry))
    return {"status": "processed"}
