# Persian Poetry Search Tool

## Description
This Python script retrieves random Persian poems using the **Ganjgah API** and searches for a couplet that starts with a given letter. It repeatedly fetches new poems until it finds a match. The tool is useful for Persian poetry enthusiasts and can also be adapted for **"مشاعره"** (Persian poetry game).

## Features
- Fetches random Persian poems.
- Searches for a couplet that begins with the user-specified letter.
- Displays the found couplet along with the poet's name.
- Handles API request errors gracefully.

## Installation
To use this script, ensure you have Python installed and install the required package:
```sh
pip install requests
```

## Usage
Run the script and enter a Persian letter to search for:
```sh
python script.py
```
Then, input a single Persian letter when prompted:
```sh
یک حرف وارد کنید: ش
```
The script will fetch and display a matching couplet if found:
```
نتیجه:
شب است و شاهد و شمع و شراب و شیرینی
غم است و سوز دل و اشک و اضطراب و حنین
حافظ
```

## Dependencies
- Python 3+
- `requests` library

## Notes
- The script continuously fetches new poems until it finds a match.
- The API responses might change over time, so ensure the API endpoints are active.
- If the API is unreachable, the script retries automatically.

## License
This project is open-source and available under the MIT License.

