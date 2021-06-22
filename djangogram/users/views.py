from django.shortcuts import render

def main(request):
    return render(request, 'users/main.html') # 호출되는 템플렛을 작성해야함