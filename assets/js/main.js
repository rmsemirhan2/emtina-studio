/**
 * EMTINA STUDIO - Interactive Logic & Multi-Language Engine
 * Built with Alpine.js & Vanilla Modern JavaScript
 */

// Comprehensive Dictionaries (Turkish & English)
const translations = {
  tr: {
    // Nav
    nav_home: "Ana Sayfa",
    nav_about: "Hakkımda",
    nav_services: "Hizmetler",
    nav_portfolio: "Portfolyo",
    nav_process: "Süreç",
    nav_contact: "İletişim",
    nav_cta: "İletişime Geç",

    // Hero
    hero_badge: "Geleceğin Dijital Mimarisi",
    hero_title_prefix: "Ultra Modern & Yüksek Performanslı",
    hero_subtitle: "Emtina Studio; yenilikçi SaaS platformlarını, mobil oyun mimarilerini ve kurumsal web sistemlerini siber hız, kusursuz UI/UX ve ölçeklenebilir kod kalitesiyle gerçeğe dönüştürür.",
    hero_cta_projects: "Projeleri İncele",
    hero_cta_contact: "Hemen İletişime Geç",
    hero_stat_1_val: "30+",
    hero_stat_1_lbl: "Tamamlanan Proje",
    hero_stat_2_val: "99.8%",
    hero_stat_2_lbl: "Müşteri Memnuniyeti",
    hero_stat_3_val: "8+ Yıl",
    hero_stat_3_lbl: "Mühendislik Deneyimi",
    hero_stat_4_val: "100K+",
    hero_stat_4_lbl: "Kullanıcı Etkileşimi",

    // About Me
    about_tag: "HAKKIMDA & KURUCU",
    about_title: "Teknoloji Tutkusu, Mühendislik Disiplini",
    about_bio_1: "Merhaba! Ben Emtina Studio'nun kurucusuyum. Modern yazılım dünyasında uçtan uca mimariler, yüksek erişilebilirlikli SaaS ürünleri ve Godot Engine ile yüksek performanslı mobil oyun geliştirme alanında uzmanlaşmış bir full-stack mühendisim.",
    about_bio_2: "Laravel ve Next.js'ten mikroservis mimarilerine, gerçek zamanlı WebSocket altyapılarından optimize veritabanı tasarımlarına kadar geniş bir spektrumda uçtan uca dijital dönüşüm sağlıyorum. Temiz kod, siber güvenlik ve üstün kullanıcı deneyimi çalışmalarımın merkezindedir.",
    about_skills_title: "Temel Uzmanlık & Teknoloji Yığını",
    about_cta_contact: "İletişime Geç",
    about_cta_projects: "Projeleri Görüntüle",

    // Services
    services_tag: "UZMANLIK ALANLARI",
    services_title: "Siber Hızda, Geleceğe Hazır Çözümler",
    services_subtitle: "Fikir aşamasından milyonlarca kullanıcıya hizmet veren üretim ortamlarına kadar her katmanda yanınızdayız.",
    service_1_title: "SaaS & Bulut Platformları",
    service_1_desc: "Abonelik modelleri, çoklu kiracılı (multi-tenant) mimari, otomatik faturalandırma ve bulut ölçeklenebilirliği ile güçlendirilmiş kurumsal SaaS sistemleri.",
    service_2_title: "Mobil Oyun & Uygulama",
    service_2_desc: "Godot 4 Engine ve modern mobil çerçevelerle geliştirilen, 60 FPS akıcı fizik, gerçek zamanlı çok oyunculu netcode ve çarpıcı görsel deneyim.",
    service_3_title: "Modern Full-Stack Web",
    service_3_desc: "Next.js, Laravel ve Tailwind ile hazırlanan, ultra hızlı yüklenen, SEO optimize ve reaktif kullanıcı arayüzlerine sahip web uygulamaları.",
    service_4_title: "API & Mikroservis Mimarisi",
    service_4_desc: "Yüksek hacimli veri akışlarını yöneten, Docker ve Redis destekli, güvenli ve iyi belgelenmiş RESTful & GraphQL API sistemleri.",
    service_5_title: "UI/UX & Dark-Tech Tasarım",
    service_5_desc: "Kullanıcı psikolojisini cyberpunk estetiğiyle harmanlayan, etkileşimli, animasyonlu ve yüksek dönüşüm odaklı tasarım sistemleri.",
    service_6_title: "Danışmanlık & Ölçekleme",
    service_6_desc: "Mevcut sistemleriniz için kod refactoring, veritabanı indeksleme, güvenlik denetimi ve bulut altyapı maliyet optimizasyonu.",

    // Portfolio
    portfolio_tag: "ÖNE ÇIKAN ÇALIŞMALAR",
    portfolio_title: "Portfolyo & Üretimdeki Projeler",
    portfolio_subtitle: "Emtina Studio laboratuvarında mimarisi kurgulanan ve canlıda değer üreten amiral gemisi projeler.",
    tab_all: "Tümü",
    tab_web: "Web & SaaS",
    tab_game: "Mobil & Oyun",

    // Process
    process_tag: "ÇALIŞMA DİSİPLİNİ",
    process_title: "Uçtan Uca Geliştirme Süreci",
    process_subtitle: "Sıfırdan canlıya kadar uyguladığımız 4 aşamalı çevik yazılım metodolojisi.",
    process_1_num: "01",
    process_1_title: "Keşif & Sistem Mimarisi",
    process_1_desc: "İhtiyaç analizi, veri tabanı şeması ve ölçeklenebilir teknoloji yığınının belirlenmesi.",
    process_2_num: "02",
    process_2_title: "UI/UX & Prototipleme",
    process_2_desc: "Dark-tech estetiğinde, kullanıcı odaklı wireframe ve interaktif prototip tasarımı.",
    process_3_num: "03",
    process_3_title: "Çevik Kodlama & Sprintler",
    process_3_desc: "Temiz mimari (Clean Architecture), test güdümlü geliştirme ve haftalık ilerleme demoları.",
    process_4_num: "04",
    process_4_title: "Dağıtım, CI/CD & Büyüme",
    process_4_desc: "Otomatize testler, Dockerize bulut dağıtımı ve lansman sonrası sürekli teknik destek.",

    // Contact
    contact_tag: "İLETİŞİME GEÇİN",
    contact_title: "Birlikte Büyük Bir Şey İnşa Edelim",
    contact_subtitle: "Yeni projeleriniz, teknoloji danışmanlığı veya ortaklık fırsatları için doğrudan iletişime geçebilirsiniz.",
    contact_email_title: "E-Posta",
    contact_email_val: "emirhan@emtinastudio.com",
    contact_phone_title: "Telefon & WhatsApp",
    contact_phone_val: "+90 850 346 16 83",
    contact_location_title: "Lokasyon",
    contact_location_val: "Tekirdağ",
    copy_btn: "Kopyala",
    copied_btn: "Kopyalandı!",
    whatsapp_cta: "WhatsApp'tan Mesaj Yaz",
    call_cta: "Doğrudan Ara",
    email_cta: "E-Posta Gönder",

    // Footer
    footer_copyright: "Emtina Studio © 2026"
  },

  en: {
    // Nav
    nav_home: "Home",
    nav_about: "About",
    nav_services: "Services",
    nav_portfolio: "Portfolio",
    nav_process: "Process",
    nav_contact: "Contact",
    nav_cta: "Get In Touch",

    // Hero
    hero_badge: "Next-Gen Digital Architecture",
    hero_title_prefix: "Ultra Modern & High Performance",
    hero_subtitle: "Emtina Studio crafts cutting-edge SaaS platforms, mobile game architectures, and enterprise web systems with cyber speed, flawless UI/UX, and scalable engineering.",
    hero_cta_projects: "Explore Work",
    hero_cta_contact: "Get In Touch",
    hero_stat_1_val: "30+",
    hero_stat_1_lbl: "Shipped Projects",
    hero_stat_2_val: "99.8%",
    hero_stat_2_lbl: "Client Satisfaction",
    hero_stat_3_val: "8+ Yrs",
    hero_stat_3_lbl: "Engineering Experience",
    hero_stat_4_val: "100K+",
    hero_stat_4_lbl: "Active User Reach",

    // About Me
    about_tag: "ABOUT ME & FOUNDER",
    about_title: "Tech Passion, Engineering Precision",
    about_bio_1: "Hello! I am the founder of Emtina Studio. I am a full-stack software engineer specialized in building end-to-end cloud architectures, high-availability SaaS products, and high-performance mobile games with Godot Engine.",
    about_bio_2: "From Laravel and Next.js to microservices, real-time WebSocket infrastructures, and fine-tuned database architectures, I deliver complete digital transformation. Clean code, cyber security, and supreme user experience are at the core of my work.",
    about_skills_title: "Core Stack & Technologies",
    about_cta_contact: "Get In Touch",
    about_cta_projects: "View Projects",

    // Services
    services_tag: "CORE CAPABILITIES",
    services_title: "Built with Cyber Speed, Built to Scale",
    services_subtitle: "From early ideation to production environments serving millions of requests, we engineer every layer.",
    service_1_title: "SaaS & Cloud Platforms",
    service_1_desc: "Multi-tenant architectures, recurring billing pipelines, automated workflows, and scalable cloud infrastructure for modern SaaS.",
    service_2_title: "Mobile Game & App Engineering",
    service_2_desc: "Fluid 60 FPS physics, real-time multiplayer netcode, and stunning visual art built with Godot 4 Engine and cross-platform tech.",
    service_3_title: "Modern Full-Stack Web",
    service_3_desc: "Blazing fast, SEO-dominant, and reactive web applications engineered using Next.js, Laravel, and Tailwind CSS.",
    service_4_title: "APIs & Microservices",
    service_4_desc: "High-throughput, Dockerized and Redis-cached RESTful & GraphQL backend services built for enterprise reliability.",
    service_5_title: "UI/UX & Dark-Tech Design",
    service_5_desc: "Cyberpunk-inspired, dark-mode first design systems blending user psychology with micro-animations and high conversion.",
    service_6_title: "Consulting & Performance",
    service_6_desc: "Codebase refactoring, database indexing, latency elimination, security audits, and cloud cost reduction.",

    // Portfolio
    portfolio_tag: "FEATURED WORK",
    portfolio_title: "Portfolio & Shipped Products",
    portfolio_subtitle: "Flagship digital products engineered in the Emtina Studio laboratory that deliver real-world business value.",
    tab_all: "All",
    tab_web: "Web & SaaS",
    tab_game: "Mobile & Game",

    // Process
    process_tag: "DEVELOPMENT WORKFLOW",
    process_title: "End-to-End Agile Process",
    process_subtitle: "Our disciplined 4-stage engineering methodology from concept to global deployment.",
    process_1_num: "01",
    process_1_title: "Discovery & Architecture",
    process_1_desc: "Deep requirements mapping, database schema design, and selection of the optimal technology stack.",
    process_2_num: "02",
    process_2_title: "UI/UX & Prototyping",
    process_2_desc: "High-fidelity interactive prototypes with cyber-dark aesthetics and effortless user journeys.",
    process_3_num: "03",
    process_3_title: "Agile Sprints & Clean Code",
    process_3_desc: "Modular clean code architecture, rigorous unit testing, and continuous weekly demo milestones.",
    process_4_num: "04",
    process_4_title: "CI/CD, Launch & Scaling",
    process_4_desc: "Automated pipelines, cloud containerization, performance benchmarks, and post-launch maintenance.",

    // Contact
    contact_tag: "GET IN TOUCH",
    contact_title: "Let's Build Something Extraordinary",
    contact_subtitle: "Reach out directly for new project inquiries, software consulting, or collaboration opportunities.",
    contact_email_title: "Email",
    contact_email_val: "emirhan@emtinastudio.com",
    contact_phone_title: "Phone & WhatsApp",
    contact_phone_val: "+90 850 346 16 83",
    contact_location_title: "Location",
    contact_location_val: "Tekirdağ",
    copy_btn: "Copy",
    copied_btn: "Copied!",
    whatsapp_cta: "Chat on WhatsApp",
    call_cta: "Call Directly",
    email_cta: "Send Email",

    // Footer
    footer_copyright: "Emtina Studio © 2026"
  }
};

