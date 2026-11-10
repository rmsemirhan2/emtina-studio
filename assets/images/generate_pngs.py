import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 750

def create_gradient(draw, w, h, c1, c2):
    for y in range(h):
        r = int(c1[0] + (c2[0] - c1[0]) * y / h)
        g = int(c1[1] + (c2[1] - c1[1]) * y / h)
        b = int(c1[2] + (c2[2] - c1[2]) * y / h)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

# 1. TACVEEM PNG
im1 = Image.new("RGBA", (W, H), (9, 9, 11, 255))
d1 = ImageDraw.Draw(im1)
create_gradient(d1, W, H, (15, 23, 42), (9, 9, 11))

# Grid lines
for x in range(0, W, 40):
    d1.line([(x, 0), (x, H)], fill=(6, 182, 212, 12))
for y in range(0, H, 40):
    d1.line([(0, y), (W, y)], fill=(6, 182, 212, 12))

# App Window Frame
d1.rounded_rectangle([60, 50, W-60, H-50], radius=20, fill=(18, 24, 38, 230), outline=(51, 65, 85, 255), width=2)
# Window Top Bar
d1.rounded_rectangle([60, 50, W-60, 110], radius=20, fill=(30, 41, 59, 200))
d1.ellipse([90, 75, 104, 89], fill=(239, 68, 68))
d1.ellipse([115, 75, 129, 89], fill=(245, 158, 11))
d1.ellipse([140, 75, 154, 89], fill=(16, 185, 129))
d1.text((180, 72), "tacveem.io  •  Akıllı Randevu & Takvim Yönetim Platformu", fill=(148, 163, 184))

# Left Sidebar
d1.rounded_rectangle([90, 140, 340, H-80], radius=14, fill=(15, 23, 42, 220), outline=(30, 41, 59), width=1)
d1.rounded_rectangle([110, 170, 320, 215], radius=10, fill=(6, 182, 212, 35), outline=(6, 182, 212, 150), width=1)
d1.text((130, 183), "📅  Canlı Takvim", fill=(56, 189, 248))
d1.text((130, 245), "👥  Müşteri Veritabanı", fill=(100, 116, 139))
d1.text((130, 305), "⚡  Hizmet Paketleri", fill=(100, 116, 139))
d1.text((130, 365), "💳  Online Ödemeler (Stripe)", fill=(100, 116, 139))
d1.text((130, 425), "📊  Doluluk & Raporlar", fill=(100, 116, 139))

# Stat Box in Sidebar
d1.rounded_rectangle([110, 510, 320, 620], radius=12, fill=(30, 27, 75, 180), outline=(99, 102, 241, 150), width=1)
d1.text((130, 530), "HAFTALIK DOLULUK", fill=(165, 180, 252))
d1.text((130, 560), "%94.8", fill=(255, 255, 255))

# Calendar Grid Right
d1.rounded_rectangle([370, 140, W-90, H-80], radius=14, fill=(11, 17, 32, 220), outline=(30, 41, 59), width=1)

# Calendar Header days
days = ["PAZARTESİ", "SALI", "ÇARŞAMBA (BUGÜN)", "PERŞEMBE"]
xs = [400, 570, 740, 930]
for d_txt, x_pos in zip(days, xs):
    col = (56, 189, 248) if "BUGÜN" in d_txt else (148, 163, 184)
    d1.text((x_pos, 165), d_txt, fill=col)

# Appointment Blocks
d1.rounded_rectangle([400, 210, 540, 320], radius=10, fill=(30, 41, 59, 200), outline=(51, 65, 85), width=1)
d1.text((415, 230), "09:30 - Dr. Kaya", fill=(226, 232, 240))
d1.text((415, 260), "Konsültasyon Seansı", fill=(148, 163, 184))

d1.rounded_rectangle([570, 280, 710, 410], radius=10, fill=(30, 41, 59, 200), outline=(51, 65, 85), width=1)
d1.text((585, 300), "11:00 - VIP Seans", fill=(226, 232, 240))
d1.text((585, 330), "Online Görüşme", fill=(148, 163, 184))

# Glowing Active Appointment
d1.rounded_rectangle([740, 220, 910, 390], radius=12, fill=(3, 105, 161, 70), outline=(6, 182, 212, 255), width=2)
d1.ellipse([760, 245, 772, 257], fill=(34, 197, 94))
d1.text((780, 242), "14:00 - Aktif Randevu", fill=(56, 189, 248))
d1.text((760, 280), "Ahmet Yılmaz", fill=(255, 255, 255))
d1.text((760, 310), "Strateji Danışmanlığı", fill=(148, 163, 184))
d1.rounded_rectangle([760, 345, 880, 375], radius=6, fill=(6, 182, 212, 40))
d1.text((780, 353), "ONAYLANDI", fill=(56, 189, 248))

