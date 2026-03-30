import os
import glob

def process_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Modify Logo text and remove "台灣整復推拿"
    # Old: f.jsx("h1",{"data-loc":"client/src/components/Navigation.tsx:34",className:"text-xl font-serif font-bold text-primary",children:"盛德整復所"}),f.jsx("p",{"data-loc":"client/src/components/Navigation.tsx:35",className:"text-xs text-muted-foreground",children:"台灣整復推拿"})
    # New: f.jsx("h1",{"data-loc":"client/src/components/Navigation.tsx:34",className:"text-3xl font-serif font-bold text-primary",children:"盛德整復所"})
    content = content.replace(
        'className:"text-xl font-serif font-bold text-primary",children:"盛德整復所"}),f.jsx("p",{"data-loc":"client/src/components/Navigation.tsx:35",className:"text-xs text-muted-foreground",children:"台灣整復推拿"})',
        'className:"text-4xl font-serif font-bold text-primary",children:"盛德整復所"})'
    )
    
    # Also if Navigation.tsx has just "台灣整復推拿" elsewhere:
    content = content.replace('children:"台灣整復推拿"', 'children:""')

    # Also increase size of the "盛" icon if needed, but text-4xl is good for title.

    # 2. Add Google Map above the address in ContactPage
    # Old: children:[f.jsx("h3",{"data-loc":"client/src/pages/ContactPage.tsx:32",className:"text-lg font-semibold text-primary mb-2",children:"地址"}),f.jsx("p",{"data-loc":"client/src/pages/ContactPage.tsx:33",className:"text-base text-foreground",children:"411臺中市太平區育仁路171號"})]
    # New: Add iframe
    old_contact_address = 'children:[f.jsx("h3",{"data-loc":"client/src/pages/ContactPage.tsx:32",className:"text-lg font-semibold text-primary mb-2",children:"地址"}),f.jsx("p",{"data-loc":"client/src/pages/ContactPage.tsx:33",className:"text-base text-foreground",children:"411臺中市太平區育仁路171號"})]'
    new_contact_address = 'children:[f.jsx("h3",{"data-loc":"client/src/pages/ContactPage.tsx:32",className:"text-lg font-semibold text-primary mb-2",children:"地址"}),f.jsx("iframe",{src:"https://maps.google.com/maps?q=411臺中市太平區育仁路171號&t=&z=16&ie=UTF8&iwloc=&output=embed",width:"100%",height:"250",style:{border:0, marginBottom:"1rem", borderRadius:"0.5rem"},allowFullScreen:!0,loading:"lazy"}),f.jsx("p",{"data-loc":"client/src/pages/ContactPage.tsx:33",className:"text-base text-foreground",children:"411臺中市太平區育仁路171號"})]'
    
    content = content.replace(old_contact_address, new_contact_address)
    
    # 3. Change the metadata properties in index.html, if it's there
    content = content.replace('台灣整復推拿服務網站', '盛德整復所服務網站')
    content = content.replace('專業的台灣整復推拿服務', '專業的整復推拿服務')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")

def main():
    base_dir = "d:/ai/shengde-clinic"
    # process index.html
    process_file(os.path.join(base_dir, "index.html"))
    # process assets/*.js
    for js_file in glob.glob(os.path.join(base_dir, "assets", "*.js")):
        process_file(js_file)

if __name__ == "__main__":
    main()