// Typewriter Texts for Hero
const typewriterPhrases = {
  tr: [
    "SaaS Platformları",
    "Mobil Oyun & Uygulamalar",
    "Yüksek Performanslı Web Sistemleri",
    "Özel Kurumsal Mimariler"
  ],
  en: [
    "SaaS Platforms",
    "Mobile Games & Apps",
    "High-Performance Web Systems",
    "Custom Enterprise Architectures"
  ]
};

// Projects Data
const projectsData = [
  {
    id: "tacveem",
    name: "Tacveem",
    category: "saas",
    badge_tr: "SaaS & Randevu",
    badge_en: "SaaS & Booking",
    desc_tr: "Modern işletmeler ve danışmanlar için çoklu takvim senkronizasyonlu, otomatik SMS/WhatsApp hatırlatmalı ve entegre online ödeme özellikli yeni nesil randevu yönetim SaaS platformu.",
    desc_en: "Next-gen appointment and calendar scheduling SaaS engineered for modern businesses, featuring automated reminders, Google/Apple calendar sync, and integrated payment flows.",
    image: "assets/images/tacveem.png",
    fallbackImage: "assets/images/tacveem-preview.svg",
    stats: [
      { label_tr: "Aktif Randevu", label_en: "Processed Bookings", value: "25,000+" },
      { label_tr: "Uptime Skoru", label_en: "Uptime Rate", value: "%99.98" },
      { label_tr: "Kaçırılan Randevu", label_en: "No-Show Drop", value: "-%45" }
    ],
    tags: ["Laravel 11", "Next.js 14", "PostgreSQL", "Stripe & Iyzico", "Redis", "Tailwind CSS"]
  },
  {
    id: "ebakim",
    name: "eBakım",
    category: "saas",
    badge_tr: "Endüstriyel Telemetri SaaS",
    badge_en: "Industrial Telemetry SaaS",
    desc_tr: "Üretim tesisleri, fabrikalar ve araç filoları için kestirimci bakım, QR kodlu hızlı ekipman tanıma ve sensör telemetrisi sunan uçtan uca IoT destekli bakım yönetim sistemi.",
    desc_en: "Comprehensive IoT-enabled maintenance management system for manufacturing plants and vehicle fleets, featuring QR asset tagging, predictive maintenance, and real-time telemetry.",
    image: "assets/images/ebakim.png",
    fallbackImage: "assets/images/ebakim-preview.svg",
    stats: [
      { label_tr: "Kayıtlı Ekipman", label_en: "Tracked Assets", value: "1,420+" },
      { label_tr: "Arıza Azalması", label_en: "Downtime Reduction", value: "-%34" },
      { label_tr: "Ortalama Onarım", label_en: "Mean Time to Repair", value: "1.8 Saat" }
    ],
    tags: ["Vue 3", "Laravel REST API", "PostgreSQL", "Docker", "WebSockets", "IoT Sensors"]
  },
  {
    id: "rivalkick",
    name: "RivalKick",
    category: "game",
    badge_tr: "Godot Mobil Futbol Oyunu",
    badge_en: "Godot Mobile Football Game",
    desc_tr: "Godot 4 Engine ile sıfırdan geliştirilen, gerçek zamanlı fizik motoruna, düşük gecikmeli P2P netcode'a ve siber estetiğe sahip rekabetçi arcade mobil futbol oyunu.",
    desc_en: "Competitive arcade mobile soccer game built from the ground up on Godot 4 Engine, featuring real-time custom 2D physics, ultra-low-latency P2P netcode, and cyber aesthetic.",
    image: "assets/images/rivalkick.png",
    fallbackImage: "assets/images/rivalkick-preview.svg",
    stats: [
      { label_tr: "Performans", label_en: "Engine Framerate", value: "60 FPS Sabit" },
      { label_tr: "Ağ Gecikmesi", label_en: "Average Net Latency", value: "<25 ms" },
      { label_tr: "Hedef Platform", label_en: "Target OS", value: "iOS & Android" }
    ],
    tags: ["Godot 4", "GDScript / C#", "WebSockets Netcode", "Node.js Matchmaker", "Spine 2D"]
  },
  {
    id: "odak",
    name: "O.D.A.K.",
    category: "saas",
    badge_tr: "Deep Work & Verimlilik",
    badge_en: "Deep Work & Productivity",
    desc_tr: "Yazılımcılar, araştırmacılar ve üreticiler için bilişsel akış (flow state) durumunu tetikleyen, çift kulaklı ses sentezleyici ve dikkat dağıtıcı blokeri içeren odaklanma motoru.",
    desc_en: "Cognitive flow-state engine for software engineers and researchers, featuring binaural audio synthesis, distraction shielding, and deep work cycle analytics.",
    image: "assets/images/odak.png",
    fallbackImage: "assets/images/odak-preview.svg",
    stats: [
      { label_tr: "Kayıtlı Odak Süresi", label_en: "Tracked Deep Hours", value: "85,000+" },
      { label_tr: "Üretkenlik Artışı", label_en: "Productivity Lift", value: "%42" },
      { label_tr: "Çevrimdışı Çalışma", label_en: "Offline Support", value: "%100 PWA" }
    ],
    tags: ["Next.js 14", "Web Audio API", "Tailwind CSS", "IndexedDB", "PWA", "Supabase"]
  }
];

