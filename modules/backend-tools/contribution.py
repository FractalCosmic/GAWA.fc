# contribution.py
from sqlalchemy.orm import Session
from . import models, schemas

def calculate_contribution(db: Session, user_id: int, component_id: int):
    # 这里应实现具体的贡献度计算逻辑
    # 这只是一个示例实现
    contribution = db.query(models.Contribution).filter(
        models.Contribution.user_id == user_id,
        models.Contribution.component_id == component_id
    ).first()

    if contribution:
        # 假设贡献度与组件的使用次数有关
        contribution.score += 1
    else:
        contribution = models.Contribution(user_id=user_id, component_id=component_id, score=1)
        db.add(contribution)
    
    db.commit()
    return contribution

def distribute_sg_tokens(db: Session):
    total_contribution = db.query(models.Contribution).with_entities(func.sum(models.Contribution.score)).scalar()
    total_sg_tokens = 1000  # 假设每次分配1000个SG代币

    contributions = db.query(models.Contribution).all()
    for contribution in contributions:
        sg_tokens = (contribution.score / total_contribution) * total_sg_tokens
        contribution.sg_tokens += sg_tokens
    
    db.commit()

# 在main.py中添加新的API端点
@app.post("/contribution/{user_id}/{component_id}")
def record_contribution(user_id: int, component_id: int, db: Session = Depends(get_db)):
    return calculate_contribution(db, user_id, component_id)

@app.post("/distribute_tokens")
def distribute_tokens(db: Session = Depends(get_db)):
    distribute_sg_tokens(db)
    return {"message": "SG tokens distributed successfully"}
