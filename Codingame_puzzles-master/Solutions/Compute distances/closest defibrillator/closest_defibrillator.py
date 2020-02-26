
lon = float(input().replace(',','.'))
lat = float(input().replace(',','.'))
n = int(input())
distance=[]
lieu=[]
d=10**6
for i in range(n):
    defib = input()
    defib = defib.replace(',', '.')
    def_x=defib.split(";")[4:]
    coords = [float(x) for x in def_x]
    lon1=coords[0]
    lat1=coords[1]
    x= (lon1-lon)*math.cos((lat+lat1)/2)
    y=lat1-lat
    temp_d=math.sqrt((x**2)+(y**2))*6371
    if temp_d<d:
        distance.append(temp_d)
        d=temp_d
        lieu=[]
        lieu.append(defib.split(";")[1])    

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print ((' ').join(word for word in lieu))
