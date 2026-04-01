import re
import os

file_path = r"c:\Users\Mert\OneDrive\Desktop\WEB Ödevi\ödev.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add data-bs-target and cursor:pointer to product cards
modal_counter = 1
def replace_product_card(match):
    global modal_counter
    # The match groups:
    # 1: before class
    # 2: class="product-card d-flex flex-column"
    # 3: inner content up to <img
    # 4: src attribute
    # 5: rest of the file
    
    # Actually, let's just do a simple replacement for the opening tag
    res = f'<div class="product-card d-flex flex-column" data-bs-toggle="modal" data-bs-target="#productModal{modal_counter}" style="cursor: pointer;">'
    modal_counter += 1
    return res

content = re.sub(r'<div class="product-card d-flex flex-column">', replace_product_card, content)

# 2. Extract product details to generate modals
# We need to find all products and their images, titles, categories, prices
# A regex to capture these:
product_regex = r'<div class="product-card d-flex flex-column".*?>.*?<img src="(.*?)".*?alt="(.*?)".*?<div class="product-category">(.*?)</div>.*?<a href="#" class="product-title">(.*?)</a>.*?<div class="product-price mt-auto">(.*?)</div>'

products = re.findall(product_regex, content, re.DOTALL)

descriptions = [
    "Fender'in efsanevi Stratocaster modeli. Alder gövde, akçaağaç (maple) sap ve 3 adet single-coil manyetik ile parlak ve net bir ton sunar. Sahne ve stüdyo için mükemmel seçim.",
    "Roland'ın üstün kalitesini sunan V-Drums seti. Hassas mesh head trampet ve gelişmiş zil padleriyle gerçek davul hissini dijital ortamda yaşatır.",
    "Tama'nın 50. yılına özel üretilmiş sınırlı üretim akustik davul seti. Akçaağaç gövdesi sayesinde sıcak ve dengeli bir tona sahiptir.",
    "Gitar dünyasının ikonik modeli Gibson Dove. AAA kalite ladin kapak ve akçaağaç yanlar. Muazzam bir rezonans ve özel işlemeli pickguard sunar.",
    "80'lerin agresif rock ve metal tonlarını arayanlar için tasarlandı. Aktif EMG manyetikler ve ikonik Explorer kasa tasarımı.",
    "Modern basçılar için tasarlanmış, ergonomik ve hafif gövdeli profesyonel bas gitar. Güçlü aktif manyetik sistemiyle vurucu tonlar.",
    "Marshall'ın lambalı kafa amfisi. 4 kanallı yapısı, her kanal için ayrı mod seçeneğiyle yüzlerce farklı analog ton kombinasyonu sunar.",
    "DW kalitesini sunan çift zincirli (double chain) twin pedal. Pürüzsüz hissiyatı ve sağlam yapısıyla yüksek tempolu tarzlara uygundur."
]

modals_html = ""
for i, product in enumerate(products):
    img_src = product[0]
    category = product[2].strip()
    title = product[3].strip()
    price_html = product[4].strip()
    desc = descriptions[i] if i < len(descriptions) else "Harika bir enstrüman."
    
    modal = f"""
    <!-- Modal {i+1} -->
    <div class="modal fade" id="productModal{i+1}" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content rounded-0 border-0">
                <div class="modal-header border-0 pb-0">
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body p-4 pt-0">
                    <div class="row align-items-center">
                        <div class="col-md-5 mb-4 mb-md-0 text-center bg-light p-3" style="min-height: 300px; display: flex; align-items: center; justify-content: center;">
                            <img src="{img_src}" class="img-fluid" alt="{title}" style="max-height: 300px; object-fit: contain;">
                        </div>
                        <div class="col-md-7 ps-md-4">
                            <h6 class="text-uppercase" style="color: var(--primary-orange); font-weight: 700; font-size: 0.85rem; letter-spacing: 1px;">{category}</h6>
                            <h3 class="mb-3 fw-bold" style="color: var(--dark-gray);">{title}</h3>
                            <p class="text-muted mb-4" style="line-height: 1.7; font-size: 0.95rem;">{desc}</p>
                            <h4 class="mb-4 fw-bold" style="color: var(--primary-orange); font-size: 1.8rem;">{price_html}</h4>
                            <div class="d-grid gap-2 d-md-block">
                                <button class="btn btn-custom btn-modal-cart w-100 py-3 text-uppercase fw-bold" style="letter-spacing: 1px; font-size: 1rem;">
                                    <i class="bi bi-cart-plus me-2"></i>Sepete Ekle
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    modals_html += modal

# Insert modals before <footer>
content = content.replace("<footer>", modals_html + "\n    <footer>")

# Add JS alert script before </body>
script_html = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Prevent the default cart button from doing anything else if clicked inside standard card
            const cardCartButtons = document.querySelectorAll('.product-card .btn-cart');
            cardCartButtons.forEach(btn => {
                btn.addEventListener('click', function(e) {
                    // Let the modal open since the card has data-bs-toggle over it
                    // But prevent default link behavior if any
                    e.preventDefault();
                });
            });

            // Alerts for modal 'Sepete Ekle' buttons
            const modalCartButtons = document.querySelectorAll('.btn-modal-cart');
            modalCartButtons.forEach(btn => {
                btn.addEventListener('click', function() {
                    alert('Ürün sepetinize eklendi!');
                });
            });
        });
    </script>
"""

content = content.replace("</body>", script_html + "</body>")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Modals and JavaScript added successfully. Processed {len(products)} products.")
