from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, ForeignKey

db = SQLAlchemy()

class RiskType(db.Model):
    __tablename__ = "risk_type"
    id = db.Column(db.Integer, primary_key=True)
    riskName = db.Column(db.String(180), nullable=False)
    def serialize(self):
        data = {
            'id': self.id,
            'riskName': str(self.riskName).strip()
        }
        return data

    def __repr__(self):
        return '<RiskType %r>' % self.riskName

class RiskField(db.Model):
    __tablename__ = "risk_field"
    id = db.Column(db.Integer, primary_key=True)
    riskTypeID = db.Column(db.Integer,ForeignKey("risk_type.id"), nullable=False)
    fieldName = db.Column(db.String(180), nullable=False)
    fieldtype = db.Column(db.String(180), nullable=False)

class EnumForRiskField(db.Model):
    __tablename__ = "enum_for_risk_field"
    id = db.Column(db.Integer, primary_key=True)
    riskTypeID = db.Column(db.Integer,ForeignKey("risk_field.id"), nullable=False)
    enumOption = db.Column(db.String(180), nullable=False)
