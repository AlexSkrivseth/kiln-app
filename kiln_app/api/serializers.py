from rest_framework import serializers

from dashboard.models import Reading, Load, Kiln


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ['temperature', 'humidity', 'timestamp', 'load']
