import requests

def get_first_char(text):
    return text[0] if text else None

def fetch_poem():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get('https://ganjgah.ir/api/ganjoor/poem/random', headers=headers)
        response.raise_for_status()
        poem_data = response.json()
        response1 = requests.get(f'https://ganjgah.ir/api/ganjoor/poem/{poem_data['id']}', headers=headers)
        poet = response1.json()
        return poem_data['plainText'].splitlines() , poet['category']['poet']['name']
    except requests.RequestException as e:
        print(f"خطای API: {e}")
        return None

def find_couplet_by_first_char(poem_lines, target_char):
    for i in range(0, len(poem_lines), 2):
        couplet = poem_lines[i:i + 2]
        if couplet and couplet[0][0] == target_char:
            return "\n".join(couplet)
    return None

def main():
    target_char = input("یک حرف وارد کنید: ").strip()
    if not target_char or len(target_char) != 1:
        print("لطفاً فقط یک حرف وارد کنید.")
        return

    while True:
        print("در حال جستجو...")
        poem_lines , poet = fetch_poem()
        if poem_lines is None:
            print("عدم دسترسی به API. دوباره سعی می‌کنیم...")
            continue

        result = find_couplet_by_first_char(poem_lines, target_char)
        if result:
            print("نتیجه:")
            print(result, '\n', poet)
            break
        else:
            print("دو سطر مورد نظر پیدا نشد. دوباره سعی می‌کنیم...")

if __name__ == "__main__":
    main()