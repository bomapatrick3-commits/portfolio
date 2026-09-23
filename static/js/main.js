window.addEventListener('load', function () {
    const loader = document.getElementById('loader');
    
    // Optional: minimum display time (so it doesn't flash too fast)
    setTimeout(function () {
      loader.classList.add('hidden');
      
      // Fully remove it after the fade-out animation
      setTimeout(function () {
        loader.remove();
      }, 500);
    }, 800); // 800ms minimum loading time
  });