// Optimized reading progress recovery script
(function() {
    const STORAGE_KEY_PREFIX = "cflt-scroll-";

    function savePosition() {
        localStorage.setItem(STORAGE_KEY_PREFIX + window.location.pathname, window.scrollY);
    }

    // 1. Handle page leaving for both mobile and desktop
    window.addEventListener("pagehide", savePosition);
    window.addEventListener("beforeunload", savePosition);
    
    // 2. Add scroll listener with debouncing to prevent progress loss during crashes
    let timeout;
    window.addEventListener("scroll", () => {
        clearTimeout(timeout);
        timeout = setTimeout(savePosition, 500);
    });

    // 3. Restore position
    function restorePosition() {
        // If the URL has a hash (e.g., #section-1), let the browser handle anchor navigation
        if (window.location.hash) return;

        const savedPos = localStorage.getItem(STORAGE_KEY_PREFIX + window.location.pathname);
        if (savedPos) {
            const pos = parseInt(savedPos, 10);
            if (isNaN(pos) || pos === 0) return;

            // Small delay to ensure dynamic content (Mermaid, images) is sufficiently loaded
            setTimeout(() => {
                window.scrollTo({
                    top: pos,
                    behavior: "instant"
                });
            }, 100); 
        }
    }

    // Support for standard page load and potential SPA-like transitions
    if (document.readyState === "complete" || document.readyState === "interactive") {
        restorePosition();
    } else {
        window.addEventListener("DOMContentLoaded", restorePosition);
    }
})();
