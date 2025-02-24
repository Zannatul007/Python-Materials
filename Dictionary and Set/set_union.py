from prescriptions_data import adverse_interactions

union_of_adverse_interactions = {*""}
for interaction in adverse_interactions:
    print(interaction)
    union_of_adverse_interactions = union_of_adverse_interactions.union(interaction)
print("-"*50)
print(sorted(union_of_adverse_interactions))