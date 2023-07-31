# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Board
from .serializers import BoardSerializer

def say_hello(request) :
    return render(request, "index.html", {
        "data" : Board.objects.all()
    }) 

# @api_view(['GET', 'POST'])
# def get_board_all(request) :
#     boards = Board.objects.all()
#     # -> Board를 JSON으로 형변환 (Serializer)
#     serializer = BoardSerializer(boards, many=True)
#     return Response(serializer.data)

class Boards(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request) :
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    
    def post(self, request) :
        serializer = BoardSerializer(data=request.data)

        if serializer.is_valid() :
            serializer.save() # create() 메소드를 호출하게 됨 
            return Response(serializer.data)

        return Response(serializer.errors)

class BoardDetail(APIView) :
    def get_object(self, pk) :
        try :
            board = Board.objects.get(pk=pk)
            return board
        except Board.DoesNotExist :
            raise NotFound

    def get(self, request, pk) :
        # pk를 가져와서 -> 보드 한개 가져오기 
        board = self.get_object(pk)
        # 보드 인스턴스를 -> JSON 형변환
        serializer = BoardSerializer(board)
        # Response 객체로 반환  
        return Response(serializer.data)
        
    def put(self, request, pk) :
        board = self.get_object(pk)
        serializer = BoardSerializer(instance=board, data=request.data, partial=True)

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    def delete(self, request, pk) :
        board = self.get_object(pk)
        board.delete()
        return Response({})