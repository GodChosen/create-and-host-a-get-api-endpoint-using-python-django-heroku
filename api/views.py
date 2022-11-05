from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import SlackUser
from api.serializers import SlackUserSerializer
from django.http import JsonResponse
import json



# @api_view(['GET'])
# def slackUser_list(request, format=None):
    
#     slackUser = SlackUser.objects.all()
#     serializer = SlackUserSerializer(slackUser, many=True)
#     return Response(serializer.data[0])

@api_view(['GET', 'POST'])
def slackUser_list(request, format=None):
    
    if request.method == 'GET':
        slackUser = SlackUser.objects.all()
        serializer = SlackUserSerializer(slackUser, many=True)
        return Response(serializer.data[0])
    
    else:
        return Response({"message": 'Just testing', "data": request.data})


# import os
# import openai
# from django.http import JsonResponse, HttpRequest
# from django.views.decorators.csrf import csrf_exempt
# import json

# operation_types = {'multiplication':'*', 'addition':'+', 'subtraction':'-'} 

# openai.api_key = os.environ.get("API_KEY")


# @csrf_exempt
# def get_evaluation(request: HttpRequest):
#     if request.POST:
#         payload = request.POST
#     else:
#          payload = json.loads(request.body.decode('utf-8'))
     
#     result = None
#     operation_type = None
#     payload_ot = payload['operation_type'].strip().lower()
    
#     if payload_ot in operation_types:

#         operation_type = payload_ot 
#         result = eval(f'{payload["x"]}{operation_types[payload_ot]}{payload["y"]}')
  

#     else:
        
#         synonyms = {'product':'multiplication', 'difference':'subtraction', 'sum':'addition'}
        
#         response = openai.Completion.create(
#             model="text-davinci-002",
#             prompt=f"{payload_ot} \n\n| solution | operation_type |",
#             temperature=0,
#             max_tokens=100,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )
#         _, result, operation_type, _=[x.strip() for x in  [y for y in response.choices[0].text.split('\n') if y][-1].split('|')]
#         operation_type = operation_type if not operation_type in synonyms else synonyms[operation_type]
      
    
#     return JsonResponse({"slackUsername":"BarryDee", "result":int(result) ,"operation_type":operation_type})


