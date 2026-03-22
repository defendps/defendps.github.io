import os

def modify_html(input_filename, output_filename):
    if not os.path.exists(input_filename):
        print(f"Hata: '{input_filename}' dosyası bulunamadı!")
        return

    with open(input_filename, 'r', encoding='utf-8') as f:
        html = f.read()

    css_code = """
/* ════ EXPORT & PRINT STYLES ════ */
.export-btn { font-family: 'JetBrains Mono', monospace; font-size: .7rem; font-weight: 600; padding: 5px 12px; border-radius: 4px; cursor: pointer; background: var(--surface2); border: 1px solid var(--border2); color: var(--text1); transition: .2s; margin-left: 5px; }
.export-btn:hover { background: var(--blue-dim); color: var(--blue); border-color: var(--blue); }

@media print {
  body { background: #ffffff !important; color: #000000 !important; }
  .hdr, .nav, .search-box, .copy-btn, .pre-copy-btn, #theme-toggle, .export-btn, .search-wrap, select, .badge { display: none !important; }
  .main { padding: 0 !important; max-width: 100% !important; }
  .sec, .card-body, .tp, .sub-detail { display: block !important; opacity: 1 !important; transform: none !important; }
  .card, .sbox, .bx { page-break-inside: avoid !important; border: 1px solid #ccc !important; margin-bottom: 15px !important; box-shadow: none !important; }
  .pre, .sbox-b, .sbox-body { white-space: pre-wrap !important; word-wrap: break-word !important; background: #f8f9fa !important; color: #1f2328 !important; border: 1px solid #ddd !important; }
  .sh { border-bottom: 2px solid #000 !important; }
  a { text-decoration: none !important; color: #0969da !important; }
}
"""
    if "/* ════ EXPORT & PRINT STYLES ════ */" not in html:
        html = html.replace("</style>", css_code + "\n</style>")

    if "exportWord()" not in html:
        html = html.replace('<button id="theme-toggle"', 
                            '<button class="export-btn" onclick="window.print()">📄 PDF İndir</button>\n    <button class="export-btn" onclick="exportWord()">📝 Word İndir</button>\n    <button id="theme-toggle"')

    js_code = """
// ── EXPORT WORD ──────────────────────────────────────────────────────────
function exportWord() {
  let contentClone = document.querySelector('.main').cloneNode(true);
  contentClone.querySelectorAll('.sec, .card-body, .tp, .sub-detail').forEach(function(el) { el.style.display = 'block'; });
  contentClone.querySelectorAll('.copy-btn, .pre-copy-btn').forEach(function(el) { el.remove(); });

  let header = "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>DefendPS - Threat Intelligence</title><style>body { font-family: Arial, sans-serif; } .pre { background-color: #f4f4f4; padding: 10px; border: 1px solid #ddd; white-space: pre-wrap; } table { border-collapse: collapse; width: 100%; } th, td { border: 1px solid #aaa; padding: 5px; }</style></head><body>";
  let footer = "</body></html>";
  let sourceHTML = header + contentClone.innerHTML + footer;
  
  let blob = new Blob(['\\ufeff', sourceHTML], { type: 'application/msword' });
  let url = URL.createObjectURL(blob);
  let link = document.createElement('a');
  link.href = url;
  link.download = 'DefendPS_Threat_Intel_Report.doc';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
"""
    if "function exportWord()" not in html:
        parts = html.rsplit("</script>", 1)
        if len(parts) == 2:
            html = parts[0] + js_code + "\n</script>" + parts[1]

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"DefendPS export modülü eklendi: {output_filename}")

# ÇALIŞTIRMA BÖLÜMÜ
input_file = "index.html"  # Orijinal HTML dosyanızın adı
output_file = "DefendPS_Exportable.html"  # Üretilecek yeni dosya
modify_html(input_file, output_file)
