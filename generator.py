import os
import shutil
import markdown

# Dosya ve dizin yolları
PAGES_LIST = "pages.list"
PAGES_DIR = "pages"
OUTPUT_DIR = "pages-html"
STYLE_PATH = "style.css"
INDEX_OUTPUT = "index.html"  # index.html, ana dizine oluşturulacak

# HTML şablonları
PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Mesflit</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>{title}</h1>
    </header>
    <main>
        {content}
    </main>
    <footer>
        <a href="../index.html">Mesflit'in Bloğu</a>
    </footer>
</body>
</html>
"""

INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mesflit'in Bloğu - Ana Sayfa</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Mesflit'in Bloğu</h1>
        <p>Keşfedebileceğiniz Herşey.</p>
    </header>
    <main>
        <ul>
            {links}
        </ul>
    </main>
    <footer>
        <p>&copy; 2025 Mesflit. Tüm hakları saklıdır.</p>
    </footer>
</body>
</html>
"""

def read_pages_list():
    """pages.list dosyasını oku ve dosya-başlık çiftlerini döndür."""
    with open(PAGES_LIST, "r", encoding="utf-8") as f:
        return [line.strip().split("|") for line in f.readlines() if line.strip()]

def markdown_to_html(md_path):
    """Markdown dosyasını HTML'ye dönüştür."""
    with open(md_path, "r", encoding="utf-8") as f:
        return markdown.markdown(f.read())

def generate_page(title, content):
    """HTML sayfası üret."""
    return PAGE_TEMPLATE.format(title=title, content=content)

def generate_index(links):
    """Ana sayfa için HTML üret."""
    return INDEX_TEMPLATE.format(links="\n".join(links))

def clean_output_directory():
    """Eski dosyaları sil ve çıkış dizinini sıfırla."""
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)  # Mevcut klasörü sil
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # Boş klasörü oluştur

def build_site():
    """Tüm siteyi oluştur."""
    clean_output_directory()  # Çıkış klasörünü sıfırla
    pages = read_pages_list()

    # Tüm sayfaları oluştur
    links = []
    for md_file, title in pages:
        md_path = os.path.join(PAGES_DIR, md_file)
        if not os.path.exists(md_path):
            print(f"Hata: {md_path} bulunamadı.")
            continue

        # Markdown'dan HTML'ye dönüştür
        html_content = markdown_to_html(md_path)
        page_html = generate_page(title, html_content)
        
        # Sayfayı kaydet
        output_file = os.path.join(OUTPUT_DIR, f"{os.path.splitext(md_file)[0]}.html")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(page_html)

        # Ana sayfa için bağlantı ekle
        links.append(f'<li><a href="pages-html/{os.path.splitext(md_file)[0]}.html">{title}</a></li>')

    # index.html oluştur
    index_html = generate_index(links)
    with open(INDEX_OUTPUT, "w", encoding="utf-8") as f:
        f.write(index_html)

    # style.css'i kopyala
    if os.path.exists(STYLE_PATH):
        shutil.copy(STYLE_PATH, OUTPUT_DIR)

if __name__ == "__main__":
    build_site()
