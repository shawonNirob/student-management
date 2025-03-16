import requests
from fastapi import HTTPException
import json
from app.config import settings
from loguru import logger

def get_llm_response(query: str) -> dict:
 
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
    }
    
    payload = {
        "model": settings.MODEL_ID,
        "messages": [
            {
                "role": "system",
                "content": "You're an AI Assistant that knows a database 'student' and a table 'students' where the columns are: not null id (auto increment), not null student_id (this is different from id and must be included in inserts), null university_name, not null contact_number, null email, null age, null gender, null name, null department, null batch_year, null level, not null created_at (server_default), not null updated_at(server_default). There are 2 unique keys: student_id, contact_number."
            },
            {"role": "user", "content": query}
        ],
        "temperature": 0.7
    }
    
    try:
        logger.info(f"Sending request to OpenAI API:\n{json.dumps(payload, indent=2)}")
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload
        )
        
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"OpenAI API error: {response.text}")
        
        result = response.json()
        content = json.loads(result['choices'][0]['message']['content'])
        logger.info(f"LLM response: {content}")
        

        return {
            'action': content.get('action', 'response_message'),
            'data': content.get('data') or content.get('message', 'No data available'),
            'sql': content.get('sql', 'NULL')
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM API request failed: {str(e)}")