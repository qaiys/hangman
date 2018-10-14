#I wanted to make my own version of the enigma code over
#the summer because i just saw the movie 'The Imitation Game' 
#but it was really hard.
#I was pretty happy with this though, so I decided to use it!

global inner
inner = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
         "s","t","u","v","w","x","y","z"," ","0","1","2","3","4","5","6","7","8",
         "9",",",".","!","?"]
def encrypt(what,where):
    shift = 1
    p = 0 
    final = []
    msg = what

    for i in msg:
      sinner = inner[shift:]+inner[:shift]
      shift += 1
      if shift >= len(inner):
        shift = 1 
      final.append(sinner[inner.index(msg[p])])
      p += 1

    final = ''.join(final)
    where.write(final)

def decrypt(what): 
    shift = 1
    p = 0 
    final = []
    msg = what

    for i in msg:
      soutter = inner[len(inner)-shift:]+inner[:len(inner)-shift]
      shift += 1
      if shift >= len(inner):
        shift = 1 
      final.append(soutter[inner.index(msg[p])])
      p += 1

    final = ''.join(final)
    return final


