import strawberry
from .resolvers import Query, Mutations

schema = strawberry.Schema(query=Query, mutation= Mutations)
