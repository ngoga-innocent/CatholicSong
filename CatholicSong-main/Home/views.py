from django.shortcuts import render,redirect
from django.views import View
from Documents.models import Copies,SongCategory
from Notifications.send_Push_Notification import send_push_notification
from django.db import transaction
import re
# Create your views here.
def HomeView(request):
    
    return render(request,'privacy.html')
class Home(View):
    def get(self, request):
        
        categories=SongCategory.objects.all()
        # print(categories)
        context={"categories":categories}
        return render(request,'home.html',context)
    

    def post(self, request):
        category_id = request.POST.get('song_category')
        try:
            category = SongCategory.objects.get(id=category_id)
        except SongCategory.DoesNotExist:
            return render(request, 'home.html', {"error": "Invalid Category"})
        
        songs = request.FILES.getlist('songs')
        user = request.user
        
        if not songs:
            return render(request, 'home.html', {"error": "No songs uploaded."})
        
        errors = []
        allowed_extensions = ['pdf', 'mp3']
        max_file_size = 10 * 1024 * 1024  # 10 MB

        with transaction.atomic():
            for song in songs:
                name = song.name
    
                # Remove the file extension
                if name.endswith('.pdf'):
                    name = name[:-4]  # Remove the last 4 characters (".pdf")
                
                # Standardize delimiters to "_"
                standardized_name = re.sub(r"[\-()]", "_", name)
                parts = standardized_name.split("_")
                
                if len(parts) < 2:  # Ensure there are at least two parts
                    print(f"Skipping file: {name}. Expected format: 'Title _ Composer'")
                    continue

                # First part as the title
                title = parts[0].strip()
                
                # All remaining parts as the composer name
                composer = " ".join(parts[1:]).strip()
                
                # Debugging output
                print(f"Title: {title}, Composer: {composer}")

                # Create a copy using the parsed data
                Copies.objects.create(
                    name=title,
                    composer=composer,
                    uploader=user,
                    part=category,
                    document=song,
                    # category=category
                )


        if errors:
            return render(request, 'home.html', {"errors": errors})
        
        return redirect('home')
  # Change 'home' to your actual URL name if different
