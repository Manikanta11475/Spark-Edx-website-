/**
 * Spark EdX — Main JavaScript
 * Handles: scroll reveals, counter animations, navigation,
 * particles, form handling, brochure modal, mobile menu
 */

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide Icons
    lucide.createIcons();

    // ===== SCROLL REVEAL =====
    initScrollReveal();

    // ===== NAVBAR SCROLL EFFECT =====
    initNavbar();

    // ===== COUNTER ANIMATION =====
    initCounters();

    // ===== HERO PARTICLES =====
    initParticles();

    // ===== CONTACT FORM =====
    initContactForm();

    // ===== BROCHURE FORM =====
    initBrochureForm();

    // ===== MOBILE MENU =====
    initMobileMenu();

    // ===== SMOOTH SCROLL FOR ANCHOR LINKS =====
    initSmoothScroll();
});

// =====================================================
// SCROLL REVEAL ON INTERSECTION
// =====================================================
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => observer.observe(el));
}

// =====================================================
// NAVBAR SCROLL BEHAVIOR
// =====================================================
function initNavbar() {
    const navbar = document.getElementById('navbar');
    let lastScrollY = 0;

    function handleScroll() {
        const scrollY = window.scrollY;

        if (scrollY > 80) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }

        lastScrollY = scrollY;
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Initial check
}

// =====================================================
// ANIMATED COUNTERS
// =====================================================
function initCounters() {
    const counters = document.querySelectorAll('.stat-number[data-target]');

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));
}

function animateCounter(element) {
    const target = parseInt(element.dataset.target);
    const suffix = element.dataset.suffix || '';
    const duration = 2000;
    const startTime = performance.now();

    function easeOutQuart(t) {
        return 1 - Math.pow(1 - t, 4);
    }

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easedProgress = easeOutQuart(progress);
        const currentValue = Math.floor(easedProgress * target);

        if (target >= 1000) {
            element.textContent = currentValue.toLocaleString('en-IN') + suffix;
        } else {
            element.textContent = currentValue + suffix;
        }

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            if (target >= 1000) {
                element.textContent = target.toLocaleString('en-IN') + suffix;
            } else {
                element.textContent = target + suffix;
            }
        }
    }

    requestAnimationFrame(update);
}

// =====================================================
// HERO FLOATING PARTICLES
// =====================================================
function initParticles() {
    const container = document.getElementById('particles-container');
    if (!container) return;

    const particleCount = 25;
    const colors = [
        'rgba(46, 117, 255, 0.4)',
        'rgba(245, 166, 35, 0.3)',
        'rgba(6, 182, 212, 0.3)',
        'rgba(255, 255, 255, 0.2)'
    ];

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');

        const size = Math.random() * 6 + 2;
        const color = colors[Math.floor(Math.random() * colors.length)];
        const left = Math.random() * 100;
        const animDuration = Math.random() * 15 + 10;
        const animDelay = Math.random() * 10;

        particle.style.cssText = `
            width: ${size}px;
            height: ${size}px;
            background: ${color};
            left: ${left}%;
            bottom: -20px;
            animation-duration: ${animDuration}s;
            animation-delay: ${animDelay}s;
            box-shadow: 0 0 ${size * 2}px ${color};
        `;

        container.appendChild(particle);
    }
}

// =====================================================
// CONTACT FORM HANDLING
// =====================================================
function initContactForm() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const submitBtn = document.getElementById('submit-btn');
        const submitText = document.getElementById('submit-text');
        const successMsg = document.getElementById('form-success');

        // Validate
        if (!form.checkValidity()) {
            form.reportValidity();
            return;
        }

        // Loading state
        submitBtn.disabled = true;
        submitText.textContent = 'Submitting...';
        submitBtn.classList.add('opacity-75', 'cursor-not-allowed');

        // Simulate submission (replace with actual API call)
        await new Promise(resolve => setTimeout(resolve, 1500));

        // Success state
        form.style.display = 'none';
        successMsg.classList.remove('hidden');

        // Re-initialize icons for success message
        lucide.createIcons();

        // Reset after 5 seconds for demo purposes
        setTimeout(() => {
            form.reset();
            form.style.display = 'block';
            successMsg.classList.add('hidden');
            submitBtn.disabled = false;
            submitText.textContent = 'Submit Inquiry';
            submitBtn.classList.remove('opacity-75', 'cursor-not-allowed');
        }, 8000);
    });
}

