from django.shortcuts import render
from django.http import JsonResponse
from random import randrange
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()

# def banners(request):
# 	data = [
# 		{
# 			"id": "123",
# 			"category": 55,
# 			"price": 500.67,
# 			"count": 12,
# 			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
# 			"title": "video card",
# 			"description": "description of the product",
# 			"freeDelivery": True,
# 			"images": [
# 				{
# 					"src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
# 					"alt": "any alt text",
# 				}
# 			],
# 			"tags": [
# 				"string"
# 			],
# 			"reviews": 5,
# 			"rating": 4.6
# 		},
# 	]
# 	return JsonResponse(data, safe=False)





# def productsPopular(request):
# 	data = [
# 		{
# 			"id": "123",
# 			"category": 55,
# 			"price": 500.67,
# 			"count": 12,
# 			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
# 			"title": "video card",
# 			"description": "description of the product",
# 			"freeDelivery": True,
# 			"images": [
# 					{
# 						"src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
# 						"alt": "hello alt",
# 					}
# 			 ],
# 			 "tags": [
# 					{
# 						"id": 0,
# 						"name": "Hello world"
# 					}
# 			 ],
# 			"reviews": 5,
# 			"rating": 4.6
# 		}
# 	]
# 	return JsonResponse(data, safe=False)
#
# def productsLimited(request):
# 	data = [
# 		{
# 			"id": "123",
# 			"category": 55,
# 			"price": 500.67,
# 			"count": 12,
# 			"date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
# 			"title": "video card",
# 			"description": "description of the product",
# 			"freeDelivery": True,
# 			"images": [
# 					{
# 						"src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
# 						"alt": "hello alt",
# 					}
# 			 ],
# 			 "tags": [
# 					{
# 						"id": 0,
# 						"name": "Hello world"
# 					}
# 			 ],
# 			"reviews": 5,
# 			"rating": 4.6
# 		}
# 	]
# 	return JsonResponse(data, safe=False)

def sales(request):
	data = {
		'items': [
			{
				"id": 123,
				"price": 500.67,
				"salePrice": 200.67,
				"dateFrom": "2023-05-08",
				"dateTo": "2023-05-20",
				"title": "video card",
				"images": [
						{
							"src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
							"alt": "hello alt",
						}
				 ],
			}
		],
		'currentPage': randrange(1, 4),
		'lastPage': 3,
	}
	return JsonResponse(data)
