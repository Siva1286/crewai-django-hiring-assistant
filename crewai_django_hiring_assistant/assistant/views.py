from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import HiringRequestForm
from .models import HiringGeneration
from ai_agents.crew import generate_hiring_content

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "assistant/home.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created.")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "assistant/register.html", {"form": form})

@login_required
def dashboard(request):
    items = HiringGeneration.objects.filter(user=request.user)
    return render(request, "assistant/dashboard.html", {"items": items})

@login_required
def generate(request):
    if request.method == "POST":
        form = HiringRequestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                output = generate_hiring_content(
                    job_title=data["job_title"],
                    skills=data["skills"],
                    experience_level=data["experience_level"],
                    additional_details=data.get("additional_details", ""),
                )
                record = HiringGeneration.objects.create(
                    user=request.user,
                    job_title=data["job_title"],
                    skills=data["skills"],
                    experience_level=data["experience_level"],
                    additional_details=data.get("additional_details", ""),
                    job_description=output["job_description"],
                    technical_questions=output["technical_questions"],
                    hr_questions=output["hr_questions"],
                )
                messages.success(request, "Hiring content generated successfully.")
                return redirect("result_detail", pk=record.pk)
            except Exception as exc:
                # Show a useful message without exposing a full traceback to the browser.
                messages.error(request, f"AI generation failed: {exc}")
    else:
        form = HiringRequestForm()
    return render(request, "assistant/generate.html", {"form": form})

@login_required
def result_detail(request, pk):
    record = get_object_or_404(HiringGeneration, pk=pk, user=request.user)
    return render(request, "assistant/result.html", {"record": record})
