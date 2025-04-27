from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi_app.database import SessionLocal, Fruit
from fastapi_app.models.fruit import FruitCreate, FruitRead 

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[FruitRead])   
def get_all_fruits(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    search: str = Query(None, description="搜尋水果名稱")
):
    query = db.query(Fruit)
    if search:
        query = query.filter(Fruit.name.contains(search))
    return query.offset(skip).limit(limit).all()

@router.post("/", response_model=FruitRead)        
def add_fruit(fruit: FruitCreate, db: Session = Depends(get_db)):
    existing = db.query(Fruit).filter(Fruit.name == fruit.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="水果名稱已存在！")
    db_fruit = Fruit(name=fruit.name, color=fruit.color)
    db.add(db_fruit)
    db.commit()
    db.refresh(db_fruit)
    return db_fruit

@router.put("/{fruit_id}", response_model=FruitRead)
def update_fruit(fruit_id: int, fruit: FruitCreate, db: Session = Depends(get_db)):
    db_fruit = db.query(Fruit).filter(Fruit.id == fruit_id).first()
    if not db_fruit:
        raise HTTPException(status_code=404, detail="水果不存在")

    # 更新資料
    db_fruit.name = fruit.name
    db_fruit.color = fruit.color
    db.commit()
    db.refresh(db_fruit)
    return db_fruit

@router.get("/{fruit_id}", response_model=FruitRead)  
def get_fruit(fruit_id: int, db: Session = Depends(get_db)):
    fruit = db.query(Fruit).filter(Fruit.id == fruit_id).first()
    if not fruit:
        raise HTTPException(status_code=404, detail="找不到這個水果")
    return fruit

@router.delete("/{fruit_id}")
def delete_fruit(fruit_id: int, db: Session = Depends(get_db)):
    fruit = db.query(Fruit).filter(Fruit.id == fruit_id).first()
    if not fruit:
        raise HTTPException(status_code=404, detail="找不到這個水果")
    db.delete(fruit)
    db.commit()
    return {"message": f"已刪除水果 ID {fruit_id}"}

