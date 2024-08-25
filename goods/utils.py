# from django.db.models import Q
# from goods.models import Yarn, Adaptations, Products


# def q_search(query):
#     keywords = [word for word in query.split() if len(word) > 2]
#     q_objects = Q()

#     for token in keywords:
#         # q_objects |= Q(name__icontains=token)
#         q_objects |= Q(description__icontains=token)
    
#     yarn_results = Yarn.objects.filter(q_objects)
#     adaptations_results = Adaptations.objects.filter(q_objects)
#     products_results = Products.objects.filter(q_objects)

#     return {
#         'yarn_results': yarn_results,
#         'adaptations_results': adaptations_results,
#         'products_results': products_results
#     }
         
           
           
         
    