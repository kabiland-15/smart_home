from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, Messages, Room


def signup(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'submit':
            username = str(request.POST['username'])
            username.lower()

            # To handle the username with spaces
            if ' ' in username:
                messages.error(request, 'Do not use spaces in the username')
                return redirect('/signup')

            email_id = request.POST['email']
            pass1 = request.POST['password1']
            pass2 = request.POST['password2']
            room = request.POST['room']
            # To handle the only when all conditions satisfied like unique username, both passwords matching
            if pass1 == pass2 and not (CustomUser.objects.filter(username=username).exists()):
                user1 = CustomUser.objects.create_user(username=username, email=email_id, password=pass1, room_name=room)
                user1.save()
                print('User created successfully')
                messages.success(request, 'Account created successfully')
                return redirect('/')

            else:

                # When password1 not matching with password2
                if pass1 != pass2:
                    messages.error(request, 'Passwords are not matching')
                    return redirect('/signup')

                # When username is already exists
                elif CustomUser.objects.filter(username=username).exists():
                    messages.error(request, 'Username already taken')
                    return redirect('/signup')
        elif action == 'exist_user':
            return redirect('/')
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'submit':
            user_name = request.POST['username']
            password = request.POST['password']
            room = request.POST['room_id']
            user = authenticate(username=user_name, password=password, room_name=room)

            # When correct credentials entered by the user
            if user is not None:
                login(request, user)
                print('User authenticated')
                return redirect('room', room_name=room, username=user_name)

            # When username is correct and password was wrong
            elif CustomUser.objects.filter(username=user).exists():
                messages.error(request, 'Entered Wrong password')
                print('Wrong password entered')
                return redirect('/')

            # When the username itself wrong
            else:
                messages.error(request, 'Entered username not found')
                print('Username not found')
                return redirect('/')

        elif action == 'new_user':
            return redirect('/signup')

    return render(request, 'index.html')

@login_required
def signout(request):
    logout(request)
    return redirect('/')

@login_required
def room(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)
    get_message = Messages.objects.filter(room=get_room)

    if request.method == 'POST':
        message = request.POST['message']
        print(message)
        new_message = Messages(room=get_room, sender=username, message=message)
        new_message.save()

    context = {
        'messages': get_message,
        'user': username,
        'room_name': room_name,
    }

    return render(request, "message.html", context)

