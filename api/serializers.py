from rest_framework import serializers

from api.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'id',
            'name'
        )


class BookSerializer(serializers.ModelSerializer):

    #Nested Relationship
    author = AuthorSerializer(many=True, read_only=True)
    

    #HypedLinked Related Field
    """
    author = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='author-detail'
    )
    """

    #Primary Key Related Field
    """
    author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """


    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'isbn',
            'language',
            'num_pages'
        )
    
    def validate_language(self, lang):
        if lang in ['eng', 'pt', 'esp', 'ch', 'du', 'fr', 'it', 'ru']:
            return lang
        raise serializers.ValidationError('Language not found')

