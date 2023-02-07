from rest_framework.serializers import ModelSerializer

from organizeEvent.models import Organisation, ToDo, Comptabilite

class ToDoSerializer(ModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'

class OrganisationSerializer(ModelSerializer):
    toDo = ToDoSerializer(many=True, read_only=True)

    class Meta:
        model = Organisation
        fields = '__all__'

class ComptabiliteSerializer(ModelSerializer):

    class Meta:
        model = Comptabilite
        fields = ['date', 'source', 'label', 'amount', 'paiementType', 'isPositive', 'note']