// Global Helper to safely refresh Lucide Icons
function refreshLucideIcons() {
  if (typeof window.lucide !== 'undefined' && window.lucide && typeof window.lucide.createIcons === 'function') {
    window.lucide.createIcons();
  }
}

// Global Helper to bind Spotlight Mousemove to cards
function initSpotlightCards() {
  const cards = document.querySelectorAll('.spotlight-card');
  cards.forEach(card => {
    if (card._hasSpotlightBound) return;
    card._hasSpotlightBound = true;
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
  });
}

// Alpine.js Registration
document.addEventListener('alpine:init', () => {

  // Global Language Store
  Alpine.store('app', {
    lang: localStorage.getItem('emtina_lang') || 'tr',
    isMobileMenuOpen: false,

    toggleLang() {
      this.lang = this.lang === 'tr' ? 'en' : 'tr';
      localStorage.setItem('emtina_lang', this.lang);
      document.documentElement.lang = this.lang;
      window.dispatchEvent(new CustomEvent('lang-changed', { detail: { lang: this.lang } }));
      setTimeout(refreshLucideIcons, 50);
    },

    setLang(targetLang) {
      this.lang = targetLang;
      localStorage.setItem('emtina_lang', this.lang);
      document.documentElement.lang = this.lang;
      window.dispatchEvent(new CustomEvent('lang-changed', { detail: { lang: this.lang } }));
      setTimeout(refreshLucideIcons, 50);
    },

    t(key) {
      if (!translations[this.lang]) return key;
      return translations[this.lang][key] || translations['tr'][key] || key;
    }
  });

  // Typewriter Component
  Alpine.data('heroTypewriter', () => ({
    text: '',
    phraseIndex: 0,
    charIndex: 0,
    isDeleting: false,
    typingSpeed: 90,
    deleteSpeed: 45,
    pauseBetween: 2200,

    init() {
      this.type();
      window.addEventListener('lang-changed', () => {
        this.phraseIndex = 0;
        this.charIndex = 0;
        this.isDeleting = false;
        this.text = '';
      });
    },

    type() {
      const currentLang = Alpine.store('app') ? Alpine.store('app').lang : 'tr';
      const phrases = typewriterPhrases[currentLang] || typewriterPhrases['tr'];
      const currentPhrase = phrases[this.phraseIndex % phrases.length];

      if (this.isDeleting) {
        this.text = currentPhrase.substring(0, this.charIndex - 1);
        this.charIndex--;
      } else {
        this.text = currentPhrase.substring(0, this.charIndex + 1);
        this.charIndex++;
      }

      let delta = this.isDeleting ? this.deleteSpeed : this.typingSpeed;

      if (!this.isDeleting && this.text === currentPhrase) {
        delta = this.pauseBetween;
        this.isDeleting = true;
      } else if (this.isDeleting && this.text === '') {
        this.isDeleting = false;
        this.phraseIndex++;
        delta = 350;
      }

      setTimeout(() => this.type(), delta);
    }
  }));

  // Portfolio Component (Clean Showcase - No Modals)
  Alpine.data('portfolioSection', () => ({
    activeTab: 'all',
    projects: projectsData,

    init() {
      this.$nextTick(() => {
        initSpotlightCards();
        refreshLucideIcons();
      });
    },

    get filteredProjects() {
      const filtered = this.activeTab === 'all' 
        ? this.projects 
        : this.projects.filter(p => p.category === this.activeTab);
      
      this.$nextTick(() => {
        initSpotlightCards();
        refreshLucideIcons();
      });
      return filtered;
    }
  }));

  // Contact Info Component (Copy to clipboard & direct communication)
  Alpine.data('contactInfo', () => ({
    copiedEmail: false,
    copiedPhone: false,

    copyEmail() {
      navigator.clipboard.writeText('emirhan@emtinastudio.com').then(() => {
        this.copiedEmail = true;
        setTimeout(() => { this.copiedEmail = false; }, 3000);
      });
    },

    copyPhone() {
      navigator.clipboard.writeText('+908503461683').then(() => {
        this.copiedPhone = true;
        setTimeout(() => { this.copiedPhone = false; }, 3000);
      });
    }
  }));

});

