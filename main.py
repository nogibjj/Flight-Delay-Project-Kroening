"""Web App to deploy the tools through an AWS Container...Eventually"""

from fastapi import FastAPI
import uvicorn

# import requests

from logic.nws_tools import get_alerts, package_alerts, alert_info
from logic.opensky_tools import count_us_aircraft, get_opensky_data

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/nws")
def read_nws():
    return get_alerts()


@app.get("/nws/package")
def read_nws_package():
    return package_alerts()


@app.get("/nws/info")
def read_nws_info():
    return alert_info()


@app.get("/opensky")
def read_opensky():
    return get_opensky_data()


@app.get("/opensky/count")
def read_opensky_count():
    output = count_us_aircraft()
    if output > 5400:
        return (
            "There are currently "
            + str(output)
            + " aircraft in the air above the U.S. right now. That's alot! It is more than the count of 5400 that the FAA says is the upper threshold for traffic."
        )
    elif output > 4750:
        return (
            "There are currently "
            + str(output)
            + " aircraft in the air above the U.S. right now. That's getting to be alot! It is less than the count of 5400 that the FAA says is the upper threshold for traffic."
        )
    else:
        return (
            "There are currently "
            + str(output)
            + " aircraft in the air above the U.S. right now. That's not alot."
        )


# run the app
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
