from django.shortcuts import render
import pyrebase
from PIL import Image
from PIL.ExifTags import TAGS
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


def addHungerSpot(request):
    if request.method == 'POST':
        doc = request.FILES['upload']
        for (tag, value) in Image.open(doc)._getexif().items():
            print('{} -> {}'.format(TAGS.get(tag), value))
    return render(request, 'users/addHungerSpot.html')

