import random
# # a=int(random.random()*6)
# # print "url"+str(a)
# for x in range(50):
#     print random.randint(0,6)

# charstore = [a
import string

charstore=string.ascii_lowercase+string.digits
id = ""
for x in range(31):
    a = random.randint(0, 35)
    id=id+charstore[a]
print id