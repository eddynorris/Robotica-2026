import re

def update_html():
    with open('c:/Users/Usuario/Documents/Proyectos/robotica/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update HTML layout
    new_video_container = """<div id="modalVideoContainer" class="relative rounded-xl overflow-hidden bg-slate-900 shadow-2xl shadow-cyan-500/5 w-full flex items-center justify-center border border-slate-700/50 transition-all duration-300">
                        <img id="modalImage" class="absolute inset-0 w-full h-full object-cover hidden" src="" alt="Robot Image">
                        <iframe id="modalVideo" class="absolute inset-0 w-full h-full hidden" frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            referrerpolicy="strict-origin-when-cross-origin"
                            allowfullscreen></iframe>
                    </div>"""
                    
    html = re.sub(
        r'<div id="modalVideoContainer"[\s\S]*?<iframe id="modalVideo"[\s\S]*?allowfullscreen></iframe>\s*</div>',
        new_video_container,
        html
    )

    new_fallback = """<div id="modalYouTubeFallback" class="mt-4 flex justify-center w-full hidden">
                        <a id="modalDirectLink" target="_blank" href="#" """
    html = html.replace(
        '<div class="mt-4 flex justify-center w-full">\n                        <a id="modalDirectLink" target="_blank" href="#"',
        new_fallback
    )

    # 2. Update logic
    new_logic = """
        // Dynamic Video/Image Source Assignment
        const originParam = window.location.origin && window.location.origin !== "null" ? window.location.origin : "https://www.youtube.com";
        const videoContainer = document.getElementById('modalVideoContainer');
        const modalVideo = document.getElementById('modalVideo');
        const modalImage = document.getElementById('modalImage');
        const modalFallback = document.getElementById('modalYouTubeFallback');
        const defaultCompilationId = "hft_i3TpRok";

        // Reset display
        modalVideo.src = '';
        modalImage.src = '';
        modalVideo.classList.add('hidden');
        modalImage.classList.add('hidden');
        modalFallback.classList.add('hidden');

        if (robot.image) {
            videoContainer.classList.remove('aspect-video', 'aspect-[9/16]');
            // Use aspect-square or generic for images
            videoContainer.classList.add('aspect-[4/3]');
            videoContainer.style.maxWidth = '100%';
            modalImage.src = robot.image;
            modalImage.classList.remove('hidden');
        } else if (robot.youtubeShortId) {
            videoContainer.classList.remove('aspect-video', 'aspect-[4/3]');
            videoContainer.classList.add('aspect-[9/16]');
            videoContainer.style.maxWidth = '300px'; 
            
            modalVideo.src = `https://www.youtube.com/embed/${robot.youtubeShortId}?autoplay=1&mute=1&modestbranding=1&rel=0&origin=${originParam}`;
            modalVideo.classList.remove('hidden');
            
            document.getElementById('modalDirectLink').href = `https://www.youtube.com/shorts/${robot.youtubeShortId}`;
            document.getElementById('modalDirectLinkText').innerHTML = `Ver Short oficial en YouTube <br><span class="text-[9px] text-red-500/70 font-mono">${robot.youtubeShortId}</span>`;
            modalFallback.classList.remove('hidden');
        } else if (robot.youtubeVideoId) {
            videoContainer.classList.add('aspect-video');
            videoContainer.classList.remove('aspect-[9/16]', 'aspect-[4/3]');
            videoContainer.style.maxWidth = '100%';
            
            modalVideo.src = `https://www.youtube.com/embed/${robot.youtubeVideoId}?autoplay=1&mute=1&modestbranding=1&rel=0&origin=${originParam}`;
            modalVideo.classList.remove('hidden');
            
            document.getElementById('modalDirectLink').href = `https://www.youtube.com/watch?v=${robot.youtubeVideoId}`;
            document.getElementById('modalDirectLinkText').textContent = "Ver video oficial en YouTube";
            modalFallback.classList.remove('hidden');
        } else {
            videoContainer.classList.add('aspect-video');
            videoContainer.classList.remove('aspect-[9/16]', 'aspect-[4/3]');
            videoContainer.style.maxWidth = '100%';
            
            const endTime = robot.youtubeTimestamp + (robot.duration || 15);
            modalVideo.src = `https://www.youtube.com/embed/${defaultCompilationId}?start=${robot.youtubeTimestamp}&end=${endTime}&autoplay=1&mute=1&modestbranding=1&rel=0&origin=${originParam}`;
            modalVideo.classList.remove('hidden');
            
            document.getElementById('modalDirectLink').href = `https://youtu.be/${defaultCompilationId}?t=${robot.youtubeTimestamp}`;
            document.getElementById('modalDirectLinkText').textContent = "¿El video no carga? Ver directamente en YouTube";
            modalFallback.classList.remove('hidden');
        }"""
        
    html = re.sub(
        r'// Dynamic Video Source Assignment[\s\S]*?document\.getElementById\(\'modalDirectLinkText\'\)\.textContent = "¿El video no carga\? Ver directamente en YouTube";\n        }',
        new_logic,
        html
    )

    with open('c:/Users/Usuario/Documents/Proyectos/robotica/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("UI logic updated.")

update_html()
