import os
import glob

def process_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Modify Logo text and remove "台灣整復推拿"
    content = content.replace(
        'className:"text-xl font-serif font-bold text-primary",children:"盛德整復所"}),f.jsx("p",{"data-loc":"client/src/components/Navigation.tsx:35",className:"text-xs text-muted-foreground",children:"台灣整復推拿"})',
        'className:"text-4xl font-serif font-bold text-primary",children:"盛德整復所"})'
    )
    content = content.replace('children:"台灣整復推拿"', 'children:""')

    # 2. Add Google Map as an independent block in ContactPage
    # First, undo the previous map injection if it exists
    old_map_injection = 'f.jsx("iframe",{src:"https://maps.google.com/maps?q=411臺中市太平區育仁路171號&t=&z=16&ie=UTF8&iwloc=&output=embed",width:"100%",height:"250",style:{border:0, marginBottom:"1rem", borderRadius:"0.5rem"},allowFullScreen:!0,loading:"lazy"}),'
    content = content.replace(old_map_injection, '')

    # Now define the standalone map block
    # We will insert it after the grid (which ends around ContactPage.tsx:83)
    # The grid is followed by the "預約方式" div at ContactPage.tsx:91
    
    map_standalone_block = 'f.jsx("div",{className:"mb-16 rounded-lg overflow-hidden border border-border shadow-md",style:{height:"450px"},children:f.jsx("iframe",{src:"https://maps.google.com/maps?q=411臺中市太平區育仁路171號&t=&z=16&ie=UTF8&iwloc=&output=embed",width:"100%",height:"100%",style:{border:0},allowFullScreen:!0,loading:"lazy"})}),'
    
    # Target the spot right before the "預約方式" div
    target_pos_string = 'f.jsxs("div",{"data-loc":"client/src/pages/ContactPage.tsx:91"'
    if target_pos_string in content and map_standalone_block not in content:
        content = content.replace(target_pos_string, map_standalone_block + target_pos_string)

    # 3. Metadata updates
    content = content.replace('台灣整復推拿服務網站', '盛德整復所服務網站')
    content = content.replace('專業的台灣整復推拿服務', '專業的整復推拿服務')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")

def main():
    base_dir = "d:/ai/shengde-clinic"
    process_file(os.path.join(base_dir, "index.html"))
    for js_file in glob.glob(os.path.join(base_dir, "assets", "*.js")):
        process_file(js_file)

if __name__ == "__main__":
    main()
