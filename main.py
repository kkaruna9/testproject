from fastapi import FastAPI
from utils import create_json

app = FastAPI()


@app.get("/num/{num}")
def read_item(num: int):
    if (num % 3) == 0 and (num % 5) == 0:
        return create_json.convert_to_json({'multiple of 3 and 5': 'GN'})
    elif (num % 3) == 0:
        return create_json.convert_to_json({'multiple of 3': 'G'})
    elif (num % 5) == 0:
        return create_json.convert_to_json({'multiple of 5': 'N'})
    else:
        return create_json.convert_to_json({'invalid': num})