// =====================================================
// BROCHURE MODAL
// =====================================================
function openBrochureModal() {
    const modal = document.getElementById('brochure-modal');
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';

    // Reset states
    document.getElementById('brochure-form').style.display = 'block';
    document.getElementById('brochure-success').classList.add('hidden');

    // Re-initialize icons
    setTimeout(() => lucide.createIcons(), 50);
}

function closeBrochureModal() {
    const modal = document.getElementById('brochure-modal');
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
}

// Close on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeBrochureModal();
});

function initBrochureForm() {
    const form = document.getElementById('brochure-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const submitBtn = document.getElementById('brochure-submit-btn');
        const submitText = document.getElementById('brochure-submit-text');

        if (!form.checkValidity()) {
            form.reportValidity();
            return;
        }

        // Loading
        submitBtn.disabled = true;
        submitText.textContent = 'Processing...';
        submitBtn.classList.add('opacity-75', 'cursor-not-allowed');

        // Simulate
        await new Promise(resolve => setTimeout(resolve, 1200));

        // Show success
        form.style.display = 'none';
        const success = document.getElementById('brochure-success');
        success.classList.remove('hidden');

        // Re-initialize icons
        lucide.createIcons();

        // Reset button for next use
        submitBtn.disabled = false;
        submitText.textContent = 'Download Now';
        submitBtn.classList.remove('opacity-75', 'cursor-not-allowed');
        form.reset();
    });
}

// Make modal functions globally accessible
window.openBrochureModal = openBrochureModal;
window.closeBrochureModal = closeBrochureModal;

// =====================================================
// MOBILE MENU TOGGLE
// =====================================================
function initMobileMenu() {
    const btn = document.getElementById('mobile-menu-btn');
    const menu = document.getElementById('mobile-menu');
    if (!btn || !menu) return;

    let isOpen = false;

    btn.addEventListener('click', () => {
        isOpen = !isOpen;
        menu.classList.toggle('open', isOpen);

        // Update icon
        const icon = btn.querySelector('[data-lucide]');
        if (icon) {
            icon.setAttribute('data-lucide', isOpen ? 'x' : 'menu');
            lucide.createIcons();
        }
    });

    // Close menu on nav link click
    menu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            isOpen = false;
            menu.classList.remove('open');
            const icon = btn.querySelector('[data-lucide]');
            if (icon) {
                icon.setAttribute('data-lucide', 'menu');
                lucide.createIcons();
            }
        });
    });
}

// =====================================================
// SMOOTH SCROLL
// =====================================================
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const navbarHeight = 80;
                const elementPosition = targetElement.getBoundingClientRect().top + window.scrollY;
                const offsetPosition = elementPosition - navbarHeight;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// =====================================================
// INTERACTIVE BROCHURE GALLERY
// =====================================================
function switchBrochurePage(page) {
    const page1 = document.getElementById('brochure-view-1');
    const page2 = document.getElementById('brochure-view-2');
    const btn1 = document.getElementById('btn-brochure-1');
    const btn2 = document.getElementById('btn-brochure-2');

    if (page === 1) {
        page1.classList.remove('hidden');
        page2.classList.add('hidden');
        
        btn1.classList.add('bg-brand-600', 'text-white');
        btn1.classList.remove('bg-white', 'text-gray-700', 'hover:bg-gray-50');
        
        btn2.classList.remove('bg-brand-600', 'text-white');
        btn2.classList.add('bg-white', 'text-gray-700', 'hover:bg-gray-50');
    } else {
        page1.classList.add('hidden');
        page2.classList.remove('hidden');
        
        btn2.classList.add('bg-brand-600', 'text-white');
        btn2.classList.remove('bg-white', 'text-gray-700', 'hover:bg-gray-50');
        
        btn1.classList.remove('bg-brand-600', 'text-white');
        btn1.classList.add('bg-white', 'text-gray-700', 'hover:bg-gray-50');
    }
}

function openLightbox(src) {
    const modal = document.getElementById('lightbox-modal');
    const img = document.getElementById('lightbox-img');
    img.src = src;
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
}

// Make lightbox closeable on background click
document.addEventListener('DOMContentLoaded', () => {
    const lightboxModal = document.getElementById('lightbox-modal');
    if (lightboxModal) {
        lightboxModal.addEventListener('click', (e) => {
            if (e.target === lightboxModal || e.target.id === 'lightbox-modal-bg') {
                closeLightbox();
            }
        });
    }
});

function closeLightbox() {
    const modal = document.getElementById('lightbox-modal');
    if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        document.body.style.overflow = '';
    }
}

// Bind to window for HTML inline calls
window.switchBrochurePage = switchBrochurePage;
window.openLightbox = openLightbox;
window.closeLightbox = closeLightbox;
