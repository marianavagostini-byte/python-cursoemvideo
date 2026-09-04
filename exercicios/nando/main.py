from fastapi import FastAPI

# Inicializa o aplicativo FastAPI
app = FastAPI(
    title="FastAPI Bootstrap",
    description="API inicial com endpoints de exemplo",
    version="1.0.0",
    docs_url="/docs"
)

@app.get("/phoda")
def sou_phoda():
    """
    Retorna uma mensagem simples de boas-vindas.
    """
    return "Eu sou Phoda!!!"

@app.get("/helloworld")
def read_hello_world():
    """
    Retorna uma mensagem simples de boas-vindas.
    """
    return {"message": "Hello World"}

@app.get("/check")
def health_check():
    """
    Retorna o status atual da aplicação (Health Check).
    """
    return {
        "status": "online",
        "details": "Application is running smoothly"
    }
