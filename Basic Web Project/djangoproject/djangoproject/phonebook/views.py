from django.shortcuts import render, redirect


def landing_page(requests):
    return render(requests, 'phonebook/index.html')
