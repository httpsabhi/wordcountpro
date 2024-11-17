from fastapi import APIRouter, Depends, HTTPException
from ..utils import get_current_user
from ..insights import generate_vocabulary_insights
from .. import schemas

router = APIRouter()

@router.post("/vocabulary_insights/")
def vocabulary_insights(data: schemas.TextData, current_user: str = Depends(get_current_user)):
    if not data.text or not data.text.strip():
        raise HTTPException(status_code=400, detail="No Text Found")

    try:
        insights = generate_vocabulary_insights(data.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating insights: {str(e)}")

    return {"user": current_user, "insights": insights}
