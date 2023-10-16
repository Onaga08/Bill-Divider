def calculate_bill(total_bill, total_unit, m1, m2, m3):
    animesh = 0
    jalaj = 0
    mayank = 0
    saket = 0
    pradyumn = 0
    
    per_unit = float(total_bill/total_unit)
    ac1_cost = float(m1*per_unit)
    ac2_cost =float(m2*per_unit)
    ac3_cost = float(m3*per_unit)
    
    animesh += float(ac1_cost/2)
    jalaj += float(ac1_cost/2)
    mayank += float(ac2_cost/2)
    saket += float(ac2_cost/2)
    pradyumn += float(ac3_cost)
    
    rem_bill = float(total_bill-(ac1_cost+ac2_cost+ac3_cost))
    
    animesh += float(rem_bill/5)
    jalaj += float(rem_bill/5)
    mayank += float(rem_bill/5)
    saket += float(rem_bill/5)
    pradyumn += float(rem_bill/5)
    
    return animesh, jalaj, mayank, saket, pradyumn
    
    
