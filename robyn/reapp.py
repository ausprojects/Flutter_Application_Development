from robyn import Robyn

app = Robyn(__file__)

@app.get("/")
async def h(request):
 return "Hello World"

app.start(port=8888)
