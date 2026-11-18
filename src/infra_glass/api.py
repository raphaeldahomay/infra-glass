from fastapi import FastAPI
from infra_glass.core.dns import get_ip_addresses

app = FastAPI()

@app.get("/inspect/{domain_name}")
def trigger_ip_func(domain_name: str):
    try:
        result = get_ip_addresses(domain_name)
        return result
    except Exception:
        return None
