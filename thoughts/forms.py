from django import forms
from .models import Node, NodeLink

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class NodeLinkForm(forms.ModelForm):
    class Meta:
        model = NodeLink
        fields = ['target_node']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        source_node = kwargs.pop('source_node', None)
        super(NodeLinkForm, self).__init__(*args, **kwargs)
        
        if user is not None and source_node is not None:
            # 1. Get nodes owned by this user
            # 2. Exclude the source node itself (can't link to itself)
            # 3. Exclude nodes that are already linked (outgoing_links)
            existing_links = source_node.outgoing_links.values_list('target_node_id', flat=True)
            
            self.fields['target_node'].queryset = Node.objects.filter(
                user=user
            ).exclude(
                pk=source_node.pk
            ).exclude(
                pk__in=existing_links
            )