d1.rounded_rectangle([930, 340, 1070, 460], radius=10, fill=(30, 41, 59, 200), outline=(51, 65, 85), width=1)
d1.text((945, 360), "16:30 - Klinik", fill=(226, 232, 240))
d1.text((945, 390), "Periyodik Kontrol", fill=(148, 163, 184))

# Integration Bar bottom
d1.rounded_rectangle([400, 560, W-120, 620], radius=10, fill=(15, 23, 42, 180), outline=(51, 65, 85), width=1)
d1.text((430, 580), "Google Calendar 2-Way Sync  •  SMS/WhatsApp Hatırlatma  •  Stripe & Iyzico Kapora  •  Çoklu Personel", fill=(148, 163, 184))

im1.save("/Users/rms/.gemini/antigravity/scratch/emtina-studio/assets/images/tacveem.png", "PNG")
print("tacveem.png created")


# 2. eBAKIM PNG
im2 = Image.new("RGBA", (W, H), (9, 9, 11, 255))
d2 = ImageDraw.Draw(im2)
create_gradient(d2, W, H, (17, 24, 39), (3, 7, 18))

for x in range(0, W, 40):
    d2.line([(x, 0), (x, H)], fill=(139, 92, 246, 12))
for y in range(0, H, 40):
    d2.line([(0, y), (W, y)], fill=(139, 92, 246, 12))

d2.rounded_rectangle([60, 50, W-60, H-50], radius=20, fill=(17, 24, 39, 230), outline=(55, 65, 81, 255), width=2)
# Top Bar
d2.rounded_rectangle([60, 50, W-60, 110], radius=20, fill=(31, 41, 55, 200))
d2.ellipse([90, 75, 104, 89], fill=(239, 68, 68))
d2.ellipse([115, 75, 129, 89], fill=(245, 158, 11))
d2.ellipse([140, 75, 154, 89], fill=(16, 185, 129))
d2.text((180, 72), "eBakım Enterprise  •  Endüstriyel Varlık & Filo Bakım Telemetrisi", fill=(167, 139, 250))

# 3 Metric Cards
d2.rounded_rectangle([90, 140, 420, 260], radius=14, fill=(31, 41, 55, 220), outline=(55, 65, 81), width=1)
d2.text((120, 165), "AKTİF MAKİNE PARKI", fill=(156, 163, 175))
d2.text((120, 195), "1,428 Ünite", fill=(255, 255, 255))
d2.text((120, 230), "↑ %99.4 Sağlık Skoru", fill=(16, 185, 129))

d2.rounded_rectangle([450, 140, 780, 260], radius=14, fill=(30, 27, 75, 220), outline=(139, 92, 246, 200), width=2)
d2.text((480, 165), "PLANLI PERİYODİK BAKIM", fill=(196, 181, 253))
d2.text((480, 195), "38 İş Emri", fill=(167, 139, 250))
d2.text((480, 230), "• Bugün 12 bakım tamamlandı", fill=(56, 189, 248))

d2.rounded_rectangle([810, 140, W-90, 260], radius=14, fill=(31, 41, 55, 220), outline=(55, 65, 81), width=1)
d2.text((840, 165), "ORTALAMA ONARIM (MTTR)", fill=(156, 163, 175))
d2.text((840, 195), "1.8 Saat", fill=(245, 158, 11))
d2.text((840, 230), "↓ -%34 Duruş Süresi", fill=(16, 185, 129))

# Telemetry List Left
d2.rounded_rectangle([90, 290, 780, H-80], radius=14, fill=(17, 24, 39, 220), outline=(55, 65, 81), width=1)
d2.text((120, 320), "Kritik Ekipman Telemetri & IoT Titreşim/Sıcaklık Durumu", fill=(243, 244, 246))

rows = [
    ("CNC Torna Ünitesi #04 (A-Blok Pres)", "OPTIMAL", (5, 150, 105), "64°C / 1.2G Titreşim"),
    ("Hidrolik Pompa Grubu B-2 (Soğutma)", "UYARI", (180, 83, 9), "82°C / Yağ Seviyesi Düşük"),
    ("Robotik Taşıma Kolu #12 (Montaj)", "OPTIMAL", (5, 150, 105), "42°C / 0.3G Titreşim"),
    ("Basınçlı Hava Kompresörü #01", "OPTIMAL", (5, 150, 105), "7.8 Bar / 55°C")
]

