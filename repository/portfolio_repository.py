from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from config.database import engine

from schemas.portfolio import PortfolioMapped, PortfolioSchema


def get(id : int):
    with Session(engine) as session:
        return session.get(PortfolioSchema, id)
    
def create(payload: PortfolioSchema):
    with Session(engine) as session:
        portfolio = PortfolioMapped(**payload.dict())
        
        try:
            session.add(portfolio)
            session.commit()
            session.refresh(portfolio)    
            
        except IntegrityError as e:
            session.rollback()
            raise HTTPException(status_code=400, detail=f"Error: {e}")
        
        return portfolio