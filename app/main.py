from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Network Health Checker API"}


@app.get("/health")
def health():
    return {"status": "ok"}
