# Hacker News Scraper

This project is a simple web scraper that collects and displays the top posts from Hacker News based on upvotes. It is designed to run on both Bash and CMD, but performs better in a Bash environment.

## How It Works

1. **Scraping**: The `scrape.py` script fetches the top posts from Hacker News, along with the number of votes and URLs.
2. **Output**: The script outputs a list of posts with their titles, URLs, and vote counts.

### Running the Script

To run the script, navigate to the project directory and execute the following command:

```bash
python scrape.py
```
**Example Output**
```bash
[{'href': 'https://newatlas.com/health-wellbeing/robot-dentist-world-first/',
  'text': 'Robot dentist performs first human procedure',
  'votes': 666},
 {'href': 'https://100r.co/site/about_us.html',
  'text': 'Hundred Rabbits is a small collective exploring the failability of modern tech',
  'votes': 546},
 ...
 {'href': 'from?site=googlesource.com',
  'text': 'googlesource.com',
  'votes': 126}]
```
## Installation
1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/hacker-news.git
```
2. **Navigate to the project directory**:
```bash
cd hacker-news
```
3. **Install required packages if any (e.g., using requirements.txt)**.
   
## Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

