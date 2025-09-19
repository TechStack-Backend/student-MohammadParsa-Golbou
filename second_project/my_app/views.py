from django.shortcuts import render, HttpResponse

developers = [
    {
        'username': 'hassan',
        'first_name': 'Hassan',
        'last_name': 'Kabirian',
        'skills': ['Python', 'Django', 'Vue.js']
    },
    {
        'username': 'sara',
        'first_name': 'Sara',
        'last_name': 'Ahmadi',
        'skills': ['JavaScript', 'React', 'CSS']
    },
    {
        'username': 'ali',
        'first_name': 'Ali',
        'last_name': 'Rezayi',
        'skills': ['Java', 'Spring Boot', 'SQL']
    }
]


def Developers_Page(request):
    return render(request, "developers_list.html", {'developers': developers})

def Developer_CV(request, username):
    for item in developers:
        if item["username"] == username:
            developer = item
            break

    if developer is None:
        return HttpResponse("Devloper Not Found!", status=404)
    
    return render(request, "developer_cv.html", {'user': developer})