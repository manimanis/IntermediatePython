# file03/exemple08.py
def alpha_chars():
    for i in range(65, 91):
        yield chr(i)

for i in alpha_chars():
    print(i, end=",")
print()
# A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,

alpha_chars2 = (chr(i) for i in range(65, 91))
print(*alpha_chars2, sep=",")