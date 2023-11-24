from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer, JournalistSerializer
from django.http import Http404
from .models import Article, Journalist


@api_view(['GET'])
def get_all_articles(request):
    articles = Article.objects.all()
    if not articles:
        return Response({
            'status': 'error',
            'message': 'No articles found',
        }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ArticleSerializer(articles, many=True)
    return Response({
        'status': 'success',
        'message': 'articles retrieved successfully',
        'count': len(serializer.data),
        'articles': serializer.data
    },status=status.HTTP_200_OK)



@api_view(['POST'])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 'success',
            'message': 'article created successfully',
            'article': serializer.data
            }, status=status.HTTP_201_CREATED)
    
    return Response({
        'status': 'error',
        'message': 'article creation failed',
        'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def single_article(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'article not found',
            }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response({
            'status': 'success',
            'message': 'article retrieved successfully',
            'article': serializer.data
            }, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'article updated successfully',
                'article': serializer.data
                }, status=status.HTTP_200_OK)
        return Response({
            'status': 'error',
            'message': 'article update failed',
            'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        article.delete()
        return Response({
            'status': 'success',
            'message': 'article deleted successfully',
            }, status=status.HTTP_200_OK)



class ArticleListCreate(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({
            'status': 'success',
            'message': 'articles retrieved successfully',
            'articles': serializer.data
            }, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'article created successfully',
                'article': serializer.data
                }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'error',
            'message': 'article creation failed',
            'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_all_journalists(request):
    journalist = Journalist.objects.all()
    if not journalist:
        return Response({
            'status': 'error',
            'message': 'No journalist found',
        }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = JournalistSerializer(journalist, many=True)
    return Response({
        'status': 'success',
        'message': 'journalists retrieved successfully',
        'count': len(serializer.data),
        'journalists': serializer.data
    },status=status.HTTP_200_OK)



@api_view(['POST'])
def create_journalist(request):
    # serializer = JournalistSerializer(data=request.POST)
    # If you're expecting JSON data, you can use the following instead:
    serializer = JournalistSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 'success',
            'message': 'Journalist created successfully',
            'journalist': serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response({
        'status': 'error',
        'message': 'Journalist creation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)




# ========================================================
class ArticleDetail(APIView):
    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article)
            return Response({
                'status': 'success',
                'message': 'Article retrieved successfully',
                'article': serializer.data
            }, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            raise Http404("Article does not exist")

    def put(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404("Article does not exist")

        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Article updated successfully',
                'article': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': 'error',
            'message': 'Article update failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404("Article does not exist")

        article.delete()
        return Response({
            'status': 'success',
            'message': 'Article deleted successfully',
        }, status=status.HTTP_200_OK)
