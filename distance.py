from geopy.distance import vincenty
tel = {'jack': 4098, 'sape': 4139}
locations = {'Denver, CO':(39.734022,-105.025854),'Fresno, CA':(36.739954,-119.753215), 'San Diego, CA':(32.796923,-117.240534)}

#print tel
#print locations
print locations['Denver, CO']
#ny = (40.7142, -74.0059)
#la = (34.0522,  -118.2436)
#co = (41.8500, -87.6500)
#print(vincenty(ny, la).kilometers)
#print(vincenty(ny, co).kilometers)
print "distance is "+str(vincenty(locations['Denver, CO'],locations['Fresno, CA']).kilometers)

Denver, CO	39.734022	-105.025854
Fresno, CA	36.739954	-119.753215
San Diego, CA	32.796923	-117.240534
Los Angeles, CA	34.060633	-118.302664
Las Vegas, NV	36.130196	-115.275518
Tucson, AZ	32.194065	-110.973896
Phoenix, AZ	33.495796	-111.988259
El Paso, TX	31.743234	-106.368605
Albuquerque, NM	35.110417	-106.578052
Memphis, TN	35.107573	-89.945745
Fort Worth, TX	32.706505	-97.337505
Dallas, TX	32.793897	-96.831871
Oklahoma City, OK	35.485328	-97.537228
Nashville, TN	36.133681	-86.800555
Louisville, KY	38.265116	-85.804479
Indianapolis, IN	39.864685	-86.11815
Charlotte, NC	35.167653	-80.793244
Detroit, MI	42.34947	-83.092711
Milwaukee, WI	43.118765	-87.947834
Columbus, OH	39.956905	-82.964352
Chicago, IL	41.897105	-87.622285
Austin, TX	30.271289	-97.742559
Baltimore, MD	39.29463	-76.625203
Boston, MA	42.357603	-71.068432
Houston, TX	29.759366	-95.359361
Jacksonville, FL	30.329882	-81.651672
New York, NY	40.74838	-73.996705
Philadelphia, PA	39.948908	-75.166109
Portland, OR	45.498819	-122.690258
San Antonio, TX	29.427462	-98.460112
San Francisco, CA	37.781334	-122.416728
San Jose, CA	37.32966	-121.890299
Seattle, WA	47.611435	-122.330456
Washington, DC	38.912217	-77.017691
Portland, OR	45.498819	-122.690258
