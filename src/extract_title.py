def extract_title(markdown):
    if markdown.startswith("# "):
        return markdown.strip("#").strip()
    else:
        raise Exception("The document does not contain a valid title")