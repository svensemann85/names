from rest_framework import serializers
from names.models import Name
from names.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class NameSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)

    def name_is_unique(self):
        print(self.data)
        return True

    class Meta:
        model = Name
        fields = '__all__'