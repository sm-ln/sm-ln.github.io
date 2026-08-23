from scholarly import scholarly

# 替换为你自己的 Google Scholar ID (在你的谷歌学术主页 URL 中的 user= 后面的字符串)
SCHOLAR_ID = '439H860AAAAJ&hl'

def fetch_publications():
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=['publications'])
    
    bib_content = ""
    for pub in author['publications']:
        scholarly.fill(pub)
        if 'bibtex' in pub:
            # 加上 al-folio 常用的展开按钮属性
            bibtex_entry = pub['bibtex'].replace('}\n}', ',\n  bibtex_show={true}\n}')
            bib_content += bibtex_entry + "\n\n"
            
    with open('_bibliography/papers.bib', 'w', encoding='utf-8') as f:
        f.write(bib_content)

if __name__ == '__main__':
    fetch_publications()
