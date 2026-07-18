from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import Employee
from .schemas import EmployeeCreate
from .services import calculate_skill_gap
from .services import recommend_learning

router = APIRouter()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    
    finally:
        db.close()


@router.post("/employees")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    db_employee = Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        designation=employee.designation,
        experience=employee.experience,
        skills=", ".join(employee.skills)
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return {
        "message": "Employee created successfully",
        "employee_id": db_employee.id
    }

@router.get("/employees")
def get_all_employees(db: Session = Depends(get_db)):
    
    employees = db.query(Employee).all()
    
    result = []
    
    for emp in employees:
        result.append({
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "department": emp.department,
            "designation": emp.designation,
            "experience": emp.experience,
            "skills": emp.skills.split(", ")
        })
    return result

@router.get("/skill-gap/{employee_id}/{team_name}")
def skill_gap_analysis(
    employee_id: int,
    team_name: str,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()
    
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
        
    employee_skills = employee.skills.split(", ")
    
    missing_skills = calculate_skill_gap(
        employee_skills,
        team_name
    )
    
    learning_recommendations = recommend_learning(
        employee_skills
    )
    
    return {
        "employee": employee.name,
        "team": team_name,
        "missing_skills": missing_skills,
        "recommendations": learning_recommendations
    }

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "id": employee.id,
        "name": employee.name,
        "email": employee.email,
        "department": employee.department,
        "designation": employee.designation,
        "experience": employee.experience,
        "skills": employee.skills.split(", ")
    }

@router.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
    ):
    
    db_employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not db_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.department = employee.department
    db_employee.designation = employee.designation
    db_employee.experience = employee.experience
    db_employee.skills = ", ".join(employee.skills)

    db.commit()
    db.refresh(db_employee)

    return {
        "message": "Employee updated successfully",
        "employee": {
            "id": db_employee.id,
            "name": db_employee.name,
            "email": db_employee.email,
            "department": db_employee.department,
            "designation": db_employee.designation,
            "experience": db_employee.experience,
            "skills": db_employee.skills.split(", ")
        }
    }
    
@router.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
    ):
    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully"
    }