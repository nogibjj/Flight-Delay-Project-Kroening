"""FastAPI App to deploy the tools through an AWS Container"""

from fastapi import FastAPI
import uvicorn

# import requests

# from logic.nws_tools import get_alerts, package_alerts, alert_info
# from logic.databricks_tools import (
#    create_and_load_alerts_table,
#    get_alerts_table_contents,
# )
# from logic.opensky_tools import count_us_aircraft, get_opensky_data

app = FastAPI()


@app.get("/")
async def root():
    return {
        "Welcome to this FastAPI app! Use /docs to see the API docs and execute commands."
    }


# run the app
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
