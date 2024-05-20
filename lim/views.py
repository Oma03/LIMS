# from django.contrib import messages
# # from django.shortcuts import render
# from django.http import HttpResponseRedirect generics-meant to be before status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *


# Create your views here.


# VIEWS

# BookAppointment
# Request Type : POST
# Request Body : [result, Firstname, Lastname, age, specimen_choice,test_type, pathologist, date, time, result]
# Return Type : Patient Details

class BookPatient(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # req_department_id = request.data['department_id']
        # department = Department.objects.get(department_id=req_department_id)

        # creating the patient object
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        specimenchoice = request.POST.get('specimenchoice')
        testtype = request.POST.get('testtype')
        pathologist = request.POST.get('pathologist')
        date = request.POST.get('date')
        time = request.POST.get('time')

        appointment = Patient(patient_lname=lastname, patients_fname=firstname, age=age, specimen_choice=specimenchoice,
                              test_type=testtype, pathologist_present=pathologist, date=date, time_e=time)
        appointment.save()

        return Response(data={'appointment': appointment.__dict__}, status=status.HTTP_200_OK)


# EditAppointment
# Request Type : POST
# Request Body : [appointment_id, dept, doctor, firstname, Lastname, email, phonenumber, date, time, note]
# Return Type : Appointment Details


# class EditAppointment(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         req_department_id = request.data['department_id']
#         department = Department.objects.get(department_id=req_department_id)
#
#         req_doctor_id = request.data['staff_id']
#         doctor = Doctor.objects.get(staff_id=req_doctor_id)
#
#         # creating the apponittment object
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         email = request.POST.get('email')
#         phonenumber = request.POST.get('phonenumber')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         note = request.POST.get('note')
#
#         if email is None or firstname is None:
#             return Response(data={"error": "No email match found"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             appointment = Appointment.objects.get(email=email, firstname=firstname)
#             appointment.department = department
#             appointment.doctor = doctor
#             appointment.patients_email = email
#             appointment.patients_firstname = firstname
#             appointment.patients_lastname = lastname
#             appointment.patients_phone = phonenumber
#             appointment.appointment_note = note
#             appointment.appointment_time = time
#             appointment.appointment_date = date
#             appointment.save()
#             # appointment.update(department=department, doctor=doctor, patients_firstname=firstname,
#             patients_lastname=
#             #                     lastname, patients_email=email, patients_phone=phonenumber, appointment_date=date,
#             #                     appointment_time=time, appointment_note=note)
#
#         return Response(data={'appointment': appointment.__dict__}, status=status.HTTP_200_OK)
#
#
# # CancelAppointment
# # Request Type : POST
# # Request Body : [ appointment_id ]
# # Return Type : Success
#
#
# class CancelAppointment(APIView):
#     def delete(self, appointment_id):
#         try:
#             app_id = Appointment.objects.get(appointment_id=appointment_id)
#             app_id.delete()
#             return Response(data={"Success"}, status=status.HTTP_200_OK)
#         except Appointment.DoesNotExist:
#             return Response(data={"Failed"}, status=status.HTTP_404_NOT_FOUND)
#
#
# # PostponeAppointment
# # Request Type : POST
# # Request Body : [ appointment_id , appointment_date , appointment_time ]
# # Return Type : Success
#
#
# class PostAppointment(APIView):
#     permission_classes = [AllowAny]
#
#     def post(self, request, appointment_id):
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         try:
#             appointment = Appointment.objects.get(appointment_id=appointment_id, appointment_date=date,
#                                                   appointment_time=time)
#             appointment.appointment_date = date
#             appointment.appointment_time = time
#             appointment.save()
#             return Response(data={'appointment': appointment.__dict__}, status=status.HTTP_200_OK)
#
#         except Appointment.DoesNotExist:
#             return Response(data={"Failed"}, status=status.HTTP_404_NOT_FOUND)
