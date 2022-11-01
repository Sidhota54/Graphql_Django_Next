import graphene
from graphene_django import DjangoObjectType

from app.models import Columns
from app.models import Store

#STORE QUERY & MUTATION(CRUD)

class StoreType(DjangoObjectType):
    class Meta:
        model = Store
        fields = ("id" , "store_name" , "store_logo" , "admin_mail")

class StoreQuery(graphene.ObjectType):
    all_store = graphene.List(StoreType)
       
    def resolve_all_store(root,info):
        return Store.objects.all()

class CreateStore(graphene.Mutation):
    class Arguments:
        store_name = graphene.String()
        store_logo = graphene.String()
        admin_mail = graphene.String()
        
    store = graphene.Field(StoreType)
    
    @classmethod
    def mutate(cls, root, info, **store_data):
        store = Store(
            store_name = store_data.get("store_name"),
            store_logo = store_data.get("store_logo"),
            admin_mail = store_data.get("admin_mail")
        )
        store.save()
        return CreateStore(store = store)

class StoreMutation(graphene.ObjectType):
    create_store = CreateStore.Field()

class DeleteStore(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        
    store = graphene.Field(StoreType)
    
    @classmethod
    def mutate(cls, root, info, id):
        store = Store.objects.get(id=id)
        store.delete()
        return DeleteStore(store)
    
class DeleteStoreMutation(graphene.ObjectType):
    delete_store = DeleteStore.Field()

class UpdateStore(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        store_name = graphene.String() 
        store_logo = graphene.String() 
        admin_mail = graphene.String()  
    
    store = graphene.Field(StoreType)  
    
    @classmethod
    def mutate(cls, root, info, id , **update_data):
        store = Store.objects.filter(id=id)
        if store:
            params = update_data
            store.update(**{k: v for k, v in params.items() if params[k]})
            return UpdateStore(store = store.first())
        else:
            print("User with given ID does not exist.")
            
class UpdateStoreMutation(graphene.ObjectType):
    create_store = CreateStore.Field()
    update_store = UpdateStore.Field()
#COLUMN QUERY & MUTATION (CRUD)

class ColumnsType(DjangoObjectType):
    class Meta:
        model = Columns
        fields = ("id" , "name" , "value")
        
class ColumnQuery(graphene.ObjectType):
    all_columns = graphene.List(ColumnsType)
    
    def resolve_all_columns(root, info):
        return Columns.objects.all()

class CreateColumns(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        value = graphene.String()    
        
    columns = graphene.Field(ColumnsType)    
        
    @classmethod
    def mutate(cls, root, info, **columns_data):    
        columns = Columns(
            name = columns_data.get("name"),
            value = columns_data.get("value")
        )
        columns.save()
        return CreateColumns(columns = columns)
    
class ColumnMutation(graphene.ObjectType):
    create_columns = CreateColumns.Field()
    
    
class DeleteColumns(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        
    columns = graphene.Field(ColumnsType)
    
    @classmethod
    def mutate(cls, root, info, id):
        columns = Columns.objects.get(id=id)
        columns.delete()
        return DeleteColumns(columns)
    
class DeleteColumnMutation(graphene.ObjectType):
    delete_columns = DeleteColumns.Field()

class UpdateColumns(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String() 
        value = graphene.String() 
    
    columns = graphene.Field(ColumnsType)  
    
    @classmethod
    def mutate(cls, root, info, id , **update_data):
        columns = Columns.objects.filter(id=id)
        if columns:
            params = update_data
            columns.update(**{k: v for k, v in params.items() if params[k]})
            return UpdateColumns(columns = columns.first())
        else:
            print("User with given ID does not exist.")
            
class UpdateColumnMutation(graphene.ObjectType):
    create_column = CreateColumns.Field()
    update_column = UpdateColumns.Field()
     
class Query(
    StoreQuery,
    ColumnQuery
):
    pass  

class Mutation(
   StoreMutation,
   ColumnMutation,
   DeleteStoreMutation,
   DeleteColumnMutation,
   UpdateStoreMutation,
   UpdateColumnMutation 
):
    pass

schema = graphene.Schema(query = Query , mutation = Mutation)