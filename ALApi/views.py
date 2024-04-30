from rest_framework.response import Response
from rest_framework.decorators import api_view
from studentInfo.models import StudentInfo
from .serializers import StudentInfoSerializer 

@api_view(['GET'])
def getData(request):
    studentInfo = StudentInfo.objects.all()
    serializer = StudentInfoSerializer(studentInfo, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addStudent(request):
    serializer = StudentInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)