from rest_framework import serializers
from studentInfo.models import StudentInfo

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'