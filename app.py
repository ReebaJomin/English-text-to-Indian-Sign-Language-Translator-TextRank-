from flask import Flask, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

df = pd.read_csv(r"C:\Users\DELL\Desktop\engtranslate\Final_dataset.csv")

file_path = os.path.join(os.getcwd(), r'C:\Users\DELL\paragraph.txt')
with open(file_path, 'r') as file:
    predefined_paragraph = file.read().strip()
#predefined_paragraph = "a dog save the life of the master from danger one can find dog everywhere in the world it also have many quality like swim in the water jumping from anywhere good smell sense dog be sometimes call canine dog be sometimes refer to a man ’ s best friend because they be kept a domestic pet and be usually loyal and like be around human the dog be so loyal to his master that nothing can induce him to leave his master his master might be a poor man or even a beggar but still the dog will not leave his master from far off dog see their master come home from work they rush to them and jump on them to show their love dog be honest friend who be always ready to die to save a friend dog always give security to the owner day and night"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_videos', methods=['POST'])
def get_videos():
    # Use predefined paragraph
    paragraph = predefined_paragraph

    # Find matching words and their corresponding URLs
    words = paragraph.split()
    video_urls = []
    for word in words:
        match = df[df['word'].str.lower() == word.lower()]
        if not match.empty:
            video_urls.append(match.iloc[0]['url'])
        else:
            continue    

    return jsonify(video_urls=video_urls)

if __name__ == '__main__':
    app.run(debug=True)