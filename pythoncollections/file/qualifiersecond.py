ft=open("teams","r")
fd=open("drop")
def get_team_set(f):
    st=set()
    for name in f:
        st.add(name.rstrip("\n"))
    return st
st1=get_team_set(ft)
st2=get_team_set(fd)
qualifiers=st1-st2
print(qualifiers)