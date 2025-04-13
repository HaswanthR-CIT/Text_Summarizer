# Text Summarizer

![Text Summarizer UI](https://via.placeholder.com/800x400.png?text=Text+Summarizer+UI)  
*A sleek and modern interface for summarizing text with interactive topic tags.*

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Project Overview
The **Text Summarizer** is a web application designed to generate concise summaries of input text and extract key topics for quick insights. Built as a showcase project for a software engineering internship at Senthuron Tech, it combines natural language processing (NLP) with an elegant, colorful, and user-friendly interface. Users can input text, select a summary length (short, medium, or long), and explore highlighted topics interactively, making it ideal for processing articles, essays, or reports efficiently.

The application leverages the `facebook/bart-large-cnn` model for summarization and NLTK for topic extraction, wrapped in a Flask backend. The frontend features a responsive design with Tailwind CSS, custom styles, and JavaScript animations, ensuring a professional yet catchy user experience.

## Features
- **Text Summarization**: Generate summaries in three lengths:
  - Short: 1–2 sentences (~30 words)
  - Medium: 2–3 sentences (~50 words)
  - Long: 3–4 sentences (~80 words)
- **Topic Extraction**: Automatically identify up to five key topics (keywords) from the input text using NLTK.
- **Interactive Tags**: Clickable topic tags that highlight corresponding words in the original text with a smooth animation.
- **Responsive UI**: Clean, elegant design with mint, teal, coral, and violet accents, optimized for mobile, tablet, and desktop.
- **Input Validation**: Ensures at least 30 words for meaningful summaries, with clear error messages.
- **Professional Styling**: Subtle gradients, modern typography (Inter), and hover effects for a polished look.
- **Debug Logging**: Backend logs for summary generation and topic extraction to aid development.

## Technologies Used
- **Backend**:
  - Python 3.8+: Core language
  - Flask 2.0+: Web framework
  - Transformers 4.30+: `facebook/bart-large-cnn` for summarization
  - NLTK 3.8+: Topic extraction and text processing
- **Frontend**:
  - HTML5: Structure
  - Tailwind CSS 3.3+: Responsive styling
  - CSS3: Custom animations and gradients
  - JavaScript: Interactive tag highlighting
- **Development Tools**:
  - VSCode: IDE
  - Git: Version control
  - GitHub: Repository hosting
  - Virtualenv: Dependency management
- **Dependencies**:
  - See `requirements.txt` for full list (e.g., `torch`, `numpy`)

## Installation
Follow these steps to set up the project locally on a Windows, macOS, or Linux machine.

### Prerequisites
- Python 3.8 or higher ([Download](https://www.python.org/downloads/))
- Git ([Download](https://git-scm.com/downloads/))
- A modern web browser (Chrome, Firefox, Edge)
- Optional: VSCode for editing ([Download](https://code.visualstudio.com/))

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/text-summarizer.git
   cd text-summarizer
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   ```
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: If `nltk` prompts for resources, the app auto-downloads `punkt` and `stopwords`.

4. **Verify Setup**
   Ensure `app.py`, `templates/index.html`, `static/style.css`, and `static/script.js` are in the project root.

5. **Run the Application**
   ```bash
   python app.py
   ```
   - The app will start at `http://127.0.0.1:5000`.
   - Expect console output:
     ```
     Loading the summarization model...
     Model loaded successfully!
      * Running on http://127.0.0.1:5000
     ```

6. **Access the App**
   Open a browser and navigate to `http://127.0.0.1:5000`.

### Troubleshooting
- **ModuleNotFoundError**: Run `pip install flask transformers nltk torch`.
- **Model Loading Slow**: Ensure a stable internet connection for the first run (downloads `bart-large-cnn`).
- **Port Conflict**: Change the port in `app.py` (e.g., `app.run(debug=True, port=5001)`).
- **NLTK Errors**: Manually download resources:
  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  ```

## Usage
1. **Open the App**
   Visit `http://127.0.0.1:5000` after starting the server.

2. **Enter Text**
   - Paste or type text (at least 30 words) into the textarea.
   - Example:
     ```
     Artificial intelligence is reshaping the world by enabling machines to perform tasks that once required human intelligence. Machine learning, a subset of AI, allows systems to learn from vast datasets...
     ```

3. **Choose Summary Length**
   - Select `Short`, `Medium`, or `Long` from the dropdown.

4. **Generate Summary**
   - Click the teal “Generate Summary” button.
   - Output includes:
     - **Summary**: Concise text based on length choice.
     - **Topics**: Clickable tags (e.g., `ai`, `privacy`) with teal-to-violet gradients.
     - **Original Text**: Input text with highlightable words.

5. **Interact with Topics**
   - Click a tag to highlight matching words in the original text (yellow-coral gradient).
   - Tags pulse subtly on click for visual feedback.

6. **Test Cases**
   - **Short Input**: Enter <30 words to see a coral error message.
   - **VR Text**: Try a paragraph about virtual reality to check topic variety (e.g., `vr`, `headsets`).
   - **Responsive Design**: Resize the browser or use a phone to verify layout.

## Project Structure
```
text-summarizer/
├── app.py                    # Flask backend with summarization and topic logic
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html            # Frontend layout with Tailwind and Jinja2
├── static/
│   ├── style.css             # Custom styles (colors, animations)
│   └── script.js             # JavaScript for tag interactions
├── venv/                     # Virtual environment (not tracked)
├── .gitignore                # Ignores venv, __pycache__, etc.
└── README.md                 # This file
```

## How It Works
### Backend (`app.py`)
- **Summarization**:
  - Uses `facebook/bart-large-cnn` from Hugging Face’s Transformers.
  - Parameters adjust length: `max_length` (30/50/80), `min_length` (10/20/30).
  - Trims summaries to complete sentences (2/3/4 max).
- **Topic Extraction**:
  - NLTK tokenizes text, removes stopwords, and picks top 5 words by frequency.
  - Example: “AI is transforming...” → `['ai', 'machine', 'privacy', ...]`.
- **Routing**:
  - `GET /`: Renders `index.html`.
  - `POST /`: Processes text, generates summary/topics, and passes to template.

### Frontend (`index.html`, `style.css`, `script.js`)
- **Layout**:
  - Mint background, white container with coral shadow.
  - Violet headings, teal button, gradient tags (teal-to-violet).
  - Responsive via Tailwind (stacks on mobile).
- **Styling**:
  - Inter font for clarity.
  - Colors: Mint (#ecfdf5), Violet (#6b21a8), Teal (#0d9488), Coral (#f87171).
  - Subtle animations: Button hover, tag lift, error fade.
- **Interactivity**:
  - JavaScript highlights words on tag click with a pulse effect.
  - Highlights use yellow-coral gradient for warmth.

### Workflow
1. User submits text and length choice.
2. Backend validates input (≥30 words).
3. Summarizer generates output, trimmed to full sentences.
4. NLTK extracts topics.
5. Frontend displays summary, tags, and text.
6. Clicking tags highlights words dynamically.

## Future Improvements
- **Advanced Summarization**: Fine-tune the model for domain-specific texts (e.g., legal, medical).
- **Topic Enhancements**: Use TF-IDF or spaCy for better keyword relevance.
- **Export Options**: Add buttons to download summaries as PDF or TXT.
- **Multilingual Support**: Integrate models like mBART for non-English texts.
- **Accessibility**: Improve ARIA labels and keyboard navigation.
- **Analytics**: Track popular topics or summary lengths for user insights.
- **UI Tweaks**: Add dark mode or customizable color themes.
- **Performance**: Cache model outputs for faster responses.

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m "Add your feature"`.
4. Push: `git push origin feature/your-feature`.
5. Open a pull request with a clear description.

Please adhere to:
- Code style: PEP 8 for Python, Prettier for HTML/CSS/JS.
- Tests: Add unit tests for new features (use `pytest`).
- Issues: Report bugs or suggest ideas via GitHub Issues.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements
- **Hugging Face**: For the `facebook/bart-large-cnn` model.
- **NLTK Team**: For robust NLP tools.
- **Tailwind CSS**: For responsive styling.
- **Senthuron Tech**: For inspiring this internship project.
- **Community**: For open-source libraries and tutorials.

