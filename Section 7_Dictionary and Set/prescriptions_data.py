# drugs
amlodipine = ("Amlodipine", "Blood pressure")
buspirone = ("Buspirone", "Anxiety disorders")
carbimazole = ("Carbimazole", "Antithyroid agent")
citalopram = ("Citalopram", "Antidepressant")
edoxaban = ("Edoxaban", "anti-coagulant")
erythromycin = ("Erythromycin", "Antibiotic")
lusinopril = ("Lusinopril", "High blood pressure")
metformin = ("Metformin", "Type 2 diabetes")
methotrexate = ("Methotrexate", "Rheumatoid arthritis")
paracetamol = ("Paracetamol", "Painkiller")
propranol = ("Propranol", "Beta blocker")
simvastatin = ("Simvastatin", "High cholesterol")
warfarin = ("Warfarin", "anti-coagulant")

# Drugs that shouldn't be taken together
adverse_interactions = [
    {metformin, amlodipine},
    {simvastatin, erythromycin},
    {citalopram, buspirone},
    {warfarin, citalopram},
    {warfarin, edoxaban},
    {warfarin, erythromycin},
    {warfarin, amlodipine},
]

# Patient prescriptions
patients = {
    "Anne": {methotrexate, paracetamol},
    "Bob": {carbimazole, erythromycin, methotrexate, paracetamol},
    "Charley": {buspirone, lusinopril, metformin},
    "Denise": {amlodipine, lusinopril, metformin, warfarin},
    "Eddie": {amlodipine, propranol, simvastatin, warfarin},
    "Frank": {buspirone, citalopram, propranol, warfarin},
    "Georgia": {carbimazole, edoxaban, warfarin},
    "Helmut": {erythromycin, paracetamol, propranol, simvastatin},
    "Izabella": {amlodipine, citalopram, simvastatin, warfarin},
    "John": {simvastatin},
    "Kenny": {amlodipine, citalopram, metformin},
}