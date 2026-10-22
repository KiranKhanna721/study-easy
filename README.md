# Study Easy

An NLP study helper that uses models from the **Modzy** model marketplace to analyse and understand text.

## Features

- **Language detection and translation:** detects the input language and translates it to English
- **Text topic modelling:** pulls the key topics out of a passage
- **Sentiment analysis**
- **Named entity recognition**
- **Text summarisation**

There are two front ends:

| Version | Location | Run with |
|---------|----------|----------|
| Flask | `app.py`, `forms.py`, `templates/` | `python app.py` |
| Streamlit | `modyz-streamlit/` | `streamlit run modyz-streamlit/app.py` |

## Configuration

Set your Modzy API URL and key as environment variables. `config.py` reads them:

```bash
export API_URL="https://app.modzy.com/api"
export API_KEY="your-modzy-api-key"
```

## Getting started

```bash
pip install -r requirements.txt
python app.py
```

## License

See [LICENSE](LICENSE).
