from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges={
    "january":"Exercise daily in the morning for 20 minutes",
    "february":"Learn python daily for one hour.",
    "march":"Update your work to the github",
    "april":"Build your projects for internship.",
    "may":"Don't lose hope and target your goals.",
    "june":"Follow your path until you get success.",
    "july":"Be positive and always believe in yourself.",
    "august":"People are harsh and unkind so be careful.",
    "september":"You might not get what you expect but don't be discourage by that",
    "october":"",
    "november":"",
    "december":""
}
# Create your views here.
def monthly_challenge_by_number(request,month):
    months=list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month=months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text=monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    