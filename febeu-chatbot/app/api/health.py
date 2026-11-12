from fastapi import APIRouter
from fastapi import HTTPException
from app.database.database import get_connection

router = APIRouter()

@router.get("/health")
def health_check():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        if not connection:
            return {"status": "unhealthy"}
    
        cursor = connection.cursor()
        cursor.execute("Select 1")
        res = cursor.fetchone()
        if res == (1,):
            return {
                "status": "healthy",
                "services": {
                    "fastapi": "healthy",
                    "postgresql": "healthy"
                }
            }
        else:
            return {
                "status": "healthy",
                "services": {
                    "fastapi": "healthy",
                    "postgresql": "unhealthy"
                }
            }

    except HTTPException:
        raise HTTPException (status_code=503, detail="Unavailable")
   
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        
