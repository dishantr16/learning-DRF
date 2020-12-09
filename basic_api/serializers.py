from rest_framework import serializers
from basic_api.models import DPost

class DRFPOST(serializers.ModelSerializer):
    class Meta:
        model = DPost
        fields = '__all__'