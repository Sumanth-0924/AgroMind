from soil_diagnosis import diagnose_soil

result = diagnose_soil("rice", N=40, P=50, K=45)

print("Soil Report:")
print(result)