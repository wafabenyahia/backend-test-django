# from django.contrib.auth import authenticate
import json

from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from  rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http.response import JsonResponse
from TestApp.models import User, Entreprise, Responsable, Pdl
from TestApp.serializers import UserSerializer, EntrepriseSerializer, LoginSerializer, GETUserSerializer, \
    GETEntrepriseSerializer, ResponsableSerializer, GETResponsableSerializer, PDLSerializer, GETPDLSerializer


@api_view(['GET'])
def view_entreprise(request):
    if request.query_params:
        items = Entreprise.objects.filter(**request.query_params.dict())
    else:
        items = Entreprise.objects.all()

    if items:
        serializer = GETEntrepriseSerializer(items, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    else:
        return JsonResponse("Failed to get ",safe= False)
@api_view(['GET'])
def get_entreprise_id(request, id):
    try:
        entreprise = Entreprise.objects.get(idEntrprise=id)
        serializer = EntrepriseSerializer(entreprise)
        return Response(serializer.data)
    except Entreprise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def get_responsable_id(request, id):
    try:
        responsable = Responsable.objects.get(entreprise__idEntrprise=id)
        serializer = ResponsableSerializer(responsable)
        return Response(serializer.data)
    except Responsable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def get_pdl_id(request, id):
    try:
        responsable = Pdl.objects.get(entreprise__idEntrprise=id)
        serializer = PDLSerializer(responsable)
        return Response(serializer.data)
    except Pdl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def add_entreprise(request):
    try:
        data = json.loads(request.body)
        user_id = data.get('userId')  # Extract userId from JSON data
        if User.objects.filter(userId=user_id).exists():
            return JsonResponse({'error': 'error user '}, status=400)

        entreprise_serializer = EntrepriseSerializer(data=data)

        if entreprise_serializer.is_valid():
            entreprise_saved = entreprise_serializer.save()
            serialized_data = GETEntrepriseSerializer(entreprise_saved).data
            return JsonResponse(serialized_data, status=201)

        return JsonResponse({'error': 'Failed to add'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
@api_view(['POST'])
def add_responsable(request):
    try:
        responsable_serializer = ResponsableSerializer(data=request.data)
        if responsable_serializer.is_valid():
            responsable_saved = responsable_serializer.save()
            serialized_data = GETResponsableSerializer(responsable_saved).data
            return JsonResponse(serialized_data, status=201)

        return JsonResponse({'error': 'Failed to add'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
@api_view(['POST'])
def add_pdl(request):
    try:
        pdl_serializer = PDLSerializer(data=request.data)
        if pdl_serializer.is_valid():
            responsable_saved = pdl_serializer.save()
            serialized_data = GETPDLSerializer(responsable_saved).data
            return JsonResponse(serialized_data, status=201)

        return JsonResponse({'error': 'Failed to add'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = GETUserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def add_user(request):
    user = UserSerializer(data=request.data)

    if User.objects.filter(**request.data).exists():
        return JsonResponse({'error': 'This data already exists'}, status=400)

    if user.is_valid():
        user.save()
        return JsonResponse("Added Sucessfully", safe=False)
    return JsonResponse("Failed to add", safe=False,status=400)

@api_view(['POST'])
def login(request):
    if 'email' in request.data and 'password'  in request.data:
        email = request.data["email"]
        password = request.data["password"]
        try:
            user = User.objects.get(password=password, email=email)
            return Response(GETUserSerializer(user).data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'email or password not in body '}, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def EntrepriseApi(request,id=0):
#     if request.method =='GET':
#         entreprises = Entreprise.objects.all()
#         entreprises_serializer = EntrepriseSerializer(entreprises,many=True)
#         return  JsonResponse(entreprises_serializer.data, safe= False)
#     elif request.method =='POST':
#         entreprise_data = JSONParser.parse(request)
#         entreprises_serializer = EntrepriseSerializer(data= entreprise_data)
#         if entreprises_serializer.is_valid():
#             entreprises_serializer.save()
#             return JsonResponse("Added Sucessfully",safe= False)
#         return JsonResponse("Failed to add", safe= False)
#     elif request.method =='PUT':
#         entreprise_data = JSONParser.parse(request)
#         entreprise = Entreprise.objects.get(entrepriseId=entreprise_data['entrepriseId'])
#         entreprises_serializer = EntrepriseSerializer(entreprise,data= entreprise_data)
#         if entreprises_serializer.is_valid():
#             entreprises_serializer.save()
#             return JsonResponse("update Sucessfully",safe= False)
#         return JsonResponse("Failed to update", safe= False)
#     elif request.method =='DELETE':
#         entreprise = Entreprise.objects.get(entrepriseId=id)
#         entreprise.delete()
#         return JsonResponse("Deleted", safe= False)