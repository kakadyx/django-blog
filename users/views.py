from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OurRegistration, UserUpdateForm, ProfileAvatar
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = OurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} зарегистрирован')
            return redirect('login')
    else:
        form = OurRegistration()
    return render(request, 'users/registration.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        avatar_form = ProfileAvatar(request.POST,request.FILES,instance=request.user.profile)
        update_form = UserUpdateForm(request.POST,instance=request.user)
        if avatar_form.is_valid() and update_form.is_valid():
            update_form.save()
            avatar_form.save()
            
            messages.success(request, f'Данные пользователя успешно изменены')
            return redirect('profile')
    else:
        avatar_form = ProfileAvatar(instance=request.user.profile)
        update_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'avatar_form': avatar_form, 'update_form':update_form})



