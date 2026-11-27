from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Node
from .forms import NodeForm

@login_required
def node_list(request):
    # Read: Get only this user's nodes
    nodes = Node.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'thoughts/node_list.html', {'nodes': nodes})

@login_required
def node_create(request):
    # Create
    if request.method == 'POST':
        form = NodeForm(request.POST)
        if form.is_valid():
            node = form.save(commit=False)
            node.user = request.user # Link to logged-in user
            node.save()
            messages.success(request, 'Thought node created!')
            return redirect('node_list')
    else:
        form = NodeForm()
    return render(request, 'thoughts/node_form.html', {'form': form, 'action': 'Create'})

@login_required
def node_update(request, pk):
    # Update: get_object_or_404 ensures users can only edit their own nodes
    node = get_object_or_404(Node, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NodeForm(request.POST, instance=node)
        if form.is_valid():
            form.save()
            messages.success(request, 'Node updated!')
            return redirect('node_list')
    else:
        form = NodeForm(instance=node)
    return render(request, 'thoughts/node_form.html', {'form': form, 'action': 'Update'})

@login_required
def node_delete(request, pk):
    # Delete
    node = get_object_or_404(Node, pk=pk, user=request.user)
    if request.method == 'POST':
        node.delete()
        messages.success(request, 'Node deleted!')
        return redirect('node_list')
    return render(request, 'thoughts/node_confirm_delete.html', {'node': node})