from django.shortcuts import render
from rest_framework.views import APIView
from .models import Project, User
from .serializer import ProjectSerializer
from rest_framework.response import Response
import json
from django.db.models import Q


class UserView(APIView):
    def post(self, request):
        result = json.loads(request.body)
        user = result['user']
        passwd = result['passwd']
        result = User.objects.filter(name=user, passwd=passwd)
        if result:
            target = User.objects.get(name=user)
            if target.position == 'Full-time':
                return Response(2)
            else:
                return Response(1)
        else:
            return Response(0)


class CreateView(APIView):
    def post(self, request):
        Project.objects.create(
            name=request.POST.get('name'),
            submitter=request.POST.get('submitter'),
            FA=request.POST.get('FA'),
            category=request.POST.get('category'),
            summary=request.POST.get('summary'),
            file_BP=request.FILES.get('file_BP'),
            file_datapack=request.FILES.get('file_datapack'),
        )

        return Response(0)


class EditView(APIView):
    def post(self, request):
        target = Project.objects.get(id=request.POST.get('id'))
        target.name = request.POST.get('name')
        target.submitter = request.POST.get('submitter')
        target.category = request.POST.get('category')
        target.FA = request.POST.get('FA')
        if request.FILES.get('file_BP'):
            target.file_BP = request.FILES.get('file_BP')
        if request.FILES.get('file_datapack'):
            target.file_datapack = request.FILES.get('file_datapack')
        target.save()
        return Response(0)


class ChangeView(APIView):
    def post(self, request):
        target = User.objects.get(name=request.POST.get('user'))
        if request.POST.get('old_password') == target.passwd:
            target.passwd = request.POST.get('new_password')
            target.save()
            return Response(1)
        else:
            return Response(0)


class EditIndexView(APIView):
    def post(self, request):
        data = Project.objects.filter(submitter=json.loads(request.body)['submitter'])
        projects_data = ProjectSerializer(data, many=True)
        return Response(projects_data.data)


class SearchView(APIView):
    def post(self, request):
        value = request.data['value']
        if value:
            model = Q()
            model.connector = 'OR'
            model.children.append(('name', value))
            model.children.append(('submitter', value))
            model.children.append(('FA', value))
            model.children.append(('category', value))
            result = Project.objects.filter(model, )
            result_data = ProjectSerializer(result, many=True)
        else:
            result = Project.objects.all()
            result_data = ProjectSerializer(result, many=True)

        return Response(result_data.data)


class SearchDefaultView(APIView):
    def get(self, request):
        result = Project.objects.all().order_by('last_update_time').reverse()
        if len(result) > 30:
            result = result[:30]

        result_data = ProjectSerializer(result, many=True)
        return Response(result_data.data)
