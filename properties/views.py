from django.shortcuts import get_object_or_404, render, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from .models import Property
from .forms import PropertyForm


class PropertyCreateView(
    SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, CreateView
):
    """
    A standard view class rendering the add property
    page for each review using the form_class attribute
    """
    form_class = PropertyForm
    model = Property
    template_name = 'add-property.html'
    success_message = 'Your property has been added succesffuly!'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.ll_or_ea = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        if self.request.user.role == 'LANDLORD_OR_ESTATEAGENT':
            return True
        else:
            return HttpResponse(
                "You are not authenticated to create a property",
                status=403)


class PropertyUpdateView(
    SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    """
    A standard view class rendering the edit property
    page for each review using the form_class attribute
    """
    form_class = PropertyForm
    model = Property
    template_name = 'edit-property.html'
    success_message = 'Your property has been updated successfully!'

    def test_func(self):
        if self.request.user.role == 'LANDLORD_OR_ESTATEAGENT':
            return True
        else:
            return HttpResponse(
                "You are not authenticated to edit this property",
                status=403)


class PropertyDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    """
    A standard view class deleting the property
    before redirecting to the homepage
    """
    model = Property
    template_name = 'property_confirm_delete.html'
    success_url = reverse_lazy('homepage')
    success_message = 'Your property has been deleted successfully!'


class PropertyDetail(View):
    """
    A standard view class rendering the individual
    page for each property
    """

    def get(self, request, slug, *args, **kwargs):
        """
        This method gets the individual property information
        needed for each property page from the model dataset
        """
        queryset = Property.objects.all()
        property = get_object_or_404(queryset, slug=slug)
        reviews = property.reviews.order_by('date_reviewed')

        liked = False
        if property.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'property.html',
            {
                'slug': slug,
                'property': property,
                'reviews': reviews,
                'liked': liked,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        This method gets the individual property information
        needed for each property page from the model dataset
        """
        queryset = Property.objects.all()
        property = get_object_or_404(queryset, slug=slug)
        reviews = property.reviews.order_by('date_reviewed')

        liked = False
        if property.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'property.html',
            {
                'slug': slug,
                'property': property,
                'reviews': reviews,
                'liked': liked,
            },
        )


class PropertyLike(View):
    """Class view to accept the request to like a
    property. It checks if the property has or hasn't
    been liked by the user and renders the new page
    accordingly"""

    def post(self, request, slug, *args, **kwargs):
        """Post request for generic propertylike view,
        will update the likes field on the property model"""
        property = get_object_or_404(Property, slug=slug)
        if property.likes.filter(id=request.user.id).exists():
            property.likes.remove(request.user)
        else:
            property.likes.add(request.user)

        return HttpResponseRedirect(reverse('property_detail', args=[slug]))
