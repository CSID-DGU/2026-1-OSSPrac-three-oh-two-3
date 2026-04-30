// ===== 다크 모드 =====
const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");

function applyTheme(theme) {
    document.documentElement.setAttribute("data-bs-theme", theme);
    localStorage.setItem("theme", theme);
    if (themeIcon) {
        themeIcon.className = theme === "dark" ? "bi bi-sun-fill" : "bi bi-moon-stars-fill";
    }
}

applyTheme(localStorage.getItem("theme") || "light");

if (themeToggle) {
    themeToggle.addEventListener("click", () => {
        const cur = document.documentElement.getAttribute("data-bs-theme");
        applyTheme(cur === "dark" ? "light" : "dark");
    });
}

// ===== 스크롤 진행도 바 =====
const progressBar = document.getElementById("scrollProgress");
window.addEventListener("scroll", () => {
    const h = document.documentElement;
    const scrolled = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
    if (progressBar) progressBar.style.width = scrolled + "%";
});

// ===== Scroll To Top 버튼 =====
const scrollTopBtn = document.getElementById("scrollTop");
window.addEventListener("scroll", () => {
    if (window.scrollY > 400) scrollTopBtn?.classList.add("visible");
    else scrollTopBtn?.classList.remove("visible");
});
scrollTopBtn?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// ===== Stats 카운터 애니메이션 =====
function animateCounter(el) {
    const target = el.getAttribute("data-target") || "";
    const numMatch = target.match(/\d+/);
    if (!numMatch) return;
    const targetNum = parseInt(numMatch[0]);
    const suffix = target.replace(/\d+/, "");

    let current = 0;
    const duration = 1500;
    const step = targetNum / (duration / 16);

    const tick = () => {
        current += step;
        if (current >= targetNum) {
            el.textContent = targetNum + suffix;
        } else {
            el.textContent = Math.floor(current) + suffix;
            requestAnimationFrame(tick);
        }
    };
    tick();
}

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting && !entry.target.dataset.animated) {
            animateCounter(entry.target);
            entry.target.dataset.animated = "true";
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll(".stat-value").forEach((el) => counterObserver.observe(el));

// ===== 기여도 progress bar 애니메이션 =====
const contriObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            const fill = entry.target;
            const pct = fill.getAttribute("data-pct");
            setTimeout(() => { fill.style.width = pct + "%"; }, 200);
            contriObserver.unobserve(fill);
        }
    });
}, { threshold: 0.3 });

document.querySelectorAll(".contri-fill").forEach((el) => contriObserver.observe(el));

// ===== 스무스 스크롤 (해시 링크) =====
document.querySelectorAll('a[href*="#"]').forEach((a) => {
    a.addEventListener("click", (e) => {
        const href = a.getAttribute("href");
        if (href === "#" || !href.includes("#")) return;
        const hashIdx = href.indexOf("#");
        const path = href.substring(0, hashIdx);
        const hash = href.substring(hashIdx);
        if (path && path !== window.location.pathname) return;
        const target = document.querySelector(hash);
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: "smooth", block: "start" });
        }
    });
});