from sklearn.feature_extraction.text import CountVectorizer

def analyze_logs(file_path="cleaned_output.txt"):
    with open(file_path, "r") as file:
        data = file.read()

    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform([data])
    keywords = vectorizer.get_feature_names_out()

    print("\n🔍 Top keywords:")
    print(", ".join(keywords))

if __name__ == "__main__":
    analyze_logs()
