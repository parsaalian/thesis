from dateutil.relativedelta import relativedelta

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .utils import get_random_action_point, choose_pattern_leitner, random_question_type
from .models import PatternArticle
from .serializers import PatternArticleSerializer, HistoricalPatternActionPointSerializer
from bourse_refs_api.models import StockHistory
from bourse_refs_api.serializers import StockHistorySerializer


class GenerateQuestion(GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):        
        action_point = get_random_action_point()
        action_point_data = HistoricalPatternActionPointSerializer(action_point).data
        
        pattern_article = PatternArticle.objects.filter(pattern=action_point.pattern)
        pattern_article_data = PatternArticleSerializer(pattern_article, many=True).data
        
        history_start_date = action_point.date - relativedelta(days=30)
        history_end_date = action_point.date + relativedelta(days=5)
        history = StockHistory.objects.filter(
            stock_id=action_point.stock_id,
            date__gte=history_start_date,
            date__lte=history_end_date
        )
        history_data = StockHistorySerializer(history, many=True).data
        
        data = {
            **action_point_data,
            'articles': pattern_article_data,
            'history': history_data
        }
        
        return Response(data, status=status.HTTP_200_OK)


class PracticeQuestion(GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        selected_pattern = choose_pattern_leitner(user)
        action_point = get_random_action_point(selected_pattern)
        
        history = StockHistory.objects.filter(
            stock_id=action_point.stock_id,
            date__gte=action_point.date - relativedelta(days=30),
            date__lte=action_point.date + relativedelta(days=60)
        )
        history_data = StockHistorySerializer(
            history.filter(date__lte=action_point.date + relativedelta(days=2)),
            many=True
        ).data
        
        question = random_question_type(action_point, history)
        question['history'] = history_data
        
        return Response(question, status=status.HTTP_200_OK)