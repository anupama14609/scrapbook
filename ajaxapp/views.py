from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from .forms import ScrapFriendForm
from .models import ScrapFriend
from django.views import View
from django.http import HttpResponse


class ScrapFriendView(View):
    form_class = ScrapFriendForm
    template_name = "ajaxapp/home.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        friends = ScrapFriend.objects.all()
        return render(self.request, self.template_name, {
            'form':form, "friends":friends
        })

    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                instance = form.save()
                serializer_instance = serializers.serialize('json',[instance,])
                return JsonResponse({"instance":serializer_instance}, status=200)
            else:
                return JsonResponse({"error":form.errors}, status=400)
        return JsonResponse({"error":""}, status=400)

