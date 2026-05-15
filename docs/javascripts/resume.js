// Optimized reading progress recovery and last-page memory script
(function() {
    const SCROLL_KEY_PREFIX = "cflt-scroll-";
    const LAST_PATH_KEY = "cflt-last-path";

    function saveState() {
        const path = window.location.pathname;
        localStorage.setItem(SCROLL_KEY_PREFIX + path, window.scrollY);
        localStorage.setItem(LAST_PATH_KEY, path);
    }

    // 1. Handle page leaving
    window.addEventListener("pagehide", saveState);
    window.addEventListener("beforeunload", saveState);
    
    // 2. Add scroll listener with debouncing
    let timeout;
    window.addEventListener("scroll", () => {
        clearTimeout(timeout);
        timeout = setTimeout(saveState, 500);
    });

    // 3. Restore URL and Position
    function restoreState() {
        const currentPath = window.location.pathname;
        const savedPath = localStorage.getItem(LAST_PATH_KEY);

        // Redirect to last visited page if landing on root and a deeper path was saved
        // We only redirect if the user is at the root "/" and we have a more specific saved path
        if (currentPath === "/" && savedPath && savedPath !== "/" && !window.location.hash && !window.location.search) {
            window.location.replace(savedPath);
            return;
        }

        // Restore scroll position
        if (window.location.hash) return;

        const savedPos = localStorage.getItem(SCROLL_KEY_PREFIX + currentPath);
        if (savedPos) {
            const pos = parseInt(savedPos, 10);
            if (isNaN(pos) || pos === 0) return;

            setTimeout(() => {
                window.scrollTo({
                    top: pos,
                    behavior: "instant"
                });
            }, 100); 
        }
    }

    if (document.readyState === "complete" || document.readyState === "interactive") {
        restoreState();
    } else {
        window.addEventListener("DOMContentLoaded", restoreState);
    }
})();
