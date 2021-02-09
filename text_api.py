from fastapi import APIRouter
import models
import natasha

router = APIRouter()


@router.get('/api/validate_text')
async def validate_text(text: str) -> bool:
    """
    Api for text validation, whether it can be processed via this service
    It must be at least 20 symbols and at least have 60% of russian letters
    """
    if len(text) >= 20:
        letters = [c.lower() in 'абвгдеёжзийклмнопстуфхцчшщъыьэюя' for c in text]
        trues = list(filter(lambda x: x == True, letters))
        if len(trues) / len(text) >= 0.65:
            return True
    return False


# async def check_spelling(text: str) -> models.SpellingCorrectionsList:
