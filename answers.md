# CMPS 2200 Recitation 08

## Answers

**Name:**_________________________
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
O((V+E)LogV)



- **2b)**
while current is not None:
        path.append(current)
        current = parents.get(current)
return ''.join(path[::-1])

