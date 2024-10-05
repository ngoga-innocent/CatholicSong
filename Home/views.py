from django.shortcuts import render,redirect
from django.views import View
from Documents.models import Copies,SongCategory
# Create your views here.
def HomeView(request):
    return render(request,'privacy.html')
class Home(View):
    def get(self, request):
        categories=SongCategory.objects.all()
        print(categories)
        context={"categories":categories}
        return render(request,'home.html',context)
    def post(self, request):
        category_id = request.POST.get('song_category')  # Using get for safety
        try:
            category = SongCategory.objects.get(id=category_id)
            print(category)
        except SongCategory.DoesNotExist:
            return render(request, 'home.html', {"error": "Invalid Category"})    
        
        songs = request.FILES.getlist('songs')  # Make sure the name matches the form field
        user = request.user
        
        if not songs:
            return render(request, 'home.html', {"error": "No songs uploaded."})

        for song in songs:
            name = song.name
            parts = name.split(" - ")
            
            if len(parts) < 2:  # Ensure there are at least two parts
                continue  # Skip this file or handle it as needed
            
            title = parts[0].strip()
            composer = parts[1].strip()

            Copies.objects.create(
                name=title,
                composer=composer,
                uploader=user,
                part=category,
                document=song
            )

        # Redirecting to the same page or another page after the upload
        return redirect('home')  # Change 'home' to your actual URL name if different
