Here is handled the database and the corresponding API.
<br /><br />
**db_handler.py** implements all the functions that directly operate on the db.
<br />
**api.py** implements the api (with [FastAPI](https://fastapi.tiangolo.com/)) which can be called to use the db_handler functions.
<br/><br/>
To start the API local server: `uvicorn api:app --reload` <br/>
You can check it on http://localhost:8000/ (`/docs` for SwaggerUI)