for idx, (title, status, badge_col, stats) in enumerate(rows):
    y = 370 + idx * 65
    d2.line([(120, y-10), (750, y-10)], fill=(55, 65, 81, 100))
    d2.text((120, y+5), title, fill=(229, 231, 235))
    d2.rounded_rectangle([520, y, 610, y+28], radius=6, fill=badge_col)
    d2.text((535, y+6), status, fill=(255, 255, 255))
    d2.text((630, y+6), stats, fill=(156, 163, 175))

# QR Code Card Right
d2.rounded_rectangle([810, 290, W-90, H-80], radius=14, fill=(24, 24, 27, 220), outline=(139, 92, 246, 150), width=1)
d2.text((840, 320), "Hızlı QR Varlık Tanıma", fill=(167, 139, 250))
d2.rounded_rectangle([890, 360, 1050, 520], radius=12, fill=(255, 255, 255))
# QR shapes
d2.rectangle([915, 385, 960, 430], fill=(0, 0, 0))
d2.rectangle([980, 385, 1025, 430], fill=(0, 0, 0))
d2.rectangle([915, 450, 960, 495], fill=(0, 0, 0))
d2.rectangle([975, 465, 1005, 495], fill=(139, 92, 246))

d2.text((835, 550), "Saha personeli mobil kamera ile anında", fill=(156, 163, 175))
d2.text((835, 575), "ekipman geçmişini ve iş emrini açar.", fill=(156, 163, 175))

im2.save("/Users/rms/.gemini/antigravity/scratch/emtina-studio/assets/images/ebakim.png", "PNG")
print("ebakim.png created")


# 3. RIVALKICK PNG
im3 = Image.new("RGBA", (W, H), (9, 9, 11, 255))
d3 = ImageDraw.Draw(im3)
create_gradient(d3, W, H, (30, 27, 75), (2, 6, 23))

# Cyber football pitch
cx, cy = W // 2, H // 2 + 30
d3.ellipse([cx - 450, cy - 240, cx + 450, cy + 240], outline=(6, 182, 212, 100), width=3)
d3.line([(cx - 480, cy), (cx + 480, cy)], fill=(6, 182, 212, 80), width=3)
d3.ellipse([cx - 100, cy - 100, cx + 100, cy + 100], outline=(6, 182, 212, 150), width=3)
d3.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(6, 182, 212, 255))

# Goals
d3.rectangle([cx - 490, cy - 130, cx - 440, cy + 130], outline=(59, 130, 246, 150), width=3)
d3.rectangle([cx + 440, cy - 130, cx + 490, cy + 130], outline=(236, 72, 153, 150), width=3)

# Top HUD
d3.rounded_rectangle([cx - 260, 50, cx + 260, 130], radius=16, fill=(3, 7, 18, 220), outline=(75, 85, 99), width=2)
d3.text((cx - 220, 75), "CYBER FC", fill=(56, 189, 248))
d3.text((cx - 30, 70), "3  :  2", fill=(255, 255, 255))
d3.text((cx + 80, 75), "NEO TOKYO", fill=(244, 63, 94))
d3.rounded_rectangle([cx - 35, 38, cx + 35, 62], radius=6, fill=(239, 68, 68))
d3.text((cx - 18, 43), "88:42", fill=(255, 255, 255))

# Godot & Ping Badges
d3.rounded_rectangle([80, 55, 260, 105], radius=10, fill=(71, 140, 191, 50), outline=(71, 140, 191), width=1)
d3.text((105, 72), "🤖 Godot 4 Engine", fill=(224, 242, 254))

d3.rounded_rectangle([W-260, 55, W-80, 105], radius=10, fill=(30, 41, 59, 180), outline=(51, 65, 85), width=1)
d3.ellipse([W-235, 78, W-223, 90], fill=(34, 197, 94))
d3.text((W-215, 72), "Ping: 18ms (P2P)", fill=(148, 163, 184))

# Player Blue Striker
d3.ellipse([cx - 180, cy - 30, cx - 110, cy + 40], fill=(2, 132, 199), outline=(56, 189, 248), width=4)
d3.text((cx - 150, cy - 10), "9", fill=(255, 255, 255))
d3.text((cx - 180, cy + 50), "ALEX (SEN)", fill=(56, 189, 248))

# Glowing Ball with trails
for i in range(15):
    tx = cx - 110 + i * 20
    ty = cy + int(math.sin(i * 0.4) * 20)
    d3.ellipse([tx-4, ty-4, tx+4, ty+4], fill=(34, 211, 238, 100))

bx, by = cx + 180, cy - 20
d3.ellipse([bx-25, by-25, bx+25, by+25], fill=(255, 255, 255), outline=(245, 158, 11), width=5)

