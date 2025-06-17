import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
from components import render_copy_button 
from text_ import BASE_PROMPT , about_text

#Initialize Session State
if 'current_prompt' not in st.session_state:
	st.session_state.current_prompt = ""
if 'suggestion_radio' not in st.session_state:
	st.session_state.suggestion_radio =None

#Page Configuration
st.set_page_config(page_title="AI Image Captioner",layout="centered")
st.title("🖼️ AI Image Captioner")
st.write("Upload an image, enter a prompt (or use a suggestion!), and generate a description.")

#Api Key Configuration
try:
	api_key=st.secrets["GEMINI_API_KEY"]
	genai.configure(api_key=api_key)
	#st.success("API Key configured successfully!",icon="✅")
except KeyError:
	st.error("ERROR: GEMINI_API_KEY not found in st.secrets. Please add it to your .streamlit/secrets.toml file.")
	st.stop()
except Exception as e:
	st.error(f"An error occurred during API config configuration: {e}")
	st.stop()

st.sidebar.header("⚙️ Configuration")

#Model Selection
available_models =[
	"gemini-1.5-pro",
	"gemini-1.5-flash",
	"gemini-1.5-flash-8b",
	"gemini-2.0-flash",
	"gemini-2.0-flash-lite"
	]

selected_model_name=st.sidebar.selectbox("Select the Gemini model:",options=available_models,index=0)

try:
	model=genai.GenerativeModel(selected_model_name)
	#st.sidebar.success(f"Using model: `{selected_model_name}`",icon="✅")
	st.success(f"Using model: `{selected_model_name}`",icon="✅")
	if'api_key' in locals() or 'api_key' in globals():
		pass
		#st.sidebar.success("API Key Configured!",icon="🔑")
except Exception as e:
	st.sidebar.error(f"Error Loading model '{selected_model_name}' : {e}")
	st.stop()




def update_prompt_from_radio():
	st.session_state.current_prompt=st.session_state.suggestion_radio

def sync_prompt_and_clear_radio():
	current_text_area_value = st.session_state.prompt_text_area_key

	st.session_state.current_prompt=current_text_area_value

	if st.session_state.suggestion_radio is not None and st.session_state.suggestion_radio!=current_text_area_value:
		st.session_state.suggestion_radio=None



#Prompt Suggestion using radio button
st.write("💡 **Prompt Suggestions:**")
prompt_suggestions =[
	"Write an Instagram caption.",
	"Describe this scene in detail.",
	"Write a short story inspired by this.",
	"Suggest 5 relevant hashtags.",
	"Identify the main objective/elements.",
	]

#Radio Buttons Widget
selected_suggestion=st.radio(
	"Select a prompt suggestion",
	options=prompt_suggestions,
	#index=None,
	horizontal=True,
	key="suggestion_radio",
	on_change=update_prompt_from_radio,
	label_visibility="collapsed"	
	)
	
#Text Area(reads from session state)
prompt_input_area= st.text_area(
	"Enter your prompt (or click a suggestion above):",
	value=st.session_state.current_prompt,
	height=100,
	key="prompt_text_area_key",  #Use this key to access value in text area(widget)
	on_change=sync_prompt_and_clear_radio
	)
uploaded_file=st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])

image_display_placeholder=st.empty()
caption_placeholder=st.empty()
output_area_placeholder=st.empty()


#Generate Button & logic
if(st.button("✨ Generate Caption")):

	user_prompt=st.session_state.prompt_text_area_key

	if uploaded_file is not None and user_prompt and user_prompt.strip():

		image_display_placeholder.empty()
		caption_placeholder.empty()
		output_area_placeholder.empty()

		image_bytes=uploaded_file.getvalue()
		image=Image.open(io.BytesIO(image_bytes))
		image_display_placeholder.image(image,caption="Your Uploaded Image",use_container_width=True)

		caption_placeholder.info("⏳ Generating caption... Please wait.")

		try:
			final_prompt=f"{BASE_PROMPT}{user_prompt}"
			response=model.generate_content([final_prompt,image])
			generated_text=response.text

			with output_area_placeholder.container():
				st.markdown("### Generated Caption:")
				st.markdown(generated_text)
				render_copy_button(generated_text) #components.py

			caption_placeholder.empty()

		except Exception as e:
			caption_placeholder.empty()
			output_area_placeholder.error(f"An error occurred: {e}")
			st.error("Failed to generate caption.")
	elif uploaded_file is None:
		st.warning("Please upload an image first.")
	else:
		st.warning("Please enter a prompt first.")	

st.sidebar.header("About")
st.sidebar.markdown(about_text,unsafe_allow_html=True)