from rest_framework import serializers
from .models import Student

## Database information serialised into Json API
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("name","password","ColourFilter","SoundFilter")