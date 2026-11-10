'use client';

import { ArrowDownRight, ArrowUpRight, BookOpen, Code2, Download, Gamepad2, Globe2, Layers3, Mail, Megaphone, Menu, Phone, Rocket, Sparkles, X } from 'lucide-react';
import { useEffect, useState } from 'react';

type Language = 'tr' | 'en';

const copy = {
  tr: {
    nav: ['Yaklaşım', 'Hakkımda', 'Projeler', 'Kitap'],
    collaborate: 'Birlikte çalışalım',
    heroEyebrow: 'DİJİTALDE İZ BIRAKAN FİKİRLER', hero: ['Fikirleri', 'deneyime', 'dönüştürüyoruz.'],
    heroBody: 'Emtina Studio; oyun, girişim, web, yazılım ve dijital pazarlamayı tek bir üretim çatısında buluşturur.',
    explore: 'Çalışmaları keşfet', discover: 'Stüdyoyu tanı', scroll: 'Kaydırarak keşfet',
    approach: 'YAKLAŞIM', approachLead: ['Bir fikrin ihtiyacı olan tüm ', 'ekipler', ' aynı ', 'stüdyoda.'],
    approachBody: 'Emtina Studio; oyun fikirlerinden web deneyimlerine, büyüme stratejisinden sosyal medya yönetimine kadar dijital üretimin farklı katmanlarını birbirine bağlar. Amaç; iyi fikirleri tek tek değil, uçtan uca büyütmek.',
    principles: [['Fikri başlat', 'Girişim ve ürün fikirlerini net bir yola dönüştür.'], ['Deneyimi kur', 'Web, yazılım ve içerik katmanlarını tek sistemde birleştir.'], ['Büyümeyi hızlandır', 'Veri, pazarlama ve toplulukla görünürlüğü güçlendir.']],
    about: 'HAKKIMDA', aboutName: 'EMİRHAN ÇETİN', aboutTitle: ['İşletme perspektifi,', 'teknik üretim', ' ve büyüme odağı.'],
    aboutBody: 'Karabük Üniversitesi İşletme mezunu Emirhan Çetin, dijital pazarlama stratejileri geliştirme konusunda uzmanlaşıyor. İşletme perspektifini SQL ve HTML/CSS yetkinlikleriyle birleştirerek veri odaklı büyüme ve performans pazarlaması süreçleri üzerinde çalışıyor.',
    stats: [['Büyüme odağı', 'Kampanya optimizasyonu'], ['Dijital deneyim', 'UX ve varlık yönetimi']],
    activeProject: 'AKTİF PROJE', activeDescription: 'Şu an odağımızda olan girişim.', project: 'GİRİŞİM', tacveem: 'Emtina Studio çatısı altında geliştirilen aktif proje. Ürün hikâyesi, hedef kitle, özellikler ve bağlantı eklendiğinde bu kart doğrudan yayına hazırdır.', tacveemCta: 'Tacveem hakkında konuşalım',
    production: 'EMTINA STUDIO / ÜRETİM ALANLARI', services: ['Oyun & girişim', 'Web & dijital deneyim', 'Yazılım geliştirme', 'Sosyal medya & büyüme'], whole: 'TEK ÇATI, BÜTÜNSEL ÜRETİM', serviceTitle: ['Fikirden', 'görünürlüğe.'], serviceBody: 'Strateji, üretim ve iletişimi ayrı parçalar yerine aynı yönü güçlendiren bir bütün olarak ele alıyoruz.',
    book: 'ÜCRETSİZ KİTAP', bookEyebrow: 'OKU / DÜŞÜN / HAREKET ET', bookTitle: ['Simülasyondan Çıkış:', 'Kendi Hikâyeni Kodla'], bookBody: 'İnsanların hayatına dokunmak amacıyla ücretsiz paylaşılan bu kitap; alışılmış döngüleri sorgulamak, sorumluluk almak ve kendi yönünü çizmek üzerine bir davet.', quote: '“Kodlar yazıldı. Sistem hazır.”', download: 'Ücretsiz indir',
    contactEyebrow: 'SONRAKİ FİKİR SENİN OLABİLİR', contactTitle: ['Bir şeyleri', 'harekete', ' geçirelim.'], contactBody: 'Yeni bir ürün, dijital bir deneyim ya da birlikte büyütecek bir fikir için kapı açık.', contact: 'İLETİŞİM', top: 'Başa dön', footerTop: 'Yukarı çık ↑',
  },
  en: {
    nav: ['Approach', 'About', 'Projects', 'Book'],
    collaborate: 'Let’s work together',
    heroEyebrow: 'IDEAS THAT LEAVE A MARK', hero: ['Turning ideas', 'into', 'experiences.'],
    heroBody: 'Emtina Studio brings games, ventures, web, software and digital marketing together under one creative roof.',
    explore: 'Explore the work', discover: 'Meet the studio', scroll: 'Scroll to explore',
    approach: 'APPROACH', approachLead: ['Every capability an idea needs, ', 'together', ' in one ', 'studio.'],
    approachBody: 'From game concepts to web experiences, growth strategy to social media management, Emtina Studio connects every layer of digital creation. The goal is not simply to launch ideas, but to grow them end to end.',
    principles: [['Start the idea', 'Turn venture and product ideas into a clear direction.'], ['Build the experience', 'Bring web, software and content layers into one system.'], ['Accelerate growth', 'Strengthen visibility through data, marketing and community.']],
    about: 'ABOUT', aboutName: 'EMİRHAN ÇETİN', aboutTitle: ['Business perspective,', 'technical craft', ' and growth focus.'],
    aboutBody: 'A Business Administration graduate of Karabük University, Emirhan Çetin focuses on developing digital marketing strategies. He combines business perspective with SQL and HTML/CSS skills to work on data-driven growth and performance marketing.',
    stats: [['Growth focus', 'Campaign optimization'], ['Digital experience', 'UX and asset management']],
    activeProject: 'ACTIVE PROJECT', activeDescription: 'The venture currently in focus.', project: 'VENTURE', tacveem: 'An active project developed under Emtina Studio. This card is ready for a product story, audience, features and a live link.', tacveemCta: 'Talk about Tacveem',
    production: 'EMTINA STUDIO / CREATIVE AREAS', services: ['Games & ventures', 'Web & digital experiences', 'Software development', 'Social media & growth'], whole: 'ONE ROOF, COMPLETE CREATION', serviceTitle: ['From idea', 'to visibility.'], serviceBody: 'We treat strategy, creation and communication as one whole working toward the same direction.',
    book: 'FREE BOOK', bookEyebrow: 'READ / REFLECT / ACT', bookTitle: ['Breaking Out of the Simulation:', 'Code Your Own Story'], bookBody: 'Shared free of charge to make a positive difference in people’s lives, this book is an invitation to question routines, take responsibility and write your own direction.', quote: '“The code is written. The system is ready.”', download: 'Download free',
    contactEyebrow: 'THE NEXT IDEA COULD BE YOURS', contactTitle: ['Let’s set', 'things', ' in motion.'], contactBody: 'The door is open for a new product, a digital experience or an idea we can grow together.', contact: 'CONTACT', top: 'Back to top', footerTop: 'Back to top ↑',
  },
} as const;

