from fastapi import FastAPI

app = FastAPI(title="PhotoShare API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
