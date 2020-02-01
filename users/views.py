from django.shortcuts import render
import pyrebase
import exifread
import re
# Create your views here.

firebaseConfig = {
    'apiKey': "AIzaSyABnAiZ-S9AYFdlCChXmWLM2EXw4DPMPt8",
    'authDomain': "foodredistribution.firebaseapp.com",
    'databaseURL': "https://foodredistribution.firebaseio.com",
    'projectId': "foodredistribution",
    'storageBucket': "foodredistribution.appspot.com",
    'messagingSenderId': "420414227380",
    'appId': "1:420414227380:web:e4e16a893e873a018a28e1",
    'measurementId': "G-HH8KFXB1FW"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database = firebase.database()


def base(request):
    return render(request, 'users/base.html')

def formatCoordinates(coor):
    coor = re.sub(r'\[|\]|,','',coor)
    coor = coor.split(' ')
    ans = 0
    for i in range(len(coor)):
        if '/' in coor[i]:
            x = int(coor[i][:coor[i].index('/')])
            y = int(coor[i][coor[i].index('/') + 1:])
            coor[i] = x / y
        else:
            coor[i] = float(coor[i])

        if i == 0:
            ans += coor[i]

        if i == 1:
            ans += (coor[i] * 0.0166667)

        if i == 2:
            ans += (coor[i] * 0.000277778)

    return ans

def addHungerSpot(request):
    if request.method == 'POST':
        doc = request.FILES['upload']
        tags = exifread.process_file(doc,'rb')
        geo = {i : tags[i] for i in tags.keys() if i.startswith('GPS')}
        latitude = str(geo['GPS GPSLatitude'])
        latitude = formatCoordinates(latitude)
        longitude = str(geo['GPS GPSLongitude'])
        longitude = formatCoordinates(longitude)

        # print(latitude + " " + longitude)
        print(latitude)
        print(longitude)
    return render(request, 'users/addHungerSpot.html')

