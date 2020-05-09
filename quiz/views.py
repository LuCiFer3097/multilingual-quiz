from rest_framework import status
from rest_framework.response import Response
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import render
from .models import *
import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\win10\Desktop\GoogleTransalation\translationApi\translationAPIkey.json"
# Create your views here.

translate_client = translate.Client()
result = translate_client.get_languages()


class translateApi(generics.CreateAPIView):

    def post(self, request):
        dic = request.data.get('dic', '')
        question = dic['question']
        language = dic['language']
        choice = dic['choice']
        a = []
        for i in language:
            for j in list(result):
                if j['name'] == i:
                    a.append(j['language'])
        b = []
        d1 = {}
        a1 = []
        for i in range(len(a)):
            d = {}
            c = []
            d1 = {}
            d['question'] = translate_client.translate(
                question, target_language=a[i])['translatedText']
            for j in choice:
                c.append(translate_client.translate(
                    j, target_language=a[i])['translatedText'])
            d['options'] = c
            d['language'] = language[i]
            d1[language[i]] = d
            a1.append(d1)
            # print(d)
        print(a1)
        # print(choice, question, language)

        return Response({'message': "Success", "result": a1})
