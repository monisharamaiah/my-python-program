m1=int(input("Enter the marks of the first subject: "))
m2=int(input("Enter the marks of the second subject: "))
m3=int(input("Enter the marks of the third subject: "))
if m1<=m2 and m1<=m3:
  avgmarks=(m2+m3)/2
if m2<=m1 and m2<=m3:
  avgmarks=(m1+m3)/2
if m3<=m1 and m3<=m2:
  avgmarks=(m1+m2)/2
print("Average marks of the best two subjects is: ",avgmarks)
