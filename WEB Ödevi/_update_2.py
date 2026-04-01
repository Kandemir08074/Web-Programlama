import sys

try:
    with open(r'c:\Users\Mert\OneDrive\Desktop\WEB Ödevi\ödev.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Smooth scroll
    if 'scroll-behavior: smooth;' not in html:
        html = html.replace('    <style>\n', '    <style>\n        html {\n            scroll-behavior: smooth;\n            scroll-padding-top: 100px;\n        }\n')

    # 2. Add ID anchors
    html = html.replace('<!-- Product 1 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3">', '<!-- Product 1 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3" id="gitarlar">')
    html = html.replace('<!-- Product 2 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3">', '<!-- Product 2 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3" id="piyanolar">')
    html = html.replace('<!-- Product 3 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3">', '<!-- Product 3 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3" id="davul">')
    html = html.replace('<!-- Product 7 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3">', '<!-- Product 7 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3" id="studyo">')
    html = html.replace('<!-- Product 8 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3">', '<!-- Product 8 -->\n            <div class="col-12 col-sm-6 col-md-4 col-lg-3" id="aksesuar">')

    # 3. Update Navbar Links HTML
    nav_old = """                <ul class="navbar-nav mx-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="#">Gitarlar</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Piyanolar & Tuşlular</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Davul & Perküsyon</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Stüdyo & Kayıt</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Aksesuarlar</a>
                    </li>
                </ul>"""
    nav_new = """                <ul class="navbar-nav mx-auto">
                    <li class="nav-item">
                        <a class="nav-link active" href="#gitarlar" onclick="document.querySelectorAll('.nav-link').forEach(l=>l.classList.remove('active'));this.classList.add('active');">Gitarlar</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#piyanolar" onclick="document.querySelectorAll('.nav-link').forEach(l=>l.classList.remove('active'));this.classList.add('active');">Piyanolar & Tuşlular</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#davul" onclick="document.querySelectorAll('.nav-link').forEach(l=>l.classList.remove('active'));this.classList.add('active');">Davul & Perküsyon</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#studyo" onclick="document.querySelectorAll('.nav-link').forEach(l=>l.classList.remove('active'));this.classList.add('active');">Stüdyo & Kayıt</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#aksesuar" onclick="document.querySelectorAll('.nav-link').forEach(l=>l.classList.remove('active'));this.classList.add('active');">Aksesuarlar</a>
                    </li>
                </ul>"""
    html = html.replace(nav_old, nav_new)

    # 4. Update Modal Icons
    icons_old = """                <div class="d-flex align-items-center">
                    <i class="bi bi-search nav-icon"></i>
                    <i class="bi bi-person nav-icon"></i>
                    <i class="bi bi-cart3 nav-icon"></i>
                </div>"""
    icons_new = """                <div class="d-flex align-items-center">
                    <i class="bi bi-search nav-icon" data-bs-toggle="modal" data-bs-target="#comingSoonModal"></i>
                    <i class="bi bi-person nav-icon" data-bs-toggle="modal" data-bs-target="#comingSoonModal"></i>
                    <i class="bi bi-cart3 nav-icon" data-bs-toggle="modal" data-bs-target="#comingSoonModal"></i>
                </div>"""
    html = html.replace(icons_old, icons_new)

    # 5. Navbar CSS Links with border bottom
    css_nav_old = """
        .nav-link {
            font-weight: 500;
            color: #dddddd !important;
            text-transform: uppercase;
            font-size: 0.85rem;
            padding: 0.5rem 1rem !important;
            letter-spacing: 1px;
            transition: color 0.3s ease;
        }

        .nav-link:hover,
        .nav-link.active {
            color: var(--primary-orange) !important;
            text-shadow: 0 0 8px rgba(0, 255, 136, 0.4);
        }"""
            
    css_nav_new = """
        .nav-link {
            font-weight: 500;
            color: #dddddd !important;
            text-transform: uppercase;
            font-size: 0.85rem;
            padding: 0.5rem 1rem !important;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            position: relative;
        }

        .nav-link::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: 0;
            left: 50%;
            background-color: var(--primary-orange);
            transition: all 0.3s ease;
            transform: translateX(-50%);
        }

        .nav-link:hover::after,
        .nav-link.active::after {
            width: 60%;
        }

        .nav-link:hover,
        .nav-link.active {
            color: var(--primary-orange) !important;
            text-shadow: 0 0 8px rgba(0, 255, 136, 0.4);
        }"""
    html = html.replace(css_nav_old, css_nav_new)

    # 6. Add Coming Soon Modal at the end inside body
    modal_html = """
    <!-- Coming Soon Modal -->
    <div class="modal fade" id="comingSoonModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content rounded-0 border-0" style="background-color: var(--bg-color);">
                <div class="modal-header border-bottom border-secondary" style="border-color: rgba(255,255,255,0.1) !important;">
                    <h5 class="modal-title fw-bold" style="color: var(--primary-orange);"><i class="bi bi-stars me-2"></i>BİLGİLENDİRME</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" style="filter: invert(1) grayscale(100%) brightness(200%);"></button>
                </div>
                <div class="modal-body p-5 text-center text-light">
                    <i class="bi bi-tools" style="font-size: 4rem; color: var(--primary-orange); margin-bottom: 20px; display: inline-block;"></i>
                    <h4 class="fw-bold text-white mb-3">Bu özellik yakında MIFA'da!</h4>
                    <p class="text-white-50 mb-0" style="font-size: 0.95rem; line-height: 1.6;">Harika bir deneyim sunabilmek için altyapı güncellemelerimiz devam ediyor. Bizi takip etmeye devam edin.</p>
                </div>
            </div>
        </div>
    </div>
"""
    if 'id="comingSoonModal"' not in html:
        html = html.replace('</body>', f'{modal_html}\n</body>')

    with open(r'c:\Users\Mert\OneDrive\Desktop\WEB Ödevi\ödev.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print("Success")
except Exception as e:
    print(f"Error: {e}")
