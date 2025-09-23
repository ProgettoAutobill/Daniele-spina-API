from fastapi import FastAPI
from routes import robot, cashflow, erp, pos, integration, dashboard

app = FastAPI()

app.include_router(robot.router)
app.include_router(cashflow.router)
app.include_router(erp.router)
app.include_router(pos.router)
app.include_router(integration.router)
app.include_router(dashboard.router)

