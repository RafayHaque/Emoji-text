from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

shapes_mapping = {
    'A': ["   🔳     ", " 🔳  🔳   ", "🔳🔳🔳🔳 ", "🔳    🔳  ", "🔳    🔳  "],
    'B': ['🔳🔳🔳 ', '🔳  🔳 ', '🔳🔳 ', '🔳  🔳 ', '🔳🔳🔳 '],
    'C': ['🔳🔳🔳 ', '🔳    ', '🔳    ', '🔳    ', '🔳🔳🔳 '],
    'D': ["🔳🔳🔳  ", "🔳    🔳 ", "🔳    🔳 ", "🔳    🔳 ", "🔳🔳🔳  "],
    'E': ["🔳🔳🔳🔳  ", "🔳        ", "🔳🔳🔳    ", "🔳        ", "🔳🔳🔳🔳  "],
    'F': ["🔳🔳🔳🔳 ", "🔳       ", "🔳🔳🔳     ", "🔳        ", "🔳        "],
    'G': [" 🔳🔳🔳  ", "🔳        ", "🔳  🔳🔳  ", "🔳   🔳  ", " 🔳🔳🔳    "],
    'H': ["🔳    🔳 ", "🔳    🔳 ", "🔳🔳🔳🔳 ", "🔳    🔳 ", "🔳    🔳 "],
    'I': ["🔳🔳🔳 ", "  🔳   ", "  🔳   ", "  🔳   ", "🔳🔳🔳 "],
    'J': ["  🔳🔳🔳 ", "    🔳   ", "    🔳   ", "🔳  🔳   ", " 🔳🔳     "],
    'K': ["🔳   🔳 ", "🔳  🔳  ", "🔳🔳   ", "🔳  🔳  ", "🔳   🔳 "],
    'L': ["🔳       ", "🔳       ", "🔳       ", "🔳       ", "🔳🔳🔳🔳 "],
    'M': [" 🔳    🔳 ", "🔳🔳  🔳🔳 ", "🔳 🔳🔳 🔳 ", "🔳  🔳  🔳 ", "🔳  🔳  🔳 "],
    'N': ["🔳    🔳 ", "🔳🔳  🔳 ", "🔳 🔳 🔳 ", "🔳  🔳🔳 ", "🔳    🔳 "],
    'O': ["  🔳🔳🔳 ", "🔳      🔳", "🔳      🔳", "🔳      🔳", "  🔳🔳🔳 "],
    'P': ["🔳🔳🔳  ", "🔳    🔳 ", "🔳🔳🔳  ", "🔳       ", "🔳       "],
    'Q': ["  🔳🔳🔳  ", "🔳      🔳 ", "🔳  🔳  🔳 ", "🔳    🔳 ", "  🔳🔳  🔳  "],
    'R': ["🔳🔳🔳    ", "🔳    🔳  ", "🔳🔳🔳    ", "🔳    🔳  ", "🔳     🔳 "],
    'S': [" 🔳🔳🔳 ", "🔳       ", " 🔳🔳🔳  ", "      🔳 ", "🔳🔳🔳  "],
    'T': ["🔳🔳🔳🔳 ", "   🔳    ", "   🔳    ", "   🔳    ", "   🔳    "],
    'U': ["🔳    🔳 ", "🔳    🔳 ", "🔳    🔳 ", "🔳    🔳 ", "🔳🔳🔳🔳 "],
    'V': ["🔳    🔳 ", "🔳    🔳 ", "🔳    🔳 ", " 🔳  🔳  ", "  🔳🔳   "],
    'W': ["🔳  🔳  🔳  ", "🔳  🔳  🔳  ", "🔳 🔳🔳 🔳  ", "🔳🔳  🔳🔳  ", " 🔳    🔳  "],
    'X': ["🔳     🔳  ", " 🔳   🔳   ", "  🔳 🔳    ", " 🔳   🔳   ", "🔳     🔳  "],
    'Y': ["🔳    🔳  ", " 🔳  🔳   ", "  🔳🔳    ", "   🔳     ", "   🔳     "],
    'Z': ["🔳🔳🔳🔳 ", "     🔳  ", "   🔳   ", " 🔳    ", "🔳🔳🔳🔳 "]

    # Add more shapes as needed
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    word = request.form['word'].upper()
    emoji = request.form['emoji']
    emoji_lines = [''] * 5
    
    for char in word:
        if char in shapes_mapping:
            shape = shapes_mapping[char]
            # Replace the mapping emoji with the selected emoji
            shape = [line.replace('🔳', emoji) for line in shape]
            for i, line in enumerate(shape):
                emoji_lines[i] += line
    
    emoji_text = '\n'.join(emoji_lines)
    return render_template('generate.html', emoji_text=emoji_text, word=word, emoji=emoji)