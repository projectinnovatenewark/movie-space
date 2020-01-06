from django.db import models
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from moviespace.movies.models import User, Comment

class UserType(DjangoObjectType):
    class Meta:
        model = User

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class Query(ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    comment = graphene.Field(CommentType, id=graphene.Int())
    users = graphene.List(UserType)
    comments= graphene.List(CommentType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return User.objects.get(pk=id)

        return 'Nothin going on here'

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Comment.objects.get(pk=id)

        return 'Nothin going on here'

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()

# Create Input Object Types
class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()

class CommentInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    comment = graphene.String()

# Create mutations for actors
class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        user_instance = User(name=input.name)
        user_instance.save()
        return CreateUser(ok=ok, user=user_instance)

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = UserInput(required=True)

    ok = graphene.Boolean()
    User = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        user_instance = User.objects.get(pk=id)
        if user_instance:
            ok = True
            user_instance.name = input.name
            user_instance.save()
            return UpdateUser(ok=ok, user=user_instance)

        return UpdateUser(ok=ok, user=None)

# Create mutations for movies
class CreateComment(graphene.Mutation):
    class Arguments:
        input = CommentInput(required=True)

    ok = graphene.Boolean()
    Comment = graphene.Field(CommentType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        for user_input in input.actors:
          user = User.objects.get(pk=user_input.id)
          if user is None:
            return CreateComment(ok=False, comment=None)
          user.append(user)
        comment_instance = Comment(
          title=input.title,
          year=input.year
          )
        comment_instance.save()
        comment_instance.user.set(user)
        return CreateComment(ok=ok, comment=comment_instance)


class UpdateComment(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = UserInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(CommentType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        movie_instance = Movie.objects.get(pk=id)
        if movie_instance:
            ok = True
            actors = []
            for actor_input in input.actors:
              actor = Actor.objects.get(pk=actor_input.id)
              if actor is None:
                return UpdateMovie(ok=False, movie=None)
              actors.append(actor)
            movie_instance.title=input.title
            movie_instance.year=input.yearce.save()
            movie_instance.actors.set(actors)
            return UpdateMovie(ok=ok, movie=movie_instance)
        return UpdateMovie(ok=ok, movie=None)

class Mutation(graphene.ObjectType):
    create_actor = CreateUser.Field()
    update_actor = UpdateUser.Field()
    create_movie = CreateComment.Field()
    update_movie = UpdateComment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)