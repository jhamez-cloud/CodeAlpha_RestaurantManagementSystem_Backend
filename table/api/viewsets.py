from config.viewsets import StandardViewset
from table.serializers import TableSerializer
from table.models import Table

class TableViewset(StandardViewset):
    queryset = Table.objects.all()
    serializer_class = TableSerializer