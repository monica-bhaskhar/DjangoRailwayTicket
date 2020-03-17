from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import *
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'index.html')

@csrf_exempt
def ticket_book(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    name = body['name']
    age = body['age']
    gender = body['gender']
    berth = body['berth']

    error_message = ""
    
    if int(age) < 5:        
        BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach=False,status=False).save()
        return JsonResponse({'is_success': 'success','alert':"Tickets should not be allocate for the children's age below 5"})


    if berth == 'Lower' and int(age) < 60:
        if int(age) > 18 and gender == 'Male':
            error_message = "Lower berth should be allocated for persons whose age is above 60."



    if BookTicket.objects.filter(name=name).exists():
        error_message = "Passenger name already exists."

    if error_message:
        return JsonResponse({'is_success': 'unsuccess','error_message': error_message})

    if request.method == 'POST' and request.is_ajax: 
        tickets = BookTicket.objects.all()

        if not tickets:
            BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S1',status='Confirmed').save()
            return JsonResponse({'is_success': 'success','msg':"Booking Confirmed Successfully"})

        else:
            # if BookTicket.objects.filter(~Q(status = False)).count() < 32:
            if BookTicket.objects.filter(status='Confirmed').count() < 24:
                count1 = BookTicket.objects.filter(coach='S1').count()
                count2 = BookTicket.objects.filter(coach='S2').count()
                count3 = BookTicket.objects.filter(coach='S3').count()

                if count1 != 8:
                    if BookTicket.objects.filter(coach='S1',berth_preference=berth).count() == 2:
                        content ="{} Coach {} Berth Fully occupied, Try other berth.".format('S1', berth)
                        return JsonResponse({'is_success': 'unsuccess','error_message': content})

                    if gender == 'Female':
                        s1male_cnt = BookTicket.objects.filter(coach='S1',gender='Male').count()
                        if s1male_cnt < 7:
                            BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S1',status='Confirmed').save()
                            return JsonResponse({'is_success': 'success','msg':"S1 Coach Booking Confirmed Successfully"})
                        else:
                            BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S2',status='Confirmed').save()
                            return JsonResponse({'is_success': 'success','msg':"S2 Coach Booking Confirmed Successfully"})
                    else:
                        BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S1',status='Confirmed').save()
                        return JsonResponse({'is_success': 'success','msg':"S1 Coach Booking Confirmed Successfully"})

                if count2 != 8:
                    if count1 == 8:
                        if BookTicket.objects.filter(coach='S2',berth_preference=berth).count() == 2:
                            content ="{} Coach {} Berth Fully occupied, Try other berth.".format('S2', berth)
                            return JsonResponse({'is_success': 'unsuccess','error_message': content})

                        if gender == 'Female':
                            s2male_cnt = BookTicket.objects.filter(coach='S2',gender='Male').count()
                            if s2male_cnt < 7:
                                BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S2',status='Confirmed').save()
                                return JsonResponse({'is_success': 'success','msg':"S2 Coach Booking Confirmed Successfully"})
                            else:
                                BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S3',status='Confirmed').save()
                                return JsonResponse({'is_success': 'success','msg':"S3 Coach Booking Confirmed Successfully"})
                        else:
                            BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S2',status='Confirmed').save()
                            return JsonResponse({'is_success': 'success','msg':"S2 Coach Booking Confirmed Successfully"})


                if count3 != 8:
                    if count2 == 8:
                        if BookTicket.objects.filter(coach='S3',berth_preference=berth).count() == 2:
                            content ="{} Coach {} Berth Fully occupied, Try other berth.".format('S3', berth)
                            return JsonResponse({'is_success': 'unsuccess','error_message': content})

                        if gender == 'Female':
                            s3male_cnt = BookTicket.objects.filter(coach='S3',gender='Male').count()
                            if s3male_cnt < 7:
                                BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S3',status='Confirmed').save()
                                return JsonResponse({'is_success': 'success','msg':"S3 Coach Booking Confirmed Successfully"})
                            else:
                                BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S4',status='Confirmed').save()
                                return JsonResponse({'is_success': 'success','msg':"S4 Coach Booking Confirmed Successfully"})

                        else:
                            BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S3',status='Confirmed').save()
                            return JsonResponse({'is_success': 'success','msg':"S3 Coach Booking Confirmed Successfully"})

            else:
                if berth == 'Lower' or  berth == 'Side':
                    if BookTicket.objects.filter(status='RAC').count() < 3:
                        BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S4',status='RAC').save()
                        return JsonResponse({'is_success': 'success','msg':"S4 Coach Booking Confirmed Successfully"})
                    else:
                        return JsonResponse({'is_success': 'unsuccess','error_message': "RAC Passengers seats fully allocated,No seats Available,Try other berth execpt Side & Lower"})

                else:
                    if BookTicket.objects.filter(status='Waiting').count() < 5:
                        if BookTicket.objects.filter(coach='S3').count() != 8:
                            BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S3',status='Waiting').save()
                            return JsonResponse({'is_success': 'success','msg':"S3 Coach Booking Confirmed Successfully"})
                        else:
                            BookTicket(name=name,age=age,gender=gender,berth_preference=berth,coach='S4',status='Waiting').save()
                            return JsonResponse({'is_success': 'success','msg':"S4 Coach Booking Confirmed Successfully"})

                    else:
                        message = "No Seats available!" 
                        return JsonResponse({'is_success':'success','alert': message})
            # else:
            #     return JsonResponse({'is_success':'success','alert':"Ticket Booking Closed"})

    else:
        return JsonResponse({'is_success':'unsuccess'})
    



