import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Emtina Studio | Fikirleri deneyime dönüştürüyoruz',
  description: 'Emtina Studio; oyun, girişim, web, yazılım ve dijital büyüme çalışmalarını tek çatı altında birleştirir.',
  openGraph: {
    title: 'Emtina Studio',
    description: 'Oyun, girişim, web, yazılım ve dijital büyüme için tek üretim çatısı.',
    images: ['/og.png'],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="tr">
      <body>{children}</body>
    </html>
  );
}
