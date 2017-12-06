import model

RiskType = model.RiskType
RiskField = model.RiskField
EnumForRiskField = model.EnumForRiskField

def getOneRisk():
  return RiskType.query.first()

def getAllRisks():
  return RiskType.query.all()
