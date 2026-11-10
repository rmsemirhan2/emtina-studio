import os

images_dir = "/Users/rms/.gemini/antigravity/scratch/emtina-studio/assets/images"

# 1. Tacveem Preview SVG
tacveem_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="tacBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#0b1120" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="800" height="500" fill="url(#tacBg)" rx="16"/>
  <!-- Grid background -->
  <g opacity="0.08" stroke="#06b6d4" stroke-width="1">
    <pattern id="tacGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none"/>
    </pattern>
    <rect width="800" height="500" fill="url(#tacGrid)" />
  </g>
  <!-- Top bar -->
  <rect x="40" y="30" width="720" height="50" rx="10" fill="#1e293b" fill-opacity="0.6" stroke="#334155" stroke-width="1"/>
  <circle cx="70" cy="55" r="7" fill="#ef4444" />
  <circle cx="95" cy="55" r="7" fill="#f59e0b" />
  <circle cx="120" cy="55" r="7" fill="#10b981" />
  <text x="160" y="60" fill="#94a3b8" font-family="sans-serif" font-size="13" font-weight="600">tacveem.io &bull; Randevu &amp; Takvim Yönetim Platformu</text>
  <rect x="620" y="42" width="120" height="26" rx="6" fill="url(#cyanGrad)" />
  <text x="642" y="59" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">+ YENİ RANDEVU</text>

  <!-- Left Sidebar mini -->
  <rect x="40" y="100" width="180" height="360" rx="12" fill="#111827" fill-opacity="0.8" stroke="#1f2937" stroke-width="1"/>
  <rect x="60" y="125" width="140" height="32" rx="8" fill="#06b6d4" fill-opacity="0.15" stroke="#06b6d4" stroke-width="1"/>
  <circle cx="78" cy="141" r="5" fill="#06b6d4" />
  <text x="94" y="146" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">Canlı Takvim</text>
  <text x="94" y="195" fill="#64748b" font-family="sans-serif" font-size="12">Müşteri Listesi</text>
  <text x="94" y="240" fill="#64748b" font-family="sans-serif" font-size="12">Hizmet Paketleri</text>
  <text x="94" y="285" fill="#64748b" font-family="sans-serif" font-size="12">Ödeme Entegrasyonu</text>
  <text x="94" y="330" fill="#64748b" font-family="sans-serif" font-size="12">Analitik Raporlar</text>
  <rect x="60" y="375" width="140" height="60" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1"/>
  <text x="75" y="400" fill="#a5b4fc" font-family="sans-serif" font-size="11" font-weight="bold">Doluluk Oranı</text>
  <text x="75" y="422" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="900">%94.2</text>

  <!-- Calendar Main Grid -->
  <rect x="240" y="100" width="520" height="360" rx="12" fill="#0f172a" fill-opacity="0.9" stroke="#1e293b" stroke-width="1"/>
  <!-- Days header -->
  <text x="270" y="130" fill="#94a3b8" font-family="sans-serif" font-size="12" font-weight="bold">PAZARTESİ</text>
  <text x="380" y="130" fill="#94a3b8" font-family="sans-serif" font-size="12" font-weight="bold">SALI</text>
  <text x="490" y="130" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">ÇARŞAMBA (BUGÜN)</text>
  <text x="640" y="130" fill="#94a3b8" font-family="sans-serif" font-size="12" font-weight="bold">PERŞEMBE</text>

  <!-- Appointments blocks -->
  <rect x="260" y="150" width="100" height="70" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="270" y="172" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="bold">09:30 - Dr. Kaya</text>
  <text x="270" y="190" fill="#64748b" font-family="sans-serif" font-size="9">Konsültasyon</text>

  <rect x="370" y="210" width="100" height="85" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="380" y="232" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="bold">11:00 - VIP Seans</text>
  <text x="380" y="250" fill="#64748b" font-family="sans-serif" font-size="9">Online Görüşme</text>

  <!-- Active glowing appointment -->
  <rect x="480" y="170" width="130" height="110" rx="10" fill="#0369a1" fill-opacity="0.3" stroke="#06b6d4" stroke-width="2" filter="url(#neonGlow)"/>
  <rect x="480" y="170" width="130" height="110" rx="10" fill="#0f172a" stroke="#06b6d4" stroke-width="1.5"/>
  <circle cx="500" cy="190" r="4" fill="#22c55e" />
  <text x="510" y="194" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">14:00 - Aktif Randevu</text>
  <text x="495" y="216" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="bold">Ahmet Yılmaz</text>
  <text x="495" y="234" fill="#94a3b8" font-family="sans-serif" font-size="10">Strateji Danışmanlığı</text>
  <rect x="495" y="250" width="80" height="18" rx="4" fill="#06b6d4" fill-opacity="0.2"/>
  <text x="507" y="263" fill="#38bdf8" font-family="sans-serif" font-size="9" font-weight="bold">ONAYLANDI</text>

  <rect x="630" y="280" width="110" height="80" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <text x="640" y="302" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="bold">16:30 - Klinik</text>
  <text x="640" y="320" fill="#64748b" font-family="sans-serif" font-size="9">Periyodik Kontrol</text>

  <!-- Stats footer in card -->
  <rect x="260" y="380" width="480" height="60" rx="8" fill="#1e293b" fill-opacity="0.4" stroke="#334155" stroke-dasharray="4 4" stroke-width="1"/>
  <text x="280" y="415" fill="#94a3b8" font-family="sans-serif" font-size="11">Google Calendar &bull; SMS Hatırlatma &bull; Stripe/Iyzico Ödeme &bull; Çoklu Şube</text>
