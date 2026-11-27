from django.db import models
from django.conf import settings

class Node(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='nodes')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class NodeTag(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('node', 'tag')

class NodeLink(models.Model):
    source_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='outgoing_links')
    target_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='incoming_links')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # This prevents linking the exact same pair twice
        unique_together = ('source_node', 'target_node')

    def __str__(self):
        return f"{self.source_node.title} -> {self.target_node.title}"