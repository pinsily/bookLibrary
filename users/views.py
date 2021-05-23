from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse

from users.models import UserProfile


def user_login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)

        user = UserProfile.objects.filter(username=username)

        # 用户已存在, 走登录
        if user:
            # 验证密码
            user = authenticate(username=username, password=password)
            if user:
                # 验证通过
                login(request, user)
                print(f"登录成功, user=>{user}, request.user=>{request.user}")
            else:
                print("密码错误")
        else:
            user = UserProfile.objects.create_user(username=username, password=password)
            print(f"注册成功, user=>{user}")
            login(request, user)

    return redirect(reverse('library:index'))


def user_logout(request):
    print(f'退出登陆, requests.user=>{request.user}')
    user = request.user
    if isinstance(user, UserProfile):
        logout(request)
        print(f'退出登陆成功, requests.user=>{request.user}')
    else:
        print("用户未登录")
    return redirect(reverse('library:index'))


def user_register(request):
    return None
