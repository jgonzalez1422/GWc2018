import school_scores
list_of_record = school_scores.get_all()

print(list_of_record[0])

for i in list_of_record:
    print(i["State"]["Name"], i["Year"], i["Gender"]["Female"]["Math"])