// Global Event Listeners & Canvas Network
document.addEventListener('DOMContentLoaded', () => {
  refreshLucideIcons();
  initSpotlightCards();

  // Background Cyber Canvas Matrix / Node Network
  const canvas = document.getElementById('cyber-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const count = Math.min(45, Math.floor(width / 32));

    for (let i = 0; i < count; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35,
        radius: Math.random() * 1.4 + 0.7,
        color: Math.random() > 0.5 ? 'rgba(6, 182, 212, ' : 'rgba(139, 92, 246, '
      });
    }

    let mousePos = { x: -1000, y: -1000 };
    window.addEventListener('mousemove', (e) => {
      mousePos.x = e.clientX;
      mousePos.y = e.clientY;
    });

    function renderNetwork() {
      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color + '0.7)';
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dx = p.x - p2.x;
          const dy = p.y - p2.y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 130) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            const alpha = (1 - dist / 130) * 0.16;
            ctx.strokeStyle = `rgba(6, 182, 212, ${alpha})`;
            ctx.lineWidth = 0.8;
            ctx.stroke();
          }
        }

        const mdx = p.x - mousePos.x;
        const mdy = p.y - mousePos.y;
        const mdist = Math.sqrt(mdx * mdx + mdy * mdy);
        if (mdist < 140) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(mousePos.x, mousePos.y);
          const alpha = (1 - mdist / 140) * 0.3;
          ctx.strokeStyle = `rgba(139, 92, 246, ${alpha})`;
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }

      requestAnimationFrame(renderNetwork);
    }
    renderNetwork();
  }
});
