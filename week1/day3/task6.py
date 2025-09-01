def school(sname):
    def name():
        print(f"School Name Is {sname}")
    return name;

st = school("Bridgeon Solutions")
st()