BASE_PROMPT="""
INSTRUCTIONS:
- Analyze the provided image carefully.
- Generate a response based *only* on the user's specific request below.
- If the user asks for a description or caption, aim for concise and engaging text (e.g., 2-4 sentences) unless the user specifies a differnt length or style.
- If the user asks for multiple options or styles , clearly label each one (e.g., "Option 1:", "Option 2:").
- Include relevant emojis and hashtags if appropriate for the requested style (like an instagram caption).
- Do not add any commentary *about* the request itself, just provide the requested content.

USER REQUEST:
"""


about_text = """
This **AI Image Captioner** helps you generate creative and context-aware descriptions, 
captions, and stories for your images!

**Key Features:**
* 🖼️ **Upload Your Image:** Easily upload JPG, JPEG, or PNG files.
* ✍️ **Custom Prompts:** Write your own detailed prompts to guide the AI.
* 💡 **Prompt Suggestions:** Select from a list of predefined prompt ideas using the radio buttons.
* 🧠 **Model Selection:** Choose from various powerful Google Gemini models (in the "Configuration" section above) to tailor the generation process.
* 📋 **Copy to Clipboard:** Conveniently copy the generated text.
* ✨ **Versatile Output:** Get diverse caption styles, stories, or detailed descriptions.

**How to Use:**
1.  Upload an image using the file uploader on the main page.
2.  Select a prompt suggestion or type your own custom prompt in the text area.
3.  (Optional) Choose a different Gemini model from the "Configuration" section in this sidebar.
4.  Click the "✨ Generate Caption" button and see the magic!

**Powered By:**
* [Streamlit](https://streamlit.io/)
* Google Gemini API

---
*This app was built as a learning project. AI-generated content can sometimes be creative and surprising, but always review outputs carefully before use.*
"""