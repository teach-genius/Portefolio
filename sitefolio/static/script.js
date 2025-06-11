document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const body = document.body;

    // Function to set the theme
    const setTheme = (theme) => {
        if (theme === 'dark') {
            body.classList.remove('light-theme');
            // Update icon to sun for light mode switch
            themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
        } else {
            body.classList.add('light-theme');
            // Update icon to moon for dark mode switch
            themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
        }
        localStorage.setItem('theme', theme);
    };

    // Check for saved theme preference or default to dark
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        setTheme(savedTheme);
    } else {
        // Default to dark mode if no preference is found
        setTheme('dark');
    }

    // Toggle theme on button click
    themeToggleBtn.addEventListener('click', () => {
        if (body.classList.contains('light-theme')) {
            setTheme('dark');
        } else {
            setTheme('light');
        }
    });

    // Optional: Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Optional: Animate progress bars on scroll (more advanced)
    const progressBars = document.querySelectorAll('.progress-fill');
    const animateProgressBars = () => {
        progressBars.forEach(progressBar => {
            const rect = progressBar.getBoundingClientRect();
            const skillSection = document.getElementById('competences-profil'); // Get the parent section
            const skillSectionRect = skillSection.getBoundingClientRect();


            if (rect.top < window.innerHeight && rect.bottom > 0 && skillSectionRect.top < window.innerHeight * 0.75) {
                const targetWidth = progressBar.style.width; // Get the width defined in HTML
                progressBar.style.width = '0%'; // Reset to 0 for animation
                setTimeout(() => {
                    progressBar.style.width = targetWidth; // Animate to target width
                }, 100); // Small delay to ensure reset takes effect
            } else if (skillSectionRect.top > window.innerHeight) {
                // Optionally reset if scrolled past
                progressBar.style.width = '0%';
            }
        });
    };

    // Initial animation check and add scroll listener
   animateProgressBars();
    window.addEventListener('scroll', animateProgressBars);
});