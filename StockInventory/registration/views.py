from django.shortcuts import render
from django.views import View
from registration.forms import RegisterCustomerForm, RegisterEmployeeForm

# Create your views here.

def index(request):
    return render(request, 'registration/index.html')

class RegisterCustomer(View):
    template = 'registration/register_customer.html'
    form = RegisterCustomerForm()

    def get(self, request):
        return render(request, self.template, {'form':self.form})

    def post(self, request):
        self.form = RegisterCustomerForm(request.POST)
        if self.form.is_valid():
            self.form.save()
        else:
            print("unsucessful")
        return index(request)

class RegisterEmployee(View):
    template = 'registration/register_employee.html'
    form = RegisterEmployeeForm()

    def get(self, request):
        return render(request, self.template, {'form':self.form})

    def post(self, request):
        self.form = RegisterEmployeeForm(request.POST)
        if self.form.is_valid():
            self.form.save()
        else:
            print("unsucessful")
        return index(request)


 class Login(View):
    template = 'Login/login.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(pk=username)
            if user.password == password:
                request.session['username'] = user.username
                request.session['type'] = user.type
                return redirect(reverse('registration:index'))
            except User.DoesNotExist:
                user = None

                return render(request, self.template,{'msg':'Incorrect username/ password.'})
