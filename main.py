from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.session import get_db
from routes import robot, cashflow, erp, pos, integration, dashboard

app = FastAPI()

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).scalar()
        return {"status": "ok", "result": result}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


app.include_router(robot.router)
app.include_router(cashflow.router)
app.include_router(erp.router)
app.include_router(pos.router)
app.include_router(integration.router)
app.include_router(dashboard.router)

