# AI Image Captioner (Streamlit + Google Gemini API)

This is an AI-powered image captioning tool built using **Streamlit** and **Google Gemini API**.  
It allows you to generate creative, detailed, and engaging captions for your images.

This project was built during my free time in exams, exploring the Gemini API and experimenting with image captioning.

---

## Features
- **Upload Your Image** — JPG, JPEG, PNG supported
- **Custom Prompts** — Write your own or choose from suggestions
- **Prompt Suggestions** — Radio buttons with popular ideas
- **Model Selection** — Choose Gemini models like `gemini-1.5-pro`, `2.0-flash`, etc.
- **Copy to Clipboard** — Easy copying of generated captions
- **Light Theme** (custom Streamlit config)

---

## Tech Stack
- **Python**
- **Streamlit**
- **Google Generative AI API (Gemini)**
- **PIL** for image handling

---

## Installation & Run Locally

1️⃣ **Clone the Repository:**
git clone https://github.com/Awesome075/ai-image-captioner.git
cd ai-image-captioner

2️⃣ **Install Dependencies:**
pip install -r requirements.txt

3️⃣ **Add Your API Key:**
Create a file `.streamlit/secrets.toml` and add:
GEMINI_API_KEY = "your_api_key_here"

4️⃣ **Run the App:**
streamlit run image_captioner.py

---

## Example Secrets File
Example provided at:
.streamlit/secrets.example.toml

---

## Why I Built This
- To learn Python GUI development with Streamlit
- To explore Google Gemini API’s capabilities
- To build something fun in between **6th semester tiring exam breaks**

---

## Future Improvements
- Improve UI/UX with better styling
- Explore additional creative or practical use cases

---

## License
## License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
Feel free to **fork**, use, and modify with credit.