# Opponent Defender
d3.ellipse([cx + 250, cy - 60, cx + 320, cy + 10], fill=(159, 18, 57), outline=(244, 63, 94), width=4)
d3.text((cx + 280, cy - 40), "4", fill=(255, 255, 255))
d3.text((cx + 250, cy + 20), "KAI (RAKİP)", fill=(244, 63, 94))

# Bottom HUD
d3.rounded_rectangle([cx - 250, H - 90, cx + 250, H - 40], radius=25, fill=(3, 7, 18, 220), outline=(6, 182, 212), width=2)
d3.text((cx - 190, H - 73), "SUPER KICK %100  •  60 FPS AKICI FİZİK NETCODE", fill=(248, 250, 252))

im3.save("/Users/rms/.gemini/antigravity/scratch/emtina-studio/assets/images/rivalkick.png", "PNG")
print("rivalkick.png created")


# 4. ODAK PNG
im4 = Image.new("RGBA", (W, H), (9, 9, 11, 255))
d4 = ImageDraw.Draw(im4)
create_gradient(d4, W, H, (24, 24, 27), (0, 0, 0))

# Header
d4.rounded_rectangle([60, 50, W-60, 110], radius=16, fill=(24, 24, 27, 220), outline=(39, 39, 42), width=1)
d4.text((90, 72), "O . D . A . K .   —   Cognitive Flow State & Deep Work Engine", fill=(255, 255, 255))
d4.rounded_rectangle([W-230, 65, W-90, 95], radius=15, fill=(139, 92, 246, 50), outline=(139, 92, 246), width=1)
d4.ellipse([W-210, 77, W-200, 87], fill=(168, 85, 247))
d4.text((W-190, 72), "DERİN AKIŞ", fill=(192, 132, 252))

# Central Timer Ring
fcx, fcy = 400, H // 2 + 25
radius = 160
d4.ellipse([fcx-radius, fcy-radius, fcx+radius, fcy+radius], outline=(39, 39, 42), width=12)

# Gradient arc outline simulation
for ang in range(-90, 180, 2):
    rad = math.radians(ang)
    x = fcx + radius * math.cos(rad)
    y = fcy + radius * math.sin(rad)
    d4.ellipse([x-7, y-7, x+7, y+7], fill=(6, 182, 212))

d4.text((fcx - 55, fcy - 60), "KALAN SÜRE", fill=(113, 113, 122))
d4.text((fcx - 100, fcy - 20), "37 : 45", fill=(255, 255, 255))
d4.text((fcx - 115, fcy + 55), "Alfa Frekansı (10 Hz Bimodal)", fill=(6, 182, 212))

# Right Column Cards
rc_x1, rc_x2 = 680, W - 90
d4.rounded_rectangle([rc_x1, 140, rc_x2, 280], radius=16, fill=(24, 24, 27, 220), outline=(39, 39, 42), width=1)
d4.text((rc_x1 + 30, 165), "GÜNLÜK DERİN ÇALIŞMA HEDEFİ", fill=(161, 161, 170))
d4.text((rc_x1 + 30, 200), "4s 25dk  /  5s 00dk", fill=(255, 255, 255))
d4.rounded_rectangle([rc_x1 + 30, 240, rc_x2 - 30, 252], radius=6, fill=(39, 39, 42))
d4.rounded_rectangle([rc_x1 + 30, 240, rc_x1 + 330, 252], radius=6, fill=(139, 92, 246))

d4.rounded_rectangle([rc_x1, 310, rc_x2, 450], radius=16, fill=(24, 24, 27, 220), outline=(39, 39, 42), width=1)
d4.text((rc_x1 + 30, 335), "ORTAM SES SENTEZLEYİCİ", fill=(161, 161, 170))
d4.text((rc_x1 + 30, 370), "• Yağmur & Siber Şehir Ambiyansı", fill=(56, 189, 248))
# Audio wave
for i in range(25):
    h_bar = int(math.sin(i * 0.7) * 15 + 20)
    wx = rc_x1 + 35 + i * 14
    d4.line([(wx, 425 - h_bar), (wx, 425)], fill=(139, 92, 246), width=3)

d4.rounded_rectangle([rc_x1, 480, rc_x2, 620], radius=16, fill=(24, 24, 27, 220), outline=(39, 39, 42), width=1)
d4.text((rc_x1 + 30, 505), "DİKKAT DAĞITICI BLOKER", fill=(161, 161, 170))
d4.text((rc_x1 + 30, 540), "✓  42 Web Sitesi & Bildirim Susturuldu", fill=(16, 185, 129))
d4.text((rc_x1 + 30, 575), "Dopamin koruma modu aktif (Offline PWA)", fill=(113, 113, 122))

im4.save("/Users/rms/.gemini/antigravity/scratch/emtina-studio/assets/images/odak.png", "PNG")
print("odak.png created")
