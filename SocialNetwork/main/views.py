from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userActivitySerializer, postSerializer, preferenceSerializer
from .models import Post, Preference, UserActivity


# Create your views here.

class userActivityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserActivity.objects.all()
    serializer_class = userActivitySerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class PostListCreateView(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = postSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class PreferenceCreateView(ListCreateAPIView):
    queryset = Preference.objects.all()
    serializer_class = preferenceSerializer
    permission_classes = [IsAuthenticated]


class ChangePreferenceView(RetrieveUpdateDestroyAPIView):
    queryset = Preference.objects.all()
    serializer_class = preferenceSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


@api_view(['GET'])
def likesAnalysisView(request):
        queryset = Preference.objects.all()
        q_set = []
        date_from = request.query_params.get('date_from', None)
        date_to = request.query_params.get('date_to', None)

        if date_from is not None and date_to is not None:
            queryset = queryset.filter(date__range=[date_from, date_to], value=1)

            for q in queryset:
                    q_set += [{"day": q.date.strftime("%A %d %b %Y"), "likes": str(q.post.likes), "post": q.post.title}]

        return Response(q_set)

