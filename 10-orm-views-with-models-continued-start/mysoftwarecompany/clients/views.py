from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import *


def list_companies(request):
    # fetching data from the database and passing it to the template
    companies = Company.objects.all()

    return render(request, 'clients/companies_list.html', {'companies': companies})

def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    return render(request, 'clients/company_detail.html', {'company': company})

def employee_search_results(request, company_id):
    # 'q' will be in the url
    query = request.GET.get('q', '')
    company = get_object_or_404(Company, id=company_id)

    if query:
        employees = company.employees.filter(
            first_name__icontains=query
        )
    else:
        employees = Employee.objects.none()

    return render(request, 'clients/employee_search_results.html', {'employees': employees, 'query': query})