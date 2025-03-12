from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import gradio as gr
import uvicorn

app = FastAPI()


def request(req: gr.Request):
    return {k:req.headers[k] for k in req.headers}

print_request = gr.Interface(request, None, "json")


HTML = """
<!DOCTYPE html>
<html>
<h1>Gradio Request Demo</h1>
<p>Click the button to be redirected to the gradio app!</p>
<button onclick="window.location.pathname='/gradio'">Redirect</button>
</html>
"""

@app.get("/")
def read_main():
    return HTMLResponse(HTML)

@app.get("/foo")
def redirect():
    return RedirectResponse("/gradio")

if __name__ == "__main__":
    app = gr.mount_gradio_app(app, print_request, path="/gradio")
    uvicorn.run(app, port=8080)