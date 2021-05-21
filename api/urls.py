from rest_framework.routers import DefaultRouter

from api.views import AuthorViewSet, BookViewSet


#Especifica o namespace das URLsConfs adicionadas
app_name = 'api'

#Indica que não é necessário o uso de '/' no final da url
router = DefaultRouter(trailing_slash=False)

#Recebe 2 parâmetros: 1º prefixo que será usado no URL
#                   2º Viewset que responderá as URLS
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = router.urls