</svg>"""

# 2. eBakım Preview SVG
ebakim_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="ebkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#111827" />
      <stop offset="50%" stop-color="#090d16" />
      <stop offset="100%" stop-color="#030712" />
    </linearGradient>
    <linearGradient id="purpGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" />
      <stop offset="100%" stop-color="#ec4899" />
    </linearGradient>
    <filter id="ebkGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="800" height="500" fill="url(#ebkBg)" rx="16"/>
  <!-- Top bar -->
  <rect x="40" y="30" width="720" height="50" rx="10" fill="#1f2937" fill-opacity="0.6" stroke="#374151" stroke-width="1"/>
  <circle cx="70" cy="55" r="7" fill="#ef4444" />
  <circle cx="95" cy="55" r="7" fill="#f59e0b" />
  <circle cx="120" cy="55" r="7" fill="#10b981" />
  <text x="160" y="60" fill="#a78bfa" font-family="sans-serif" font-size="13" font-weight="bold">eBakım Enterprise</text>
  <text x="290" y="60" fill="#6b7280" font-family="sans-serif" font-size="12">| Endüstriyel Ekipman &amp; Filo Bakım Telemetrisi</text>
  <rect x="630" y="42" width="110" height="26" rx="6" fill="url(#purpGrad)" />
  <text x="647" y="59" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">QR TARA / GİR</text>

  <!-- 3 Top Metric Cards -->
  <rect x="40" y="100" width="220" height="90" rx="10" fill="#1f2937" stroke="#374151" stroke-width="1"/>
  <text x="60" y="125" fill="#9ca3af" font-family="sans-serif" font-size="11" font-weight="bold">AKTİF MAKİNE PARKI</text>
  <text x="60" y="158" fill="#ffffff" font-family="sans-serif" font-size="24" font-weight="900">1,428 Adet</text>
  <text x="60" y="178" fill="#10b981" font-family="sans-serif" font-size="11">&uarr; %99.4 Sağlık Skoru</text>

  <rect x="290" y="100" width="220" height="90" rx="10" fill="#1f2937" stroke="#8b5cf6" stroke-width="1.5" filter="url(#ebkGlow)"/>
  <rect x="290" y="100" width="220" height="90" rx="10" fill="#1e1b4b" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="310" y="125" fill="#c4b5fd" font-family="sans-serif" font-size="11" font-weight="bold">PLANLI PERİYODİK BAKIM</text>
  <text x="310" y="158" fill="#a78bfa" font-family="sans-serif" font-size="24" font-weight="900">38 İş Emri</text>
  <text x="310" y="178" fill="#38bdf8" font-family="sans-serif" font-size="11">&bull; Bugün 12 tamamlandı</text>

  <rect x="540" y="100" width="220" height="90" rx="10" fill="#1f2937" stroke="#374151" stroke-width="1"/>
  <text x="560" y="125" fill="#9ca3af" font-family="sans-serif" font-size="11" font-weight="bold">ORTALAMA ONARIM (MTTR)</text>
  <text x="560" y="158" fill="#f59e0b" font-family="sans-serif" font-size="24" font-weight="900">1.8 Saat</text>
  <text x="560" y="178" fill="#10b981" font-family="sans-serif" font-size="11">&darr; -%34 Arıza Süresi</text>

  <!-- Telemetry Table & QR Preview -->
  <rect x="40" y="210" width="470" height="250" rx="12" fill="#111827" stroke="#1f2937" stroke-width="1"/>
  <text x="60" y="240" fill="#f3f4f6" font-family="sans-serif" font-size="13" font-weight="bold">Kritik Ekipman Telemetri &amp; Sensör Durumu</text>

  <!-- Row 1 -->
  <line x1="60" y1="260" x2="490" y2="260" stroke="#374151" stroke-width="0.5"/>
  <text x="60" y="285" fill="#e5e7eb" font-family="sans-serif" font-size="12" font-weight="bold">CNC Torna Ünitesi #04</text>
  <text x="60" y="302" fill="#9ca3af" font-family="sans-serif" font-size="10">Konum: A-Blok Pres Hattı</text>
  <rect x="340" y="275" width="60" height="20" rx="4" fill="#065f46"/>
  <text x="350" y="289" fill="#34d399" font-family="sans-serif" font-size="10" font-weight="bold">OPTIMAL</text>
  <text x="430" y="289" fill="#e5e7eb" font-family="sans-serif" font-size="12" font-weight="bold">64°C / 1.2G</text>

  <!-- Row 2 -->
  <line x1="60" y1="320" x2="490" y2="320" stroke="#374151" stroke-width="0.5"/>
  <text x="60" y="345" fill="#e5e7eb" font-family="sans-serif" font-size="12" font-weight="bold">Hidrolik Pompa Grubu B-2</text>
  <text x="60" y="362" fill="#9ca3af" font-family="sans-serif" font-size="10">Konum: Soğutma Kulesi</text>
  <rect x="340" y="335" width="65" height="20" rx="4" fill="#78350f"/>
  <text x="348" y="349" fill="#fde047" font-family="sans-serif" font-size="10" font-weight="bold">UYARI</text>
  <text x="430" y="349" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold">82°C / Yağ Seviyesi</text>

  <!-- Row 3 -->
  <line x1="60" y1="380" x2="490" y2="380" stroke="#374151" stroke-width="0.5"/>
  <text x="60" y="405" fill="#e5e7eb" font-family="sans-serif" font-size="12" font-weight="bold">Robotik Taşıma Kolu #12</text>
  <text x="60" y="422" fill="#9ca3af" font-family="sans-serif" font-size="10">Konum: Montaj Bandı</text>
  <rect x="340" y="395" width="60" height="20" rx="4" fill="#065f46"/>
  <text x="350" y="409" fill="#34d399" font-family="sans-serif" font-size="10" font-weight="bold">OPTIMAL</text>
  <text x="430" y="409" fill="#e5e7eb" font-family="sans-serif" font-size="12" font-weight="bold">42°C / 0.3G</text>

  <!-- Right QR & Asset Card -->
  <rect x="530" y="210" width="230" height="250" rx="12" fill="#18181b" stroke="#8b5cf6" stroke-width="1"/>
  <text x="550" y="240" fill="#a78bfa" font-family="sans-serif" font-size="12" font-weight="bold">Hızlı Varlık Tanıma</text>
  <!-- Stylized QR box -->
  <rect x="575" y="260" width="140" height="140" rx="10" fill="#ffffff"/>
  <rect x="590" y="275" width="35" height="35" fill="#000000"/>
  <rect x="597" y="282" width="21" height="21" fill="#ffffff"/>
  <rect x="665" y="275" width="35" height="35" fill="#000000"/>
  <rect x="672" y="282" width="21" height="21" fill="#ffffff"/>
  <rect x="590" y="350" width="35" height="35" fill="#000000"/>
  <rect x="597" y="357" width="21" height="21" fill="#ffffff"/>
  <rect x="635" y="315" width="20" height="20" fill="#8b5cf6"/>
  <rect x="665" y="350" width="30" height="30" fill="#000000"/>
  <text x="560" y="430" fill="#9ca3af" font-family="sans-serif" font-size="11" text-anchor="start">Saha personeli mobil kamera ile anında kayıt oluşturur.</text>
</svg>"""

