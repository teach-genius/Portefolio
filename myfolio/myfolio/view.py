from django.shortcuts import render


from django.shortcuts import render

def home_view(request):
    projets = [
        {
            "title": "Medical Image Classification",
            "description": "Deep learning model for detecting abnormalities in X-ray images using CNN architecture.",
            "repo_url": "https://github.com/teach-genius/Medical_Classification",
            "tech": ["PyTorch", "CNN", "Medical AI"],
            "live_demo_url": "https://medical-ai-demo.com",
            "img":"https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
        },
        {
            "title": "NLP Research Project",
            "description": "Exploring natural language processing techniques to improve healthcare chatbots.",
            "repo_url": "https://github.com/teach-genius/NLP_Research",
            "tech": ["BERT", "Transformers", "Healthcare"],
            "live_demo_url": "https://nlp-healthcare-demo.com",
            "img":"https://images.unsplash.com/photo-1655720828018-edd2daec9349?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
        },
        {
            "title": "Reinforcement Learning for Energy",
            "description": "Optimizing energy consumption using reinforcement learning techniques.",
            "repo_url": "https://github.com/teach-genius/RL_Energy",
            "tech": ["RL", "Python", "Energy"],
            "live_demo_url": "https://rl-energy-demo.com",
            "img":"https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2072&q=80"
             
        }
    ]

    skills = [
        {
        "skill":"Machine Learning",
        "tech":["TensorFlow","PyTorch","Scikit-learn","Deep Learning","Neural NetWorks","Camputer Vision"]
        },
        {
        "skill":"Machine Learning",
        "tech":["TensorFlow","PyTorch","Scikit-learn","Deep Learning","Neural NetWorks","Camputer Vision"]
        },
        {
        "skill":"Machine Learning",
        "tech":["TensorFlow","PyTorch","Scikit-learn","Deep Learning","Neural NetWorks","Camputer Vision"]
        },
        {
        "skill":"Machine Learning",
        "tech":["TensorFlow","PyTorch","Scikit-learn","Deep Learning","Neural NetWorks","Camputer Vision"]
        },
        
        

    ]

    return render(request, "index.html", context={
        "github": "https://github.com/teach-genius",
        "linkedin": "https://www.linkedin.com/in/teach-genius",
        "projets": projets,
        "skills":skills
    })
