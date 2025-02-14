# Medical Health Assistant

## Overview
Medical Health Assistant is an AI-powered chatbot that provides preliminary health guidance based on user queries. Built using Python and Streamlit, it incorporates predefined medical knowledge and leverages OpenAI’s GPT-3.5-turbo API for generating responses to health-related questions.

## Features
- **Instant Responses**: Provides predefined answers for common medical queries.
- **AI-Powered Support**: Uses OpenAI API when predefined answers are not available.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.
- **Broad Healthcare Coverage**: Offers guidance on symptoms, medications, mental health, fitness, diet, and more.

## Installation
To run the project locally, follow these steps:

### Prerequisites
- Python 3.7 or higher
- OpenAI API key

### Steps
1. Clone the repository:
   ```bash
  
   cd Medical-Health-Assistant
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run medical.py
   ```

## Usage
- Enter your health-related query in the text box.
- Click "Submit" to receive an AI-generated response.
- If a predefined response exists, it will be displayed instantly; otherwise, OpenAI API will generate an answer.

## Technologies Used
- **Python**: Backend development
- **Streamlit**: Web interface
- 
**NLTK**: Text processing
- **Transformers & TensorFlow**: AI model integration

## Future Enhancements
- **Multi-language support**
- **Integration with real-time medical databases**
- **Voice-based interaction**
- **Mobile-friendly deployment**

## Disclaimer
This chatbot is for informational purposes only and should not be used as a replacement for professional medical advice. Always consult a healthcare provider for medical concerns.

## Contributing
Contributions are welcome! Feel free to submit pull requests or report issues.

## License
This project is licensed under the MIT License.

## Contact
For questions or feedback, reach out at hariombhu01@gmail.com.