# 3. RivalKick Preview SVG
rivalkick_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <radialGradient id="stadiumGlow" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#1e1b4b" />
      <stop offset="50%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#020617" />
    </radialGradient>
    <linearGradient id="neonTurq" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4" />
      <stop offset="100%" stop-color="#10b981" />
    </linearGradient>
    <filter id="ballGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="10" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="800" height="500" fill="url(#stadiumGlow)" rx="16"/>
  
  <!-- Cyber Stadium Pitch Lines -->
  <ellipse cx="400" cy="270" rx="340" ry="170" fill="none" stroke="#06b6d4" stroke-opacity="0.3" stroke-width="2" />
  <line x1="60" y1="270" x2="740" y2="270" stroke="#06b6d4" stroke-opacity="0.2" stroke-width="2" />
  <circle cx="400" cy="270" r="70" fill="none" stroke="#06b6d4" stroke-opacity="0.4" stroke-width="2" stroke-dasharray="6 4" />
  <circle cx="400" cy="270" r="6" fill="#06b6d4" />

  <!-- Goal Area Left & Right -->
  <rect x="60" y="210" width="70" height="120" fill="none" stroke="#3b82f6" stroke-opacity="0.4" stroke-width="2"/>
  <rect x="670" y="210" width="70" height="120" fill="none" stroke="#ec4899" stroke-opacity="0.4" stroke-width="2"/>

  <!-- Top HUD Bar -->
  <rect x="220" y="25" width="360" height="60" rx="12" fill="#030712" fill-opacity="0.85" stroke="#374151" stroke-width="1.5"/>
  <text x="250" y="62" fill="#38bdf8" font-family="sans-serif" font-size="22" font-weight="900">CYBER FC</text>
  <text x="375" y="63" fill="#ffffff" font-family="sans-serif" font-size="26" font-weight="900">3</text>
  <text x="396" y="61" fill="#f43f5e" font-family="sans-serif" font-size="16" font-weight="bold">:</text>
  <text x="415" y="63" fill="#ffffff" font-family="sans-serif" font-size="26" font-weight="900">2</text>
  <text x="450" y="62" fill="#f43f5e" font-family="sans-serif" font-size="22" font-weight="900">NEO TOKYO</text>
  <rect x="365" y="15" width="70" height="18" rx="4" fill="#ef4444"/>
  <text x="382" y="28" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">88:42</text>

  <!-- Godot Engine Badge Top Left -->
  <rect x="40" y="30" width="130" height="36" rx="8" fill="#478cbf" fill-opacity="0.2" stroke="#478cbf" stroke-width="1"/>
  <circle cx="60" cy="48" r="8" fill="#478cbf"/>
  <text x="76" y="52" fill="#e0f2fe" font-family="sans-serif" font-size="11" font-weight="bold">Godot 4 Engine</text>

  <!-- Multiplayer Ping Top Right -->
  <rect x="640" y="30" width="120" height="36" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
  <circle cx="658" cy="48" r="4" fill="#22c55e"/>
  <text x="670" y="52" fill="#94a3b8" font-family="sans-serif" font-size="11">Ping: 18ms (P2P)</text>

  <!-- Player 1 (Striker Blue) -->
  <circle cx="280" cy="250" r="28" fill="#0284c7" stroke="#38bdf8" stroke-width="3" filter="url(#ballGlow)"/>
  <circle cx="280" cy="250" r="16" fill="#0f172a" />
  <text x="276" y="255" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">9</text>
  <text x="255" y="295" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">ALEX (SEN)</text>

  <!-- Cyber Ball with Speed Trails -->
  <path d="M 310 250 Q 380 230 450 220" fill="none" stroke="#22d3ee" stroke-width="4" stroke-linecap="round" opacity="0.6"/>
  <path d="M 340 252 Q 400 234 460 221" fill="none" stroke="#f43f5e" stroke-width="2" stroke-linecap="round" opacity="0.8"/>
  <circle cx="470" cy="220" r="14" fill="#ffffff" stroke="#f59e0b" stroke-width="3" filter="url(#ballGlow)"/>

  <!-- Opponent Defender (Red) -->
  <circle cx="560" cy="230" r="28" fill="#9f1239" stroke="#f43f5e" stroke-width="3"/>
  <circle cx="560" cy="230" r="16" fill="#0f172a" />
  <text x="556" y="235" fill="#f43f5e" font-family="sans-serif" font-size="12" font-weight="bold">4</text>
  <text x="540" y="275" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold">KAI (RAKİP)</text>

  <!-- Bottom Action Card -->
  <rect x="180" y="420" width="440" height="50" rx="25" fill="#030712" fill-opacity="0.9" stroke="#06b6d4" stroke-width="1.5"/>
  <text x="240" y="451" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">SUPER KICK ŞARJ %100 &bull; DOKUNMATİK JOÝSTİK AKTİF</text>
</svg>"""

# 4. O.D.A.K. Preview SVG
odak_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <radialGradient id="odakBg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#18181b" />
      <stop offset="50%" stop-color="#09090b" />
      <stop offset="100%" stop-color="#000000" />
    </radialGradient>
    <linearGradient id="glowRing" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" />
      <stop offset="50%" stop-color="#06b6d4" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>
    <filter id="odakGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="800" height="500" fill="url(#odakBg)" rx="16"/>

  <!-- Top minimalist header -->
  <rect x="40" y="30" width="720" height="50" rx="10" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="65" y="60" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="900" letter-spacing="4">O . D . A . K .</text>
  <text x="220" y="60" fill="#71717a" font-family="sans-serif" font-size="12">Deep Work &amp; Cognitive Flow State Engine</text>
  <rect x="630" y="42" width="110" height="26" rx="13" fill="#8b5cf6" fill-opacity="0.2" stroke="#8b5cf6" stroke-width="1"/>
  <circle cx="645" cy="55" r="4" fill="#a855f7" />
  <text x="658" y="59" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">DERİN AKIŞ</text>

  <!-- Big Central Focus Timer Ring -->
  <circle cx="300" cy="270" r="120" fill="none" stroke="#27272a" stroke-width="8"/>
  <circle cx="300" cy="270" r="120" fill="none" stroke="url(#glowRing)" stroke-width="8" stroke-dasharray="754" stroke-dashoffset="190" stroke-linecap="round" filter="url(#odakGlow)"/>
  <circle cx="300" cy="270" r="120" fill="none" stroke="url(#glowRing)" stroke-width="6" stroke-dasharray="754" stroke-dashoffset="190" stroke-linecap="round"/>

  <!-- Timer Inside -->
  <text x="300" y="255" fill="#71717a" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle" letter-spacing="2">KALAN SÜRE</text>
  <text x="300" y="295" fill="#ffffff" font-family="sans-serif" font-size="44" font-weight="900" text-anchor="middle" font-feature-settings="tnum">37:45</text>
  <text x="300" y="325" fill="#06b6d4" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Alfa Dalgaları (10 Hz Bimodal)</text>

  <!-- Right Side Analytics & Modules -->
  <rect x="470" y="110" width="290" height="105" rx="12" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="490" y="135" fill="#a1a1aa" font-family="sans-serif" font-size="11" font-weight="bold">GÜNLÜK ODAKLANMA HEDEFİ</text>
  <text x="490" y="170" fill="#ffffff" font-family="sans-serif" font-size="24" font-weight="900">4s 25dk / 5s 00dk</text>
  <!-- Progress bar -->
  <rect x="490" y="185" width="250" height="8" rx="4" fill="#27272a"/>
  <rect x="490" y="185" width="220" height="8" rx="4" fill="url(#glowRing)"/>

  <rect x="470" y="235" width="290" height="105" rx="12" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="490" y="260" fill="#a1a1aa" font-family="sans-serif" font-size="11" font-weight="bold">ORTAM SES SENTEZLEYİCİ</text>
  <text x="490" y="285" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold">&bull; Yağmur &amp; Siber Şehir Ambiyansı</text>
  <text x="490" y="305" fill="#71717a" font-family="sans-serif" font-size="11">Aktif Gürültü İzolasyonu Açık</text>
  <!-- Mini audio wave -->
  <path d="M 490 325 Q 510 315 530 325 T 570 325 T 610 325 T 650 325 T 690 325 T 730 325" fill="none" stroke="#8b5cf6" stroke-width="2"/>

  <rect x="470" y="360" width="290" height="105" rx="12" fill="#18181b" stroke="#27272a" stroke-width="1"/>
  <text x="490" y="385" fill="#a1a1aa" font-family="sans-serif" font-size="11" font-weight="bold">DİKKAT DAĞITICI BLOKER</text>
  <text x="490" y="410" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="bold">&check; 42 Site &amp; Bildirim Sessize Alındı</text>
  <text x="490" y="430" fill="#71717a" font-family="sans-serif" font-size="11">Dopamin döngüsü koruma modu devrede</text>
</svg>"""

with open(os.path.join(images_dir, "tacveem-preview.svg"), "w") as f:
    f.write(tacveem_svg)

with open(os.path.join(images_dir, "ebakim-preview.svg"), "w") as f:
    f.write(ebakim_svg)

with open(os.path.join(images_dir, "rivalkick-preview.svg"), "w") as f:
    f.write(rivalkick_svg)

with open(os.path.join(images_dir, "odak-preview.svg"), "w") as f:
    f.write(odak_svg)

print("All preview SVGs generated successfully!")
