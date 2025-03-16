from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException
from app.llm.llm_integration import get_llm_response
from loguru import logger

def process_llm_query(db: Session, query: str) -> dict:
    
    try:
        llm_response = get_llm_response(query)
        
 
        sql = llm_response.get("sql")
        action = llm_response.get("action")
        data = llm_response.get("data")


        allowed_actions = ("fetch_data", "insert_data", "update_data", "delete_data", "count_data")
        if sql == 'NULL' or action not in allowed_actions:
            logger.warning(f"Invalid action or SQL: action={action}, sql={sql}")
            return {"data": data, "message": "Please provide the valid Instruction", "action": action}

        if action == "fetch_data":
            result = db.execute(text(sql))
            columns = result.keys()
            rows = result.fetchall()

            data = [dict(zip(columns, row)) for row in rows]
            return {
                "data": data,
                "message": "Data fetched successfully"
            }
        
        if action == "insert_data":
            db.execute(text(sql))
            db.commit()
            return {"message": "Data inserted successfully", "data": data}

        if action == "update_data":
            db.execute(text(sql))
            db.commit()
            return {"message": "Data updated successfully", "data": data}

        if action == "delete_data":
            db.execute(text(sql))
            db.commit()
            return {"message": "Data deleted successfully", "data": data}
            
        if action == "count_data":
            result = db.execute(text(sql))
            count = result.scalar()
            return {"message": "Count retrieved successfully", "data": count}

    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate entry detected: Student ID or Contact Number already exists."
        )

    except Exception as e:
        logger.error(f"Database operation failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database operation failed: {str(e)}")
