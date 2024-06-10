from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Meeting, Room
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required


@login_required
def details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(
        request, template_name="details/details.html", context={"meeting": meeting}
    )


@login_required
def rooms(request):
    return render(
        request,
        template_name="rooms/rooms.html",
        context={"rooms": Room.objects.all()},
    )


MeetingForm = modelform_factory(Meeting, exclude=[])


@login_required
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, template_name="new/new.html", context={"form": form})


@login_required
def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect(to="details", id=id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request, template_name="edit/edit.html", context={"form": form})


@login_required
def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        # Form is only shown to ask for confirmation
        # When we get a POST, we know we can go ahead and delete
        meeting.delete()
        return redirect("welcome")
    else:
        return render(
            request,
            template_name="confirm/confirm_delete.html",
            context={"meeting": meeting},
        )
