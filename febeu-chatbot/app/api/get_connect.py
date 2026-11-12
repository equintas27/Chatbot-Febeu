from fastapi import FastAPI
from app.database.database import get_connection()

router = APIRouter()

@router.get("/get_connection")
def connect():
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("Select current_database()")
        db_name = cursor.fecthone()[0]
        cursor.close()
        
        return {
            "status": "connected",
            "database_name": db_name
        }
    
    finally:
        connection.close()

