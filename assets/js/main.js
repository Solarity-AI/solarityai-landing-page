(function () {
  "use strict";

  // ======= Sticky Header
  window.onscroll = function () {
    const ud_header = document.querySelector(".ud-header");
    const sticky = ud_header.offsetTop;
    const logo = document.querySelector(".navbar-brand img");

    if (window.pageYOffset > sticky) {
      ud_header.classList.add("sticky");
    } else {
      ud_header.classList.remove("sticky");
    }

    // show or hide the back-to-top button
    const backToTop = document.querySelector(".back-to-top");
    if (
      document.body.scrollTop > 50 ||
      document.documentElement.scrollTop > 50
    ) {
      backToTop.style.display = "flex";
    } else {
      backToTop.style.display = "none";
    }
  };

  // ====== Hamburger Menu Toggle - SIMPLE DIRECT APPROACH
  // This will be handled by inline script in HTML for maximum reliability

  // ====== Smooth Scroll
  const pageLink = document.querySelectorAll(".ud-menu-scroll");

  pageLink.forEach((elem) => {
    elem.addEventListener("click", (e) => {
      e.preventDefault();
      const targetId = elem.getAttribute("href");
      const targetSection = document.querySelector(targetId);

      if (targetSection) {
        const headerOffset = 80;
        const elementPosition = targetSection.getBoundingClientRect().top;
        const offsetPosition =
          elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: "smooth",
        });
      }
    });
  });

  // ====== Active Menu Item on Scroll
  function onScroll(event) {
    const sections = document.querySelectorAll("section[id]");
    const scrollPos =
      window.pageYOffset ||
      document.documentElement.scrollTop ||
      document.body.scrollTop;

    sections.forEach((section) => {
      const sectionTop = section.offsetTop - 100;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute("id");
      const navLink = document.querySelector(
        `.ud-menu-scroll[href="#${sectionId}"]`,
      );

      if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
        document.querySelectorAll(".ud-menu-scroll").forEach((link) => {
          link.classList.remove("active");
        });
        if (navLink) {
          navLink.classList.add("active");
        }
      }
    });
  }

  window.document.addEventListener("scroll", onScroll);

  // ====== WOW.js Initialization
  if (typeof WOW !== "undefined") {
    new WOW().init();
  }

  // ====== Scroll to Top
  function scrollTo(element, to = 0, duration = 500) {
    const start = element.scrollTop;
    const change = to - start;
    const increment = 20;
    let currentTime = 0;

    const animateScroll = () => {
      currentTime += increment;

      const val = Math.easeInOutQuad(currentTime, start, change, duration);

      element.scrollTop = val;

      if (currentTime < duration) {
        setTimeout(animateScroll, increment);
      }
    };

    animateScroll();
  }

  Math.easeInOutQuad = function (t, b, c, d) {
    t /= d / 2;
    if (t < 1) return (c / 2) * t * t + b;
    t--;
    return (-c / 2) * (t * (t - 2) - 1) + b;
  };

  const backToTopBtn = document.querySelector(".back-to-top");
  if (backToTopBtn) {
    backToTopBtn.onclick = () => {
      scrollTo(document.documentElement);
    };
  }

  // ====== Form Validation Enhancement
  const contactForm = document.querySelector(".ud-contact-form");
  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      const inputs = contactForm.querySelectorAll(
        "input[required], textarea[required]",
      );
      let isValid = true;

      inputs.forEach((input) => {
        if (!input.value.trim()) {
          isValid = false;
          input.style.borderColor = "#ef4444";
        } else {
          input.style.borderColor = "";
        }
      });

      if (!isValid) {
        e.preventDefault();
        const currentLang = window.getCurrentLanguage
          ? window.getCurrentLanguage()
          : "en";
        const errorMsg =
          translations[currentLang] &&
          translations[currentLang]["formErrorRequiredFields"]
            ? translations[currentLang]["formErrorRequiredFields"]
            : "Please fill in all required fields.";
        alert(errorMsg);
      } else {
        // Track form submission with Google Analytics
        if (typeof gtag !== "undefined") {
          const formData = {
            name: contactForm.querySelector('input[name="name"]')?.value || "",
            email:
              contactForm.querySelector('input[name="user_email"]')?.value ||
              "",
            company:
              contactForm.querySelector('input[name="company"]')?.value ||
              "N/A",
            messageLength:
              contactForm.querySelector('textarea[name="message"]')?.value
                ?.length || 0,
          };

          gtag("event", "form_submission", {
            event_category: "Contact",
            event_label: "Contact Form",
            value: 1,
            form_name: formData.name,
            form_email: formData.email,
            form_company: formData.company,
            message_length: formData.messageLength,
          });

          console.log("✅ Form submission tracked:", formData);
        }
      }
    });
  }

  // ====== Intersection Observer for Fade-in Animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
      }
    });
  }, observerOptions);

  // Observe all cards and sections
  document
    .querySelectorAll(".ud-capability-card, .ud-project-card, .ud-single-team")
    .forEach((el) => {
      el.style.opacity = "0";
      el.style.transform = "translateY(20px)";
      el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
      observer.observe(el);
    });

  // ====== Partner Logo Hover Effects
  document.querySelectorAll(".ud-partner-logo").forEach((logo) => {
    logo.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-5px) scale(1.05)";
    });

    logo.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0) scale(1)";
    });
  });

  // ====== Initialize on DOM Ready
  document.addEventListener("DOMContentLoaded", function () {
    // Set initial active menu item
    onScroll();

    // Add loading animation
    document.body.style.opacity = "0";
    setTimeout(() => {
      document.body.style.transition = "opacity 0.5s ease";
      document.body.style.opacity = "1";
    }, 100);
  });

  // === LinkedIn Profile Click Tracking ===
  function setupLinkedInTracking() {
    // Track all LinkedIn links in the team section
    const linkedinLinks = document.querySelectorAll(
      '#team a[href*="linkedin.com"]',
    );

    console.log(
      "Setting up LinkedIn tracking. Found",
      linkedinLinks.length,
      "LinkedIn links",
    );

    if (linkedinLinks.length === 0) {
      console.warn(
        'No LinkedIn links found in team section. Check if team section exists and has id="team"',
      );
      return;
    }

    linkedinLinks.forEach((link, index) => {
      link.addEventListener("click", function (e) {
        const linkedinUrl = this.getAttribute("href");
        const teamMemberName =
          this.closest(".ud-single-team")
            ?.querySelector(".ud-team-info h5")
            ?.textContent?.trim() || "Unknown";
        const clickType = this.closest(".ud-team-image") ? "image" : "icon";

        // Log to console for debugging
        console.log("🔗 LinkedIn click tracked:", {
          teamMember: teamMemberName,
          url: linkedinUrl,
          clickType: clickType,
          timestamp: new Date().toISOString(),
        });

        // Track with Google Analytics
        if (typeof gtag !== "undefined") {
          gtag("event", "linkedin_profile_click", {
            event_category: "Team",
            event_label: teamMemberName,
            linkedin_url: linkedinUrl,
            click_type: clickType,
            value: 1,
          });
          console.log("✅ Event sent to Google Analytics");
        } else {
          console.warn("⚠️ Google Analytics (gtag) not loaded yet");
        }
      });

      console.log(
        `LinkedIn link ${index + 1} tracking attached:`,
        link.getAttribute("href"),
      );
    });
  }

  // Run when DOM is ready, or immediately if already loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupLinkedInTracking);
  } else {
    setupLinkedInTracking();
  }

  console.log("=== MOBILE MENU SCRIPT LOADING ===");

  // ULTRA SIMPLE DIRECT APPROACH
  window.addEventListener("load", function () {
    console.log("=== PAGE LOADED, INITIALIZING MENU ===");

    setTimeout(function () {
      console.log("=== SETTING UP MENU NOW ===");

      const btn = document.getElementById("mobileMenuToggle");
      const menu = document.querySelector(".navbar-collapse");

      console.log("Button found:", !!btn);
      console.log("Menu found:", !!menu);

      if (!btn) {
        console.error("BUTTON NOT FOUND!");
        return;
      }

      if (!menu) {
        console.error("MENU NOT FOUND!");
        return;
      }

      // Disable Bootstrap
      btn.removeAttribute("data-bs-toggle");
      btn.removeAttribute("data-bs-target");

      if (window.bootstrap) {
        try {
          const collapse = bootstrap.Collapse.getInstance(menu);
          if (collapse) {
            collapse.dispose();
            console.log("Bootstrap collapse disposed");
          }
        } catch (e) {
          console.log("Bootstrap error:", e);
        }
      }

      // Replace button to remove all listeners
      const newBtn = btn.cloneNode(true);
      btn.parentNode.replaceChild(newBtn, btn);
      console.log("Button replaced");

      // Toggle function
      function toggleMenu() {
        const isOpen = menu.classList.contains("show");
        console.log("TOGGLE CALLED - Menu open:", isOpen);

        if (isOpen) {
          newBtn.classList.remove("active");
          menu.classList.remove("show");
          document.body.style.overflow = "";
          console.log("✅ MENU CLOSED");
        } else {
          newBtn.classList.add("active");
          menu.classList.add("show");
          document.body.style.overflow = "hidden";
          console.log("✅ MENU OPENED");
        }
      }

      // Direct onclick
      newBtn.onclick = function (e) {
        console.log("ONCLICK FIRED");
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        toggleMenu();
        return false;
      };

      // addEventListener backup
      newBtn.addEventListener(
        "click",
        function (e) {
          console.log("ADDEVENTLISTENER FIRED");
          e.preventDefault();
          e.stopPropagation();
          toggleMenu();
        },
        true,
      );

      // Test click
      console.log("Adding test click handler...");
      newBtn.addEventListener("mousedown", function () {
        console.log("MOUSEDOWN on button!");
      });

      // Close on links
      const links = menu.querySelectorAll("a");
      links.forEach(function (link) {
        link.addEventListener("click", function () {
          setTimeout(function () {
            newBtn.classList.remove("active");
            menu.classList.remove("show");
            document.body.style.overflow = "";
          }, 100);
        });
      });

      // Close on outside
      document.addEventListener("click", function (e) {
        if (menu.classList.contains("show")) {
          if (!menu.contains(e.target) && !newBtn.contains(e.target)) {
            newBtn.classList.remove("active");
            menu.classList.remove("show");
            document.body.style.overflow = "";
          }
        }
      });

      console.log("✅ MENU SETUP COMPLETE");
      console.log("Button element:", newBtn);
      console.log("Menu element:", menu);
    }, 1000);
  });
})();
