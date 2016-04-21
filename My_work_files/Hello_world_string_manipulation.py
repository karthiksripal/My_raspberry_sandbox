a = (u'FRIEND.WAV',)
print a
#print a[:1]
a = str(a)
ltrima = a.replace("(u'","")
rtrima = ltrima.replace("',)","")
print rtrima
print a.strip()


