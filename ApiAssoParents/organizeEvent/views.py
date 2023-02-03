from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
 
from organizeEvent.models import Organisation, ToDo
from organizeEvent.serializers import ToDoSerializer, OrganisationSerializer
 
class ToDoViewSet(ModelViewSet):

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


    def perform_create(self, serializer):
        newToDo = serializer.save()
        orga = Organisation.objects.get(id = newToDo.orgaId)
        orga.toDo.add(newToDo)


class OrganisationViewset(ModelViewSet):

    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    def list(self, request, *arg, **kwargs):
        queryset = self.queryset
        password = request.query_params.get('password', None)
        if password:
            queryset = queryset.filter(password = password)
            if len(queryset) == 0:
                return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data)
    

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        toDos = []
        toDos.append(ToDo.objects.create(**{'description':'Faire une affiche', 'informations' : 'Un membre de l\'association peut utiliser un logiciel de creation pour créer une affiche pour présenter l\'évennement aux autres parents, dans le but de la diffuser ou de l\'afficher', 'orgaId': instance.id}))
        toDos.append(ToDo.objects.create(**{'description': 'Faire des fleches', 'informations' : 'Pour que les parents trouvent le lieu de l\'évennement, faire une affiche avec une fleche pour indiquer où se trouve le lieu de l\'évennement', 'orgaId': instance.id}))
        toDos.append(ToDo.objects.create(**{'description':'Demande d\'autorisation', 'informations' : 'La directrice de l\'ecole (ce.0333468r@ac-bordeaux.fr), Sarah bernhardt (sarahbernhardt@cabordeaux.fr), Bouygues (l.piquetpellorce@bouygues-immobilier.com) ou la mairie (MILLERE Murielle <m.millere@mairie-bordeaux.fr>, BINEAU Jerome <j.bineau@mairie-bordeaux.fr>, SCHMITT Sylvie <sylvie.schmitt@mairie-bordeaux.fr>, MAURIN Vincent <vincent.maurin@mairie-bordeaux.fr>. Pret de matériel : Service Logistique :  logistique-evenement@mairie-bordeaux.fr)', 'orgaId': instance.id}) )
        toDos.append(ToDo.objects.create(**{'description': 'Publication educartable', 'informations' : 'Envoyer un email à la directrice du groupe scolaire Mme RIZZETTO (ce.0333468r@ac-bordeaux.fr) pour diffuser l\'information aux autres parents', 'orgaId': instance.id}))
        toDos.append(ToDo.objects.create(**{'description':'Publication instagram', 'informations' : 'Diffuser et communiquer sur les reseaux', 'orgaId': instance.id}) )
        toDos.append(ToDo.objects.create(**{'description': 'Publication site web', 'informations' : 'Présenter les informations de l\'évenement sur notre site internet', 'orgaId': instance.id}))
        toDos.append(ToDo.objects.create(**{'description':'Afficher les affiches à l\'école', 'informations' : 'Coller, ou attacher les affiches sur l\'école de maniere à être vu par le plus de parents possibles, maternelles comme élémentaires.', 'orgaId': instance.id}) )
        toDos.append(ToDo.objects.create(**{'description': 'Faire les courses manquantes', 'informations' : 'Acheter la nourriture ou les fournitures necessaires, envoyer ensuite la facture au trésorier (Timothée DEMARES) directement ou en message privée sur WhattApp pour être remboursé. Ce remboursement sera anonyme.', 'orgaId': instance.id}))
        toDos.append(ToDo.objects.create(**{'description':'Preparation de la nourriture', 'informations' : 'A vos fourneaux !', 'orgaId': instance.id}) )
        instance.toDo.set(toDos)
        instance.save()
