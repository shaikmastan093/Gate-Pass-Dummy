# serializers.py
from rest_framework import serializers
from .models import VisitorTable
from visitor.mixins import EncryptedFieldMixin

class VisitorTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorTable
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Decrypt sensitive fields
        representation['name'] = EncryptedFieldMixin().decrypt(representation['name'])
        representation['mobile'] = EncryptedFieldMixin().decrypt(representation['mobile'])
        representation['visiting_mobile'] = EncryptedFieldMixin().decrypt(representation['visiting_mobile'])
        representation['visit_person'] = EncryptedFieldMixin().decrypt(representation['visit_person'])
        representation['address'] = EncryptedFieldMixin().decrypt(representation['address'])

        return representation
