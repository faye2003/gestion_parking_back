from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'  # permet ?limit=10
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'status': True,
            'message': 'Liste récupérée avec succès',
            'data': data,
            'meta': {
                'count': self.page.paginator.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            }
        })
