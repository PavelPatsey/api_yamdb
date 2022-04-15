from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Comments, Reviews
from users.models import User
from titles.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )

    class Meta:
        model = Reviews
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Reviews.objects.all(),
                fields=("title", "author")
            )
        ]


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, 
        slug_field="username"
    )

    class Meta:
        model = Comments
        fields = "__all__"


class SignUpSerializer(serializers.ModelSerializer):
    """
    Использовать имя 'me' в качестве username запрещено.
    Поля email и username должны быть уникальными.
    """
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('email', 'username',)
