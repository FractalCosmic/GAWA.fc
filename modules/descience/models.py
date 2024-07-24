# models.py
from django.db import models
from django.contrib.auth.models import User
from py2neo import Graph, Node, Relationship

class Research(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_knowledge_graph()

    def update_knowledge_graph(self):
        graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
        
        # Create or update research node
        research_node = Node("Research", id=self.id, title=self.title)
        graph.merge(research_node, "Research", "id")
        
        # Extract keywords (This is a simplified version. You might want to use NLP techniques for better keyword extraction)
        keywords = set(word.lower() for word in self.title.split() + self.content.split() if len(word) > 3)
        
        for keyword in keywords:
            keyword_node = Node("Keyword", name=keyword)
            graph.merge(keyword_node, "Keyword", "name")
            graph.create(Relationship(research_node, "HAS_KEYWORD", keyword_node))

# views.py
from django.shortcuts import render
from .models import Research
from py2neo import Graph

def search_research(request):
    query = request.GET.get('q', '')
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
    
    # Search in Neo4j
    cypher_query = """
    MATCH (r:Research)-[:HAS_KEYWORD]->(k:Keyword)
    WHERE k.name CONTAINS $query
    RETURN r.id, r.title, collect(k.name) as keywords
    """
    results = graph.run(cypher_query, query=query.lower()).data()
    
    # Fetch full research objects from Django
    research_ids = [result['r.id'] for result in results]
    researches = Research.objects.filter(id__in=research_ids)
    
    return render(request, 'search_results.html', {'researches': researches, 'results': results})
