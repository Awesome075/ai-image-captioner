import streamlit as st
import uuid
import json

def render_copy_button(text_to_copy: str , button_label:str = "Copy Caption",height: int =50):

	if not isinstance(text_to_copy,str) or not text_to_copy.strip():
		return

	try:
		escaped_text=json.dumps(text_to_copy)[1:-1]
	except Exception as e:
		st.error(f"Error preparing text for copy button: {e}")
		return


	button_id = f"copy_btn_{uuid.uuid4()}"

	html_code= f"""
		<style>
			.copy-btn{{
				display.inline-block;
				padding: 0.25rem 0.75 rem;
				background-color: #007bff;
				color:white;
				border: none;
				border-radius: 0.25rem;
				text-align: center;
				text-decoration: none;
				font-size: 0.9rem;
				cursor: pointer;
				margin-top: 5px;
			}}
			.copy-btn:hover{{background-color: #0056b3;}}
			.copy-btn:active{{background-color: #004085;}}
		</style>
		<button id="{button_id}" class="copy-btn" onclick="copyToClipboard()">
			{button_label}
		</button>
		<script>
		async function copyToClipboard(){{
			const textToCopy =`{escaped_text}`;
			try{{
				await navigator.clipboard.writeText(textToCopy);
				const button = document.getElementById("{button_id}");
				const originalText ='Copied!';
				setTimeout(()=> {{button.innerText = originalText;}},1500);

			}} catch(err){{
				console.error('Failed To Copy: ',err);
				alert('Failed to copy text.')
			}}
		}}
		</script>
		"""

	st.components.v1.html(html_code,height=height)