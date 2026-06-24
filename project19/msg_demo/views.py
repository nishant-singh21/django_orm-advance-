from django.shortcuts import render
from django.contrib import messages


def show_msg(request):
    messages.debug(request, 'this is a debug message.')
    messages.info(request,'this ia  an info message. ')
    messages.success(request,'this ia  an success message. ')
    messages.warning(request,'this ia  an warning message. ')
    messages.error(request,'this ia  an error message. ')
    
    return render(request, 'message.html')

