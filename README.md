# 🛍️ Smart Shopping Optimizer

A web-based shopping assistant that helps users find the cheapest combination of products across multiple online stores while staying within their budget. Built with Flask and optimization algorithms to deliver the best shopping deals.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Multi-Store Price Comparison**: Automatically searches and compares prices across different e-commerce platforms
- **Budget Optimization**: Uses linear programming (PuLP) to find the most cost-effective product combinations
- **Flexible Selection**: Option to allow partial selections when some items are unavailable
- **Modern UI**: Beautiful, responsive interface with gradient designs and calligraphy fonts
- **Real-time Results**: Displays optimized shopping cart with direct product links
- **Smart Algorithm**: Minimizes total cost while respecting budget constraints

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher installed
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/devthejas/Smart_Shopping_Optimizer.git
cd Smart_Shopping_Optimizer
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## 🏃 Usage

1. Start the Flask server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

3. Enter your shopping items (comma-separated):

```
rice, sugar, pizza
```

4. (Optional) Set a maximum budget in rupees

5. Click **"Find Cheapest Links"** to get optimized results

## 📁 Project Structure

```
smart-shopping-optimizer/
│
├── app.py                 # Main Flask application
├── amazon_scraper.py      # Web scraping logic for product data
├── index.html             # Frontend HTML template
├── style.css              # Styling (optional external CSS)
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Data Processing**: Pandas (data manipulation)
- **Web Scraping**: BeautifulSoup4, Requests, lxml
- **Optimization**: PuLP (linear programming)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Fonts**: Google Fonts (Pacifico, Quicksand)

## 📦 Dependencies

```
Flask
pandas
requests
beautifulsoup4
pulp
lxml
```

## 🔧 Configuration

Currently, the scraper uses placeholder data. To enable real-time scraping:

1. Open `amazon_scraper.py`
2. Implement actual scraping logic using BeautifulSoup
3. Add API keys if using e-commerce APIs
4. Configure rate limiting to avoid getting blocked

**Note**: Web scraping should comply with the website's terms of service and robots.txt policies.

## 🎨 Customization

### Changing Fonts

Edit the Google Fonts link in `index.html`:

```html
<link
  href="https://fonts.googleapis.com/css2?family=YourFont&display=swap"
  rel="stylesheet"
/>
```

### Adjusting Colors

Modify the gradient colors in the CSS:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Adding More Stores

Extend `amazon_scraper.py` with additional scraper functions for other e-commerce platforms.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues

- Scraper currently returns placeholder data
- Limited to single currency (₹ INR)
- No user authentication or saved preferences

## 🔮 Future Enhancements

- [ ] Real-time web scraping implementation
- [ ] Support for multiple currencies
- [ ] User accounts and shopping history
- [ ] Price tracking and alerts
- [ ] Mobile app version
- [ ] Integration with more e-commerce platforms
- [ ] Product review aggregation
- [ ] Chrome extension for quick comparisons

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**

- Portfolio: [yourwebsite.com](https://yourwebsite.com)
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Flask documentation for excellent guides
- PuLP library for optimization algorithms
- Google Fonts for beautiful typography
- The open-source community for inspiration

## 📧 Contact

For questions or feedback, please reach out:

- Email: thejas.ks@lead.ac.in
- Create an issue in this repository

---

⭐ If you found this project helpful, please give it a star!

Made with ❤️ by [devthejas]
