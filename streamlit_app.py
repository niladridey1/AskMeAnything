from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
def answer_question(question):
    prompt = f"Question: {question}\nAnswer:"

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop="\n",
        timeout=10,
    )

    answer = response.choices[0].text.strip()
    return answer
@app.route("/process_form", methods=["POST"])
def process_form():
    question = request.form.get("question")
    answer = answer_question(question)
    return render_template("result.html", question=question, answer=answer)