const anchors = ['#yaklasim', '#hakkimda', '#projeler', '#kitap'];
const serviceIcons = [Gamepad2, Globe2, Code2, Megaphone];
const principleIcons = [Rocket, Layers3, Sparkles];

function Mark() { return <img src="/emtina-logo.png" alt="Emtina Studio" />; }

export default function Home() {
  const [language, setLanguage] = useState<Language>('tr');
  const [menuOpen, setMenuOpen] = useState(false);
  const t = copy[language];

  useEffect(() => { document.documentElement.lang = language; }, [language]);

  const toggleLanguage = () => setLanguage(language === 'tr' ? 'en' : 'tr');
  return (
    <main>
      <div className="noise" aria-hidden="true" />
      <header className="site-header">
        <a href="#ana" className="brand" aria-label="Emtina Studio home"><Mark /><span>EMTINA<span>STUDIO</span></span></a>
        <nav className="desktop-nav" aria-label="Main navigation">{t.nav.map((label, index) => <a key={anchors[index]} href={anchors[index]}>{label}</a>)}</nav>
        <div className="header-actions"><button className="language-switch" onClick={toggleLanguage} aria-label={language === 'tr' ? 'Switch to English' : 'Türkçeye geç'}><Globe2 size={14} /> {language === 'tr' ? 'EN' : 'TR'}</button><a className="header-cta" href="#iletisim">{t.collaborate} <ArrowUpRight size={15} /></a></div>
        <button className="menu-button" onClick={() => setMenuOpen(!menuOpen)} aria-expanded={menuOpen} aria-controls="mobile-nav" aria-label="Menu">{menuOpen ? <X /> : <Menu />}</button>
        {menuOpen && <nav id="mobile-nav" className="mobile-nav" aria-label="Mobile navigation">{t.nav.map((label, index) => <a key={anchors[index]} href={anchors[index]} onClick={() => setMenuOpen(false)}>{label}</a>)}<a href="#iletisim" onClick={() => setMenuOpen(false)}>{t.collaborate} <ArrowUpRight size={16} /></a></nav>}
      </header>

      <section id="ana" className="hero section-wrap"><div className="orb orb-cyan" aria-hidden="true" /><div className="orb orb-violet" aria-hidden="true" /><div className="hero-grid" aria-hidden="true" />
        <div className="hero-copy"><p className="eyebrow enter"><span /> {t.heroEyebrow}</p><h1 className="enter delay-1">{t.hero[0]}<br /><em>{t.hero[1]}</em><br />{t.hero[2]}</h1><p className="hero-lede enter delay-2">{t.heroBody}</p><div className="hero-actions enter delay-3"><a className="button button-primary" href="#projeler">{t.explore} <ArrowDownRight size={18} /></a><a className="text-link" href="#hakkimda">{t.discover} <span>→</span></a></div></div>
        <div className="hero-art enter delay-2" aria-label="Emtina Studio mark"><div className="orbit orbit-one" /><div className="orbit orbit-two" /><div className="hero-mark"><Mark /></div><p className="art-caption">MAKE / LEARN / SHIP</p></div><div className="scroll-cue"><span /> {t.scroll}</div>
      </section>

      <section id="yaklasim" className="section-wrap manifesto reveal"><div className="section-label"><span>01</span> {t.approach}</div><div className="manifesto-copy"><p className="display-copy">{t.approachLead[0]}<strong>{t.approachLead[1]}</strong>{t.approachLead[2]}<i>{t.approachLead[3]}</i></p><p className="body-copy">{t.approachBody}</p><div className="principles">{t.principles.map(([title, body], index) => { const Icon = principleIcons[index]; return <article key={title}><span>0{index + 1}</span><Icon size={24} /><h3>{title}</h3><p>{body}</p></article>; })}</div></div></section>

      <section id="hakkimda" className="about section-wrap reveal"><div className="about-photo"><img src="/emirhan-cetin.png" alt="Emirhan Çetin" /><div className="photo-glow" /></div><div className="about-copy"><div className="section-label"><span>02</span> {t.about}</div><p className="eyebrow">{t.aboutName}</p><h2>{t.aboutTitle[0]}<br /><em>{t.aboutTitle[1]}</em>{t.aboutTitle[2]}</h2><p>{t.aboutBody}</p><div className="about-stats">{t.stats.map(([title, body]) => <div key={title}><b>{title}</b><span>{body}</span></div>)}</div></div></section>

      <section id="projeler" className="projects section-wrap reveal"><div className="projects-top"><div className="section-label"><span>03</span> {t.activeProject}</div><p>{t.activeDescription}</p></div><div className="project-grid"><article className="project-card tacveem-card"><div className="project-number">01 / {t.activeProject}</div><div className="project-symbol">T<span>V</span></div><div className="project-content"><p>{t.project}</p><h3>Tacveem</h3><p className="project-description">{t.tacveem}</p><a href="#iletisim">{t.tacveemCta} <ArrowUpRight size={17} /></a></div></article><article className="project-card services-card"><div className="project-number">{t.production}</div><div className="service-list">{t.services.map((service, index) => { const Icon = serviceIcons[index]; return <div key={service}><Icon size={20} /><span>{service}</span></div>; })}</div><div className="project-content"><p>{t.whole}</p><h3>{t.serviceTitle[0]}<br />{t.serviceTitle[1]}</h3><p className="project-description">{t.serviceBody}</p></div></article></div></section>

      <section id="kitap" className="book section-wrap reveal"><div className="book-image"><div className="book-aura" /><img src="/simulasyondan-cikis-kapak.png" alt="Simülasyondan Çıkış book cover" /></div><div className="book-copy"><div className="section-label"><span>04</span> {t.book}</div><p className="eyebrow"><BookOpen size={15} /> {t.bookEyebrow}</p><h2>{t.bookTitle[0]}<br /><em>{t.bookTitle[1]}</em></h2><p>{t.bookBody}</p><div className="book-quote">{t.quote}</div><a className="button button-primary" href="/simulasyondan-cikis-kendi-hikayeni-kodla.pdf" download>{t.download} <Download size={18} /></a></div></section>

      <section id="iletisim" className="contact section-wrap reveal"><div className="contact-grid" aria-hidden="true" /><p className="eyebrow">{t.contactEyebrow}</p><h2>{t.contactTitle[0]}<br /><em>{t.contactTitle[1]}</em>{t.contactTitle[2]}</h2><p>{t.contactBody}</p><div className="contact-options"><span>{t.contact}</span><a className="contact-link" href="mailto:emirhan@emtinastudio.com"><Mail size={17} /> emirhan@emtinastudio.com</a><a className="contact-link" href="tel:08503461683"><Phone size={17} /> 0850 346 16 83</a></div><a className="button button-light" href="#ana">{t.top} <ArrowUpRight size={18} /></a></section>
      <footer className="footer section-wrap"><a href="#ana" className="brand"><Mark /><span>EMTINA<span>STUDIO</span></span></a><p>© {new Date().getFullYear()} Emtina Studio</p><a href="#ana">{t.footerTop}</a></footer>
    </main>
  );
}
