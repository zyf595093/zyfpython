L=['Hello','World',18,'Apple',None]
L2=[s.lower() for s in L if isinstance(s,str)]
print (L